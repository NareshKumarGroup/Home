# Scripts

## sync_orcid_publications.py

Syncs publications from ORCID (Naresh Kumar, `0000-0002-0951-9621`) to the site’s `_publications/` folder.

- **What it does:** Calls the ORCID Public API for the configured ORCID ID, fetches works, and adds any that aren’t already in `_publications/` (matched by DOI or slug). New entries are written as Jekyll markdown files with front matter (`title`, `authors`, `type`, `year`, `journal`, `doi`, `url`).
- **When it runs:** A GitHub Action runs this script on a schedule (1st of each month) and on manual trigger. See `.github/workflows/sync-orcid-publications.yml`.
- **Run locally:** From the repo root, `python3 scripts/sync_orcid_publications.py`. Uses `GITHUB_WORKSPACE` or current directory as repo root. Override ORCID with `ORCID_ID=0000-0002-0951-9621`.
