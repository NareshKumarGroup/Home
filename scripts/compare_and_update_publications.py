#!/usr/bin/env python3
"""
Compare ORCID _publications with manual publications.md and add missing entries.
Extracts DOIs from publications.md, loads _publications/*.md, finds ORCID pubs
whose DOI is not in the manual list, and inserts them into the correct year section.
"""

import os
import re
import sys

REPO_ROOT = os.environ.get("GITHUB_WORKSPACE") or os.environ.get("REPO_ROOT") or "."
PUBLICATIONS_MD = os.path.join(REPO_ROOT, "publications.md")
PUBLICATIONS_DIR = os.path.join(REPO_ROOT, "_publications")


def extract_dois_from_md(path):
    """Extract all DOIs from publications.md (from href='https://doi.org/...')."""
    dois = set()
    if not os.path.isfile(path):
        return dois
    with open(path, "r", encoding="utf-8", errors="ignore") as f:
        content = f.read()
    # Match doi.org/10.xxxx or doi.org/10.xxxx/yyyy
    for m in re.finditer(r"doi\.org/(10\.\S+?)(?:\"|'|&|\s|>)", content):
        doi = m.group(1).rstrip("'\">").strip()
        if doi:
            dois.add(doi.lower())
    return dois


def parse_front_matter(path):
    """Parse YAML front matter from a markdown file. Returns dict or None."""
    if not os.path.isfile(path):
        return None
    with open(path, "r", encoding="utf-8", errors="ignore") as f:
        content = f.read()
    if not content.strip().startswith("---"):
        return None
    parts = content.split("---", 2)
    if len(parts) < 3:
        return None
    # Simple YAML parse for our keys
    block = parts[1]
    data = {}
    for line in block.split("\n"):
        line = line.strip()
        if ":" in line:
            k, v = line.split(":", 1)
            k = k.strip()
            v = v.strip().strip('"').strip("'")
            data[k] = v
    return data


def load_orcid_publications(publications_dir):
    """Load all publications from _publications/*.md."""
    pubs = []
    if not os.path.isdir(publications_dir):
        return pubs
    for name in os.listdir(publications_dir):
        if not name.endswith(".md"):
            continue
        path = os.path.join(publications_dir, name)
        fm = parse_front_matter(path)
        if fm and fm.get("title"):
            pubs.append({
                "title": fm.get("title", ""),
                "authors": fm.get("authors", "Naresh Kumar et al."),
                "journal": fm.get("journal", ""),
                "doi": (fm.get("doi") or "").strip(),
                "url": (fm.get("url") or "").strip(),
                "year": str(fm.get("year", "0000")).strip(),
                "type": fm.get("type", "journal"),
            })
    return pubs


def find_year_sections(lines):
    """
    Find (start_line_index, end_line_index, year) for each year-section.
    end_line_index is the line of the closing </div> (0-based).
    """
    sections = []
    i = 0
    while i < len(lines):
        line = lines[i]
        if "year-section" in line and "<div" in line:
            year = None
            depth = 0
            j = i
            while j < len(lines):
                l = lines[j]
                depth += l.count("<div") - l.count("</div>")
                if year is None and "<h3>" in l:
                    m = re.search(r"<h3>\s*(\d{4})\s*</h3>", l)
                    if m:
                        year = m.group(1)
                if depth == 0:
                    if year:
                        sections.append((i, j, year))
                    break
                j += 1
        i += 1
    return sections


def publication_item_html(pub):
    """Generate one publication-item div block."""
    title_esc = pub["title"].replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;").replace('"', "&quot;")
    authors_esc = pub["authors"].replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;").replace('"', "&quot;")
    journal_esc = pub["journal"].replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;").replace('"', "&quot;")
    doi_url = pub["url"] if pub.get("url") else (f"https://doi.org/{pub['doi']}" if pub.get("doi") else "")
    link_line = f'<a href="{doi_url}" target="_blank"><i class="fas fa-external-link-alt"></i> DOI</a>' if doi_url else ""
    return f"""                    <div class="publication-item" data-type="{pub.get('type', 'journal')}">
                        <div class="publication-content">
                            <h4>{title_esc}</h4>
                            <p class="authors">{authors_esc}</p>
                            <p class="journal">{journal_esc}</p>
                            <div class="publication-links">
                                {link_line}
                            </div>
                        </div>
                    </div>

"""


def main():
    manual_dois = extract_dois_from_md(PUBLICATIONS_MD)
    orcid_pubs = load_orcid_publications(PUBLICATIONS_DIR)

    missing = []
    for p in orcid_pubs:
        doi = (p.get("doi") or "").lower()
        if doi and doi in manual_dois:
            continue
        if not doi:
            # No DOI - could still add; for now skip or add by title+year
            pass
        missing.append(p)

    # Group missing by year (newest first for insertion order)
    by_year = {}
    for p in missing:
        y = p.get("year", "0000")
        if y not in by_year:
            by_year[y] = []
        by_year[y].append(p)

    if not by_year:
        print("No missing publications to add.")
        return 0

    with open(PUBLICATIONS_MD, "r", encoding="utf-8", errors="ignore") as f:
        lines = f.readlines()

    sections = find_year_sections(lines)
    # Map year -> (end_line_index) where we insert before that line
    year_end_line = {y: end for _, end, y in sections}

    # Build insertions: (line_index, list of HTML blocks to insert)
    insertions = []
    for year, pubs in sorted(by_year.items(), key=lambda x: -int(x[0]) if x[0].isdigit() else 0):
        if year not in year_end_line:
            # No section for this year - append at end of last section or after first year-section
            if sections:
                insert_at = sections[-1][1]  # end of last section
            else:
                insert_at = 0
            year_end_line[year] = insert_at
        insert_at = year_end_line[year]
        block = "".join(publication_item_html(p) for p in pubs)
        insertions.append((insert_at, block))

    # Sort insertions by line index descending so we insert from bottom up (preserves indices)
    insertions.sort(key=lambda x: -x[0])

    for line_idx, block in insertions:
        # Insert block before line_idx (so new lines go before the closing </div>)
        new_lines = block.splitlines(keepends=True)
        if new_lines and not new_lines[-1].endswith("\n"):
            new_lines[-1] += "\n"
        lines[line_idx:line_idx] = new_lines

    with open(PUBLICATIONS_MD, "w", encoding="utf-8") as f:
        f.writelines(lines)

    total_added = sum(len(by_year[y]) for y in by_year)
    print(f"Manual DOIs found: {len(manual_dois)}")
    print(f"ORCID publications: {len(orcid_pubs)}")
    print(f"Missing (not in manual): {len(missing)}")
    print(f"Added to publications.md: {total_added}")
    for y in sorted(by_year.keys(), key=lambda x: -int(x) if x.isdigit() else 0):
        print(f"  Year {y}: {len(by_year[y])} publication(s)")
    return 0


if __name__ == "__main__":
    sys.exit(main())
