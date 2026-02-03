# Scripts

## sync_orcid_publications.py

Syncs publications from **Naresh Kumar's ORCID** (0000-0002-0951-9621) to `publications.md`.

- Fetches works from the ORCID Public API (title, authors, year, journal, DOI, URL).
- Compares with existing entries in `publications.md` by **DOI** and **normalized title** to avoid duplicates.
- Appends only new publications into the correct year section (same HTML format as the rest of the page).
- Uses only Python standard library (no pip install).

**Run locally:**
```bash
python3 scripts/sync_orcid_publications.py
```

**Override ORCID (optional):**
```bash
ORCID_ID=0000-0002-0951-9621 python3 scripts/sync_orcid_publications.py
```

**GitHub Actions:** The workflow `.github/workflows/sync-orcid-publications.yml` runs this script on the 1st of each month and on manual trigger, then commits and pushes `publications.md` if there are new entries.
