import requests

BASE_URL = "https://eutils.ncbi.nlm.nih.gov/entrez/eutils"

def fetch_papers(query: str, max_results: int = 10, debug: bool = False):
    """Fetch PubMed papers based on a search query with full syntax support."""
    search_url = f"{BASE_URL}/esearch.fcgi"
    params = {
        "db": "pubmed",
        "term": query,  # Supports full query syntax
        "retmax": max_results,
        "retmode": "json"
    }

    response = requests.get(search_url, params=params)
    response.raise_for_status()
    data = response.json()

    pmids = data["esearchresult"].get("idlist", [])
    
    if debug:
        print(f"Found {len(pmids)} paper(s): {pmids}")

    return pmids
    