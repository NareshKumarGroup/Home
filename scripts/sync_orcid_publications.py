#!/usr/bin/env python3
"""
Sync publications from Naresh Kumar's ORCID to publications.md.
Fetches works from ORCID Public API, enriches with CrossRef (full authors, journal, year),
and appends new entries to the publications page.
Only adds works that don't already exist (matched by DOI or normalized title).
Uses only Python stdlib (urllib, xml.etree, re, os, html, json).
"""

import html
import json
import os
import re
import sys
import time
import urllib.parse
import urllib.request
import xml.etree.ElementTree as ET

ORCID_API = "https://pub.orcid.org/v3.0"
CROSSREF_API = "https://api.crossref.org/works"
NARESH_ORCID = "0000-0002-0951-9621"


def local_tag(elem):
    """Return tag without namespace (local name)."""
    if elem.tag is None:
        return ""
    return elem.tag.split("}")[-1] if "}" in elem.tag else elem.tag


def get_child_text(parent, tag_name):
    """Get text of first child with given local tag name."""
    if parent is None:
        return None
    for c in parent:
        if local_tag(c) == tag_name and c.text and c.text.strip():
            return c.text.strip()
        t = get_child_text(c, tag_name)
        if t:
            return t
    return None


def get_year_from_publication_date(parent):
    """Extract year from publication-date element."""
    if parent is None:
        return None
    for c in parent:
        if local_tag(c) == "publication-date":
            y = get_child_text(c, "year")
            if y:
                return y
            for cc in c:
                if local_tag(cc) == "year" and cc.text:
                    return cc.text.strip()
        elif "publication" in local_tag(c).lower():
            return get_year_from_publication_date(c)
    return None


def get_doi_from_external_ids(parent):
    """Extract DOI from external-ids."""
    if parent is None:
        return None
    for c in parent.iter():
        if local_tag(c) == "external-ids":
            for ext in c:
                if local_tag(ext) == "external-id":
                    etype = None
                    value = None
                    for cc in ext:
                        if local_tag(cc) == "external-id-type" and cc.text:
                            etype = cc.text.strip().lower()
                        if local_tag(cc) == "external-id-value" and cc.text:
                            value = cc.text.strip()
                    if etype == "doi" and value:
                        return value
        elif local_tag(c) == "external-id":
            etype = None
            value = None
            for cc in c:
                if local_tag(cc) == "external-id-type" and cc.text:
                    etype = cc.text.strip().lower()
                if local_tag(cc) == "external-id-value" and cc.text:
                    value = cc.text.strip()
            if etype == "doi" and value:
                return value
    return None


def get_contributors_from_work(elem):
    """Extract list of author names from contributors (credit-name)."""
    authors = []
    for c in elem.iter():
        if local_tag(c) == "contributors":
            for contrib in c:
                if local_tag(contrib) == "contributor":
                    name = get_child_text(contrib, "credit-name")
                    if name and name.strip():
                        authors.append(name.strip())
    return authors


def parse_work_summary(elem):
    """Parse one work-summary element into a dict. Returns None if no title."""
    title = get_child_text(elem, "title")
    if not title:
        return None
    year = get_year_from_publication_date(elem) or get_child_text(elem, "year")
    if not year or not str(year).isdigit():
        year = "0000"
    work_type = get_child_text(elem, "type") or "journal-article"
    type_map = {"journal-article": "journal", "book": "book", "book-chapter": "book", "conference-paper": "journal"}
    pub_type = type_map.get(work_type, "journal") if work_type else "journal"
    journal = get_child_text(elem, "journal-title") or ""
    doi = get_doi_from_external_ids(elem)
    url = get_child_text(elem, "url") or ""
    if doi and not url:
        url = f"https://doi.org/{doi}"
    authors_list = get_contributors_from_work(elem)
    authors_str = ", ".join(authors_list) if authors_list else "Naresh Kumar et al."
    return {
        "title": title,
        "year": str(year),
        "type": pub_type,
        "journal": journal,
        "doi": doi or "",
        "url": url,
        "authors": authors_str,
    }


def fetch_orcid_works(orcid_id):
    """Fetch works from ORCID Public API. Returns list of work dicts."""
    url = f"{ORCID_API}/{orcid_id}/works"
    req = urllib.request.Request(url, headers={"Accept": "application/orcid+xml"})
    with urllib.request.urlopen(req, timeout=30) as resp:
        body = resp.read().decode("utf-8", errors="replace")
    root = ET.fromstring(body)
    works = []
    for elem in root.iter():
        if local_tag(elem) == "work-summary":
            w = parse_work_summary(elem)
            if w and w.get("title"):
                works.append(w)
    seen = set()
    out = []
    for w in works:
        key = (w.get("doi") or "").strip() or (w.get("title", "") + w.get("year", ""))
        if key and key not in seen:
            seen.add(key)
            out.append(w)
    return out


def strip_html_from_title(title):
    """Remove HTML tags from title (e.g. <i>H</i> -> H)."""
    if not title:
        return ""
    return re.sub(r"<[^>]+>", "", title).strip()


def fetch_crossref_metadata(doi):
    """Fetch full metadata from CrossRef by DOI. Returns dict with authors, journal, year, title or None."""
    if not doi or not doi.strip():
        return None
    enc_doi = urllib.parse.quote(doi.strip())
    url = f"{CROSSREF_API}/{enc_doi}"
    req = urllib.request.Request(url, headers={"User-Agent": "KumarGroupWebsite/1.0 (mailto:n.kumar@unsw.edu.au)"})
    try:
        with urllib.request.urlopen(req, timeout=15) as resp:
            data = json.loads(resp.read().decode("utf-8", errors="replace"))
    except Exception:
        return None
    msg = data.get("message") or {}
    authors_list = msg.get("author") or []
    author_parts = []
    for a in authors_list:
        given = (a.get("given") or "").strip()
        family = (a.get("family") or "").strip()
        if family:
            name = f"{given} {family}".strip() if given else family
            author_parts.append(name)
    authors_str = ", ".join(author_parts) if author_parts else None
    container = msg.get("container-title") or []
    journal = (container[0] or "").strip() if container else None
    published = msg.get("published") or msg.get("created") or {}
    date_parts = published.get("date-parts") or []
    year = None
    if date_parts and date_parts[0]:
        year = str(date_parts[0][0]) if date_parts[0][0] else None
    title_list = msg.get("title") or []
    title = (title_list[0] or "").strip() if title_list else None
    if title:
        title = strip_html_from_title(title)
    return {
        "authors": authors_str,
        "journal": journal,
        "year": year,
        "title": title,
    }


def enrich_work_with_crossref(work):
    """Enrich work dict with full authors, journal, year from CrossRef when DOI present."""
    doi = (work.get("doi") or "").strip()
    if not doi:
        return work
    meta = fetch_crossref_metadata(doi)
    if not meta:
        return work
    if meta.get("authors"):
        work["authors"] = meta["authors"]
    if meta.get("journal"):
        work["journal"] = meta["journal"]
    if meta.get("year"):
        work["year"] = meta["year"]
    if meta.get("title"):
        work["title"] = meta["title"]
    return work


def normalize_title(title):
    """Normalize title for comparison (lowercase, collapse spaces, strip HTML)."""
    if not title:
        return ""
    s = strip_html_from_title(title)
    s = re.sub(r"\s+", " ", s.lower().strip())
    return s[:200]


def load_existing_from_publications_md(filepath):
    """Load set of DOIs and normalized titles from publications.md."""
    existing_dois = set()
    existing_titles = set()
    if not os.path.isfile(filepath):
        return existing_dois, existing_titles
    try:
        with open(filepath, "r", encoding="utf-8", errors="ignore") as f:
            content = f.read()
        for m in re.finditer(r'href="https://doi\.org/([^"]+)"', content):
            doi = m.group(1).strip()
            if doi:
                existing_dois.add(doi.lower())
        for m in re.finditer(r"<h4>([^<]+)</h4>", content):
            t = normalize_title(m.group(1))
            if t:
                existing_titles.add(t)
    except Exception as e:
        print(f"Warning: could not read existing publications: {e}", file=sys.stderr)
    return existing_dois, existing_titles


def publication_html_block(work):
    """Generate one publication HTML block for publications.md."""
    title = strip_html_from_title(work.get("title") or "")
    authors = work.get("authors") or "Naresh Kumar et al."
    journal = work.get("journal") or ""
    doi = work.get("doi") or ""
    url = work.get("url") or (f"https://doi.org/{doi}" if doi else "")
    title_esc = html.escape(title)
    authors_esc = html.escape(authors)
    journal_esc = html.escape(journal)
    pub_type = work.get("type") or "journal"
    lines = [
        "",
        "                    <div class=\"publication-item\" data-type=\"" + pub_type + "\">",
        "                        <div class=\"publication-content\">",
        "                            <h4>" + title_esc + "</h4>",
        "                            <p class=\"authors\">" + authors_esc + "</p>",
        "                            <p class=\"journal\">" + journal_esc + "</p>",
    ]
    if doi or url:
        lines.append("                            <div class=\"publication-links\">")
        link = f"https://doi.org/{doi}" if doi else url
        lines.append('                                <a href="' + html.escape(link) + '" target="_blank"><i class="fas fa-external-link-alt"></i> DOI</a>')
        lines.append("                            </div>")
    lines.append("                        </div>")
    lines.append("                    </div>")
    return "\n".join(lines)


def update_existing_publications_with_crossref(filepath):
    """Update existing publication blocks in publications.md with full authors and journal from CrossRef."""
    try:
        with open(filepath, "r", encoding="utf-8", errors="ignore") as f:
            content = f.read()
    except Exception as e:
        print(f"Error reading {filepath}: {e}", file=sys.stderr)
        return 0
    # Find each DOI link and the authors/journal lines that precede it (same block)
    blocks = []
    for m in re.finditer(r'href="https://doi\.org/([^"]+)"', content):
        doi = m.group(1).strip()
        pos = m.start()
        before = content[:pos]
        auth_m = list(re.finditer(r'<p class="authors">([^<]*)</p>', before))
        jour_m = list(re.finditer(r'<p class="journal">([^<]*)</p>', before))
        if auth_m and jour_m:
            last_auth, last_jour = auth_m[-1], jour_m[-1]
            blocks.append((doi, last_auth.start(), last_auth.end(), last_jour.start(), last_jour.end()))
    if not blocks:
        return 0
    # Fetch CrossRef for each DOI and build replacements (start, end, new_text)
    replacements = []
    seen_spans = set()
    for doi, a_start, a_end, j_start, j_end in blocks:
        meta = fetch_crossref_metadata(doi)
        time.sleep(0.35)
        if not meta:
            continue
        if meta.get("authors") and (a_start, a_end) not in seen_spans:
            seen_spans.add((a_start, a_end))
            replacements.append((a_start, a_end, "<p class=\"authors\">" + html.escape(meta["authors"]) + "</p>"))
        if meta.get("journal") and (j_start, j_end) not in seen_spans:
            seen_spans.add((j_start, j_end))
            replacements.append((j_start, j_end, "<p class=\"journal\">" + html.escape(meta["journal"]) + "</p>"))
    # Apply in reverse order by start so positions don't shift
    for start, end, new_text in sorted(replacements, key=lambda x: -x[0]):
        content = content[:start] + new_text + content[end:]
    try:
        with open(filepath, "w", encoding="utf-8") as f:
            f.write(content)
    except Exception as e:
        print(f"Error writing {filepath}: {e}", file=sys.stderr)
        return 0
    return len(blocks)


def insert_new_publications_into_md(filepath, new_works):
    """Insert new publication HTML blocks into publications.md by year."""
    if not new_works:
        return 0
    by_year = {}
    for w in new_works:
        y = w.get("year") or "0000"
        by_year.setdefault(y, []).append(w)
    try:
        with open(filepath, "r", encoding="utf-8", errors="ignore") as f:
            content = f.read()
    except Exception as e:
        print(f"Error reading {filepath}: {e}", file=sys.stderr)
        return 0

    # 1) Insert into existing year sections (after <h3>YEAR</h3>)
    years_without_section = []
    for year in sorted(by_year.keys(), reverse=True):
        pattern = re.compile(
            r"(<!-- " + re.escape(year) + r" -->\s*\n\s*<div class=\"year-section\">\s*\n\s*<h3>" + re.escape(year) + r"</h3>)\s*\n",
            re.IGNORECASE,
        )
        block = "\n".join(publication_html_block(w) for w in by_year[year])
        replacement = r"\1\n\n" + block + "\n"
        if pattern.search(content):
            content = pattern.sub(replacement, content, count=1)
        else:
            years_without_section.append(year)

    # 2) For years that had no section, add new sections at top (newest first)
    new_years = sorted(years_without_section, reverse=True)
    if new_years:
        new_sections = []
        for year in new_years:
            block = "\n".join(publication_html_block(w) for w in by_year[year])
            new_sections.append(
                "\n                <!-- "
                + year
                + " -->\n                <div class=\"year-section\">\n                    <h3>"
                + year
                + "</h3>\n"
                + block
                + "\n                </div>"
            )
        insert_marker = '<div class="publications-list">'
        idx = content.find(insert_marker)
        if idx != -1:
            end = idx + len(insert_marker)
            content = content[:end] + "\n" + "\n".join(new_sections) + content[end:]
        else:
            content += "\n" + "\n".join(new_sections)

    try:
        with open(filepath, "w", encoding="utf-8") as f:
            f.write(content)
    except Exception as e:
        print(f"Error writing {filepath}: {e}", file=sys.stderr)
        return 0
    return sum(len(ws) for ws in by_year.values())


def main():
    repo_root = os.environ.get("GITHUB_WORKSPACE") or os.environ.get("REPO_ROOT") or os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    orcid_id = os.environ.get("ORCID_ID") or NARESH_ORCID
    publications_md = os.path.join(repo_root, "publications.md")
    update_existing = os.environ.get("UPDATE_EXISTING", "").strip().lower() in ("1", "true", "yes")

    # Optionally update existing entries with full authors/journal from CrossRef
    if update_existing:
        updated = update_existing_publications_with_crossref(publications_md)
        print(f"Existing publications updated with CrossRef: {updated}")

    existing_dois, existing_titles = load_existing_from_publications_md(publications_md)
    try:
        works = fetch_orcid_works(orcid_id)
    except Exception as e:
        print(f"Failed to fetch ORCID works: {e}", file=sys.stderr)
        return 1

    new_works = []
    for w in works:
        doi = (w.get("doi") or "").strip()
        title_norm = normalize_title(w.get("title") or "")
        if doi and doi.lower() in existing_dois:
            continue
        if title_norm and title_norm in existing_titles:
            continue
        new_works.append(w)
        if doi:
            existing_dois.add(doi.lower())
        if title_norm:
            existing_titles.add(title_norm)

    # Enrich each new work with full authors, journal, year from CrossRef (by DOI)
    for w in new_works:
        enrich_work_with_crossref(w)
        time.sleep(0.35)  # be nice to CrossRef API

    added = insert_new_publications_into_md(publications_md, new_works)
    print(f"ORCID works fetched: {len(works)}")
    print(f"New publications added: {added}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
