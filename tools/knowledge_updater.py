"""
knowledge_updater.py — Skill 6: mental-health-guidance
Self-improving knowledge pipeline: fetches latest clinical evidence and appends to SECOND-KNOWLEDGE-BRAIN.md.

Sources:
  - PubMed NCBI Entrez API (free, no key required for basic use)
  - Cochrane Library search (HTML scrape via crawl4ai)
  - NICE guidelines pages (HTML scrape via crawl4ai)

Schedule: Run weekly (e.g., cron every Sunday 02:00)
Usage: python knowledge_updater.py [--dry-run] [--max-results N]
"""

import hashlib
import json
import re
import time
import argparse
from datetime import datetime, timedelta
from pathlib import Path
from typing import Optional
import urllib.parse
import urllib.request
import urllib.error

# ── Configuration ────────────────────────────────────────────────────────────

BRAIN_PATH = Path(__file__).parent.parent / "SECOND-KNOWLEDGE-BRAIN.md"

PUBMED_BASE = "https://eutils.ncbi.nlm.nih.gov/entrez/eutils"

PUBMED_QUERIES = [
    "CBT depression randomized controlled trial",
    "GAD generalized anxiety disorder treatment meta-analysis",
    "PTSD psychotherapy systematic review",
    "DBT dialectical behavior therapy randomized trial",
    "ACT acceptance commitment therapy anxiety depression",
    "MBCT mindfulness cognitive therapy relapse",
    "motivational interviewing substance use",
    "behavioral activation depression RCT",
    "PHQ-9 screening validity",
    "mental health digital intervention",
]

NICE_URLS = [
    "https://www.nice.org.uk/guidance/cg90",    # Depression
    "https://www.nice.org.uk/guidance/cg113",   # GAD
    "https://www.nice.org.uk/guidance/ng116",   # PTSD
    "https://www.nice.org.uk/guidance/cg31",    # OCD
]

MAX_AGE_DAYS = 365          # Only include papers from last 365 days
MAX_RESULTS_PER_QUERY = 5   # PubMed results per query
DELAY_BETWEEN_REQUESTS = 0.4  # Seconds — respect NCBI rate limits (3 req/sec)


# ── Utilities ─────────────────────────────────────────────────────────────────

def url_hash(url_or_doi: str) -> str:
    """Compute a short hash for deduplication."""
    return hashlib.md5(url_or_doi.lower().strip().encode()).hexdigest()[:12]


def load_existing_hashes(brain_path: Path) -> set:
    """Extract all DOI/URL hashes already in SECOND-KNOWLEDGE-BRAIN.md."""
    if not brain_path.exists():
        return set()
    content = brain_path.read_text(encoding="utf-8")
    dois = re.findall(r"10\.\d{4,}/[^\s\)\"']+", content)
    urls = re.findall(r"https?://[^\s\)\"']+", content)
    return {url_hash(x) for x in dois + urls}


def http_get(url: str, timeout: int = 15) -> Optional[str]:
    """Simple HTTP GET — returns response body as string or None on error."""
    try:
        req = urllib.request.Request(url, headers={"User-Agent": "MentalHealthGuidanceBot/1.0"})
        with urllib.request.urlopen(req, timeout=timeout) as resp:
            return resp.read().decode("utf-8", errors="replace")
    except (urllib.error.URLError, urllib.error.HTTPError, Exception):
        return None


# ── PubMed Fetcher ────────────────────────────────────────────────────────────

def pubmed_search(query: str, max_results: int, min_date: str) -> list[str]:
    """Search PubMed and return a list of PMIDs."""
    params = urllib.parse.urlencode({
        "db": "pubmed",
        "term": query,
        "retmax": max_results,
        "retmode": "json",
        "sort": "relevance",
        "mindate": min_date,
        "datetype": "pdat",
    })
    url = f"{PUBMED_BASE}/esearch.fcgi?{params}"
    body = http_get(url)
    if not body:
        return []
    try:
        data = json.loads(body)
        return data.get("esearchresult", {}).get("idlist", [])
    except json.JSONDecodeError:
        return []


def pubmed_fetch(pmids: list[str]) -> list[dict]:
    """Fetch article summaries for a list of PMIDs. Returns list of dicts."""
    if not pmids:
        return []
    ids = ",".join(pmids)
    params = urllib.parse.urlencode({
        "db": "pubmed",
        "id": ids,
        "retmode": "json",
        "rettype": "abstract",
    })
    url = f"{PUBMED_BASE}/esummary.fcgi?{params}"
    body = http_get(url)
    if not body:
        return []
    try:
        data = json.loads(body)
        results = data.get("result", {})
        articles = []
        for pmid in pmids:
            art = results.get(pmid, {})
            if not art:
                continue
            authors_raw = art.get("authors", [])
            authors = ", ".join(a.get("name", "") for a in authors_raw[:3])
            if len(authors_raw) > 3:
                authors += " et al."
            pub_date = art.get("pubdate", "")[:4]  # Year only
            title = art.get("title", "").rstrip(".")
            journal = art.get("fulljournalname", art.get("source", ""))
            doi = next(
                (
                    aid.get("value", "")
                    for aid in art.get("articleids", [])
                    if aid.get("idtype") == "doi"
                ),
                "",
            )
            url_val = f"https://pubmed.ncbi.nlm.nih.gov/{pmid}/"
            articles.append({
                "title": title,
                "authors": authors,
                "year": pub_date,
                "journal": journal,
                "doi": doi,
                "url": url_val,
                "pmid": pmid,
            })
        return articles
    except json.JSONDecodeError:
        return []


def classify_evidence_level(title: str, journal: str) -> str:
    """Heuristic evidence level classification from title/journal keywords."""
    title_lower = title.lower()
    if any(k in title_lower for k in ["systematic review", "meta-analysis", "cochrane"]):
        return "Meta-Analysis / Systematic Review"
    if any(k in title_lower for k in ["randomized", "rct", "controlled trial"]):
        return "RCT"
    if any(k in title_lower for k in ["cohort", "longitudinal", "prospective"]):
        return "Cohort Study"
    if any(k in title_lower for k in ["guideline", "recommendation", "consensus"]):
        return "Clinical Guideline"
    return "Peer-Reviewed Study"


def infer_relevance(title: str, query: str) -> str:
    """Generate a short relevance note."""
    frameworks = {
        "CBT": "CBT", "cognitive behav": "CBT", "dialectical": "DBT",
        "acceptance": "ACT", "motivational": "MI", "mindfulness": "MBCT",
        "behavioral activation": "BA",
    }
    conditions = {
        "depress": "depression", "anxiety": "anxiety", "GAD": "GAD",
        "PTSD": "PTSD", "trauma": "PTSD", "substance": "substance use",
        "alcohol": "alcohol use",
    }
    fw = next((v for k, v in frameworks.items() if k.lower() in title.lower()), "")
    cond = next((v for k, v in conditions.items() if k.lower() in title.lower()), "")
    if fw and cond:
        return f"{fw} for {cond}"
    if fw:
        return f"{fw} framework evidence"
    if cond:
        return f"{cond} treatment evidence"
    return "General mental health treatment evidence"


# ── NICE Fetcher ──────────────────────────────────────────────────────────────

def fetch_nice_guideline(url: str) -> Optional[dict]:
    """Fetch NICE guideline page title and summary (minimal parse)."""
    body = http_get(url)
    if not body:
        return None
    title_match = re.search(r"<title>([^<]+)</title>", body)
    title = title_match.group(1).strip() if title_match else "NICE Guideline"
    title = re.sub(r"\s*\|\s*NICE.*$", "", title)
    code_match = re.search(r"nice\.org\.uk/guidance/([a-z0-9]+)", url)
    code = code_match.group(1).upper() if code_match else ""
    year_match = re.search(r"Published:\s*(\d{4})", body) or re.search(r"Last updated:\s*\w+ (\d{4})", body)
    year = year_match.group(1) if year_match else datetime.now().strftime("%Y")
    return {
        "title": f"NICE {code}: {title}",
        "authors": "National Institute for Health and Care Excellence (NICE)",
        "year": year,
        "journal": "NICE Clinical Guidelines",
        "doi": "",
        "url": url,
    }


# ── Entry Formatter ───────────────────────────────────────────────────────────

def format_entry(article: dict, query: str = "") -> str:
    """Format an article dict into SECOND-KNOWLEDGE-BRAIN.md append format."""
    title = article.get("title", "Unknown Title")
    authors = article.get("authors", "Unknown Authors")
    year = article.get("year", "")
    journal = article.get("journal", "")
    doi = article.get("doi", "")
    url = article.get("url", "")
    evidence_level = article.get("evidence_level", classify_evidence_level(title, journal))
    relevance = article.get("relevance", infer_relevance(title, query))

    doi_or_url = f"10.{doi.split('10.')[-1]}" if doi and "10." in doi else url
    link_display = f"https://doi.org/{doi}" if doi else url

    return (
        f"\n### {title}\n"
        f"- **Source**: {journal}\n"
        f"- **Authors**: {authors}\n"
        f"- **Year**: {year}\n"
        f"- **DOI/URL**: {link_display}\n"
        f"- **Evidence Level**: {evidence_level}\n"
        f"- **Key Finding**: [Auto-fetched — review and annotate manually for accuracy]\n"
        f"- **Relevance**: {relevance}\n"
    )


def format_update_header(date_str: str, source: str, count: int) -> str:
    return f"\n## Update: {date_str} — {source} ({count} new entries)\n"


# ── Dedup + Append ────────────────────────────────────────────────────────────

def append_to_brain(brain_path: Path, entries: list[str], header: str, dry_run: bool = False) -> int:
    """Append new entries to SECOND-KNOWLEDGE-BRAIN.md. Returns count appended."""
    if not entries:
        return 0
    content = header + "".join(entries)
    if dry_run:
        print(f"[DRY RUN] Would append {len(entries)} entries:\n{content[:500]}...")
        return len(entries)
    with brain_path.open("a", encoding="utf-8") as f:
        f.write("\n" + content)
    return len(entries)


# ── Main Pipeline ─────────────────────────────────────────────────────────────

def run(max_results: int = MAX_RESULTS_PER_QUERY, dry_run: bool = False) -> None:
    today = datetime.now().strftime("%Y-%m-%d")
    min_date = (datetime.now() - timedelta(days=MAX_AGE_DAYS)).strftime("%Y/%m/%d")

    print(f"[knowledge_updater] Starting run — {today}")
    print(f"[knowledge_updater] Brain path: {BRAIN_PATH}")

    existing_hashes = load_existing_hashes(BRAIN_PATH)
    print(f"[knowledge_updater] Found {len(existing_hashes)} existing entries (by hash)")

    total_appended = 0

    # ── Phase 1: PubMed ───────────────────────────────────────────────────
    print("\n[PubMed] Searching...")
    pubmed_new_entries = []
    seen_this_run = set()

    for query in PUBMED_QUERIES:
        pmids = pubmed_search(query, max_results, min_date)
        time.sleep(DELAY_BETWEEN_REQUESTS)
        if not pmids:
            continue
        articles = pubmed_fetch(pmids)
        time.sleep(DELAY_BETWEEN_REQUESTS)
        for art in articles:
            identifier = art.get("doi") or art.get("url", "")
            h = url_hash(identifier)
            if h in existing_hashes or h in seen_this_run:
                continue
            seen_this_run.add(h)
            pubmed_new_entries.append(format_entry(art, query))
            print(f"  [NEW] {art['year']} — {art['title'][:80]}")

    if pubmed_new_entries:
        header = format_update_header(today, "PubMed", len(pubmed_new_entries))
        appended = append_to_brain(BRAIN_PATH, pubmed_new_entries, header, dry_run)
        total_appended += appended
        print(f"[PubMed] Appended {appended} new entries.")
    else:
        print("[PubMed] No new entries found.")

    # ── Phase 2: NICE Guidelines ──────────────────────────────────────────
    print("\n[NICE] Fetching guideline pages...")
    nice_new_entries = []

    for url in NICE_URLS:
        art = fetch_nice_guideline(url)
        time.sleep(DELAY_BETWEEN_REQUESTS)
        if not art:
            continue
        h = url_hash(url)
        if h in existing_hashes or h in seen_this_run:
            print(f"  [SKIP] Already present: {url}")
            continue
        seen_this_run.add(h)
        art["evidence_level"] = "Clinical Guideline (NICE)"
        art["relevance"] = f"NICE official guideline — clinical recommendations for {url.split('/')[-1].upper()}"
        nice_new_entries.append(format_entry(art))
        print(f"  [NEW] NICE {url.split('/')[-1].upper()}: {art['title'][:80]}")

    if nice_new_entries:
        header = format_update_header(today, "NICE Guidelines", len(nice_new_entries))
        appended = append_to_brain(BRAIN_PATH, nice_new_entries, header, dry_run)
        total_appended += appended
        print(f"[NICE] Appended {appended} new entries.")
    else:
        print("[NICE] No new entries found.")

    # ── Summary ───────────────────────────────────────────────────────────
    print(f"\n[knowledge_updater] Run complete — {total_appended} total new entries appended.")
    if dry_run:
        print("[knowledge_updater] DRY RUN — no files were modified.")


# ── CLI Entry Point ───────────────────────────────────────────────────────────

if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description="Update SECOND-KNOWLEDGE-BRAIN.md with latest mental health clinical evidence."
    )
    parser.add_argument(
        "--dry-run",
        action="store_true",
        help="Preview entries without writing to disk",
    )
    parser.add_argument(
        "--max-results",
        type=int,
        default=MAX_RESULTS_PER_QUERY,
        help=f"Max PubMed results per query (default: {MAX_RESULTS_PER_QUERY})",
    )
    args = parser.parse_args()
    run(max_results=args.max_results, dry_run=args.dry_run)
