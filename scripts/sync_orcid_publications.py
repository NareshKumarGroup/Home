#!/usr/bin/env python3
"""
Sync publications from ORCID to publications.md (FULL METADATA VERSION)

- Fetches work summaries from ORCID
- Fetches full work records using put-code
- Extracts complete authors, year, journal, DOI, URL
- Avoids duplicates using DOI or normalized title
- Inserts publications grouped by year
- Uses ONLY Python standard library
"""

import html
import os
import re
import sys
import time
import urllib.request
import xml.etree.ElementTree as ET

ORCID_API = "https://pub.orcid.org/v3.0"
DEFAULT_ORCID = "0000-0002-0951-9621"


# -------------------- XML HELPERS --------------------

def local(tag):
    return tag.split("}")[-1] if "}" in tag else tag


def find_text(root, tag_name):
    for e in root.iter():
        if local(e.tag) == tag_name and e.text and e.text.strip():
            return e.text.strip()
    return None


def normalize_title(title):
    return re.sub(r"\s+", " ", title.lower().strip())[:200] if title else ""


# -------------------- ORCID FETCHING --------------------

def fetch_xml(url):
    req = urllib.request.Request(url, headers={"Accept": "application/orcid+xml"})
    with urllib.request.urlopen(req, timeout=30) as r:
        return ET.fromstring(r.read().decode("utf-8", errors="replace"))


def get_put_code(ws):
    """Get put-code from work-summary element (may be namespaced)."""
    put_code = ws.attrib.get("put-code")
    if put_code:
        return put_code
    for k, v in (ws.attrib or {}).items():
        if v and (k == "put-code" or k.endswith("put-code")):
            return v
    return None


def fetch_work_summaries(orcid_id):
    root = fetch_xml(f"{ORCID_API}/{orcid_id}/works")
    summaries = []

    for ws in root.iter():
        if local(ws.tag) == "work-summary":
            put_code = get_put_code(ws)
            title = find_text(ws, "title")
            if put_code and title:
                summaries.append({
                    "put_code": put_code,
                    "title": title
                })
    return summaries


def fetch_full_work(orcid_id, put_code):
    return fetch_xml(f"{ORCID_API}/{orcid_id}/work/{put_code}")


# -------------------- FULL METADATA PARSING --------------------

def get_publication_date(root):
    """Extract (year, month, day) from publication-date in ORCID work. Returns (year, month, day) as strings; month/day are "00" if missing."""
    year, month, day = "0000", "00", "00"
    for e in root.iter():
        if local(e.tag) == "publication-date":
            year = find_text(e, "year") or year
            m = find_text(e, "month")
            if m and m.isdigit():
                month = m.zfill(2) if len(m) < 2 else m[:2]
            d = find_text(e, "day")
            if d and d.isdigit():
                day = d.zfill(2) if len(d) < 2 else d[:2]
            break
    if not year or not year.isdigit():
        year = find_text(root, "year") or "0000"
    return (year if year.isdigit() else "0000", month, day)


def parse_full_work(root):
    title = find_text(root, "title")
    journal = find_text(root, "journal-title") or ""
    year, month, day = get_publication_date(root)
    if not year or not year.isdigit():
        year = "0000"
    doi = ""
    url = ""

    authors = []

    for e in root.iter():
        if local(e.tag) == "credit-name" and e.text:
            authors.append(e.text.strip())

        if local(e.tag) == "external-id":
            id_type = find_text(e, "external-id-type")
            id_val = find_text(e, "external-id-value")
            if id_type and id_type.lower() == "doi":
                doi = id_val

    if doi:
        url = f"https://doi.org/{doi}"
    else:
        url = find_text(root, "url") or ""

    # Sort key YYYYMMDD for latest-first ordering (missing month/day treated as 01)
    m, d = month if month != "00" else "01", day if day != "00" else "01"
    date_sort = f"{year}{m}{d}"

    return {
        "title": title,
        "authors": ", ".join(authors) if authors else "Naresh Kumar et al.",
        "journal": journal,
        "year": year,
        "doi": doi or "",
        "url": url,
        "type": "journal",
        "date_sort": date_sort,
    }


# -------------------- EXISTING PUBLICATIONS --------------------

def load_existing(filepath):
    dois, titles = set(), set()

    if not os.path.isfile(filepath):
        return dois, titles

    content = open(filepath, encoding="utf-8", errors="ignore").read()

    for m in re.finditer(r'https://doi.org/([^"]+)', content):
        dois.add(m.group(1).lower())

    for m in re.finditer(r"<h4>([^<]+)</h4>", content):
        titles.add(normalize_title(m.group(1)))

    return dois, titles


# -------------------- HTML GENERATION --------------------

def publication_block(w):
    return f"""
                    <div class="publication-item" data-type="{w['type']}">
                        <div class="publication-content">
                            <h4>{html.escape(w['title'])}</h4>
                            <p class="authors">{html.escape(w['authors'])}</p>
                            <p class="journal">{html.escape(w['journal'])}</p>
                            <div class="publication-links">
                                <a href="{html.escape(w['url'])}" target="_blank">
                                    <i class="fas fa-external-link-alt"></i> DOI
                                </a>
                            </div>
                        </div>
                    </div>
""".rstrip()


# -------------------- UPDATE EXISTING (FIX INCOMPLETE) --------------------

def strip_html(s):
    return re.sub(r"<[^>]+>", "", s).strip() if s else ""


def parse_publication_blocks(content):
    """Find all publication blocks: (title, authors, journal, doi, match_obj)."""
    # Capture h4, authors content, journal content with positions for replacement
    pat = re.compile(
        r"(<h4>)([^<]+)(</h4>\s*<p class=\"authors\">)([^<]*)(</p>\s*<p class=\"journal\">)([^<]*)(</p>)",
        re.DOTALL,
    )
    blocks = []
    for m in pat.finditer(content):
        title = strip_html(m.group(2))
        authors = (m.group(4) or "").strip()
        journal = (m.group(6) or "").strip()
        # DOI: look in next 600 chars
        chunk = content[m.end() : m.end() + 600]
        doi_m = re.search(r'href="https://doi\.org/([^"]+)"', chunk)
        doi = doi_m.group(1).strip() if doi_m else None
        if not doi:
            doi_m = re.search(r"https://doi\.org/([^\s\"'<>]+)", chunk)
            doi = doi_m.group(1).strip() if doi_m else None
        blocks.append({
            "title": title,
            "authors": authors,
            "journal": journal,
            "doi": doi,
            "match": m,
        })
    return blocks


def is_incomplete(block):
    """True if authors or journal look missing/incomplete."""
    a = (block.get("authors") or "").strip()
    j = (block.get("journal") or "").strip()
    if a == "Naresh Kumar et al." or not a:
        return True
    if not j or len(j) < 3:
        return True
    # Truncated authors (ends with ...)
    if a.endswith("..."):
        return True
    return False


def update_existing_publications(filepath, orcid_id):
    """Find incomplete entries in publications.md, match to ORCID, fetch full metadata, replace."""
    with open(filepath, "r", encoding="utf-8", errors="ignore") as f:
        content = f.read()

    blocks = parse_publication_blocks(content)
    incomplete = [b for b in blocks if is_incomplete(b)]
    if not incomplete:
        print("No incomplete publications found.")
        return 0

    summaries = fetch_work_summaries(orcid_id)
    title_to_put_code = {}
    for s in summaries:
        t = normalize_title(s["title"])
        if t:
            title_to_put_code[t] = s["put_code"]
    # Also by stripped title (no HTML)
    for s in summaries:
        t = normalize_title(strip_html(s["title"]))
        if t and t not in title_to_put_code:
            title_to_put_code[t] = s["put_code"]

    replacements = []
    for block in incomplete:
        title_norm = normalize_title(block["title"])
        put_code = title_to_put_code.get(title_norm)
        if not put_code:
            # Try without punctuation / extra chars
            t2 = re.sub(r"[^\w\s]", "", title_norm).strip()[:180]
            for k, pc in title_to_put_code.items():
                k2 = re.sub(r"[^\w\s]", "", k).strip()[:180]
                if k2 == t2 or t2 in k2 or k2 in t2:
                    put_code = pc
                    break
        if not put_code:
            continue
        try:
            full_root = fetch_full_work(orcid_id, put_code)
            w = parse_full_work(full_root)
        except Exception:
            continue
        m = block["match"]
        new_authors = html.escape(w["authors"])
        new_journal = html.escape(w["journal"])
        new_block = m.group(1) + m.group(2) + m.group(3) + new_authors + m.group(5) + new_journal + m.group(7)
        replacements.append((m.start(), m.end(), new_block))
        # Avoid rate limiting
        time.sleep(0.25)

    # Apply from end to start so positions stay valid
    for start, end, new_block in sorted(replacements, key=lambda x: -x[0]):
        content = content[:start] + new_block + content[end:]

    if replacements:
        with open(filepath, "w", encoding="utf-8") as f:
            f.write(content)
    return len(replacements)


# -------------------- INSERT INTO MD --------------------

def insert_publications(filepath, works):
    if not works:
        return 0

    by_year = {}
    for w in works:
        by_year.setdefault(w["year"], []).append(w)

    content = open(filepath, encoding="utf-8").read()

    for year in sorted(by_year.keys(), reverse=True):
        # Sort by publication date (latest first); date_sort is YYYYMMDD
        items = sorted(by_year[year], key=lambda w: w.get("date_sort", w["year"] + "0101"), reverse=True)
        block = "\n".join(publication_block(w) for w in items)

        pattern = re.compile(
            rf"(<!-- {year} -->\s*<div class=\"year-section\">\s*<h3>{year}</h3>)",
            re.IGNORECASE
        )

        if pattern.search(content):
            content = pattern.sub(rf"\1\n{block}", content, count=1)
        else:
            new_section = f"""
                <!-- {year} -->
                <div class="year-section">
                    <h3>{year}</h3>
{block}
                </div>
"""
            marker = '<div class="publications-list">'
            content = content.replace(marker, marker + new_section, 1)

    open(filepath, "w", encoding="utf-8").write(content)
    return sum(len(v) for v in by_year.values())


# -------------------- MAIN --------------------

def main():
    import argparse
    parser = argparse.ArgumentParser(description="Sync ORCID publications to publications.md")
    parser.add_argument("--update-existing", action="store_true", help="Fix incomplete entries (e.g. 'Naresh Kumar et al.') by fetching full metadata from ORCID")
    args = parser.parse_args()

    repo_root = os.environ.get("GITHUB_WORKSPACE") or os.getcwd()
    orcid_id = os.environ.get("ORCID_ID") or DEFAULT_ORCID
    publications_md = os.path.join(repo_root, "publications.md")

    if args.update_existing:
        updated = update_existing_publications(publications_md, orcid_id)
        print(f"Updated {updated} incomplete publication(s) from ORCID.")
        return 0

    existing_dois, existing_titles = load_existing(publications_md)

    summaries = fetch_work_summaries(orcid_id)
    new_works = []

    for s in summaries:
        full_root = fetch_full_work(orcid_id, s["put_code"])
        w = parse_full_work(full_root)

        doi = w["doi"].lower()
        title_norm = normalize_title(w["title"])

        if doi and doi in existing_dois:
            continue
        if title_norm in existing_titles:
            continue

        new_works.append(w)
        if doi:
            existing_dois.add(doi)
        existing_titles.add(title_norm)

    added = insert_publications(publications_md, new_works)

    print(f"ORCID works processed: {len(summaries)}")
    print(f"New publications added: {added}")


if __name__ == "__main__":
    main()
