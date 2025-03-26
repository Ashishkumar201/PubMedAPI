import requests
import xml.etree.ElementTree as ET
import re

BASE_URL = "https://eutils.ncbi.nlm.nih.gov/entrez/eutils"

def fetch_paper_details(pmid: str):
    """Fetch details of a PubMed paper and parse XML response."""
    fetch_url = f"{BASE_URL}/efetch.fcgi"
    params = {"db": "pubmed", "id": pmid, "retmode": "xml"}  # XML format

    response = requests.get(fetch_url, params=params)
    response.raise_for_status()

    try:
        root = ET.fromstring(response.text)  # Parse XML

        # Extract Title
        title = root.find(".//ArticleTitle").text if root.find(".//ArticleTitle") is not None else "N/A"

        # Extract Publication Date
        pub_date = root.find(".//PubDate/Year")
        publication_date = pub_date.text if pub_date is not None else "N/A"

        # Extract Authors & Affiliations
        authors = []
        affiliations = []
        corresponding_email = "N/A"

        for author in root.findall(".//Author"):
            last_name = author.find("LastName")
            first_name = author.find("ForeName")
            full_name = f"{first_name.text} {last_name.text}" if first_name is not None and last_name is not None else "N/A"

            affiliation = author.find(".//AffiliationInfo/Affiliation")
            affiliation_text = affiliation.text if affiliation is not None else "N/A"

            if full_name != "N/A":
                authors.append(full_name)
                affiliations.append(affiliation_text)

            # Check for Corresponding Author Email
            email_match = re.search(r"[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}", affiliation_text)
            if email_match:
                corresponding_email = email_match.group()

        # Identify Non-Academic Authors & Company Affiliations
        non_academic_authors = []
        company_affiliations = []

        for author, aff in zip(authors, affiliations):
            if aff and not any(keyword in aff.lower() for keyword in ["university", "college", "institute"]):
                non_academic_authors.append(author)
                company_affiliations.append(aff)

        return {
            "PubmedID": pmid,
            "Title": title,
            "Publication Date": publication_date,
            "Non-academic Authors": ", ".join(non_academic_authors) or "N/A",
            "Company Affiliations": ", ".join(company_affiliations) or "N/A",
            "Corresponding Author Email": corresponding_email,
        }

    except Exception as e:
        print(f"ERROR: Failed to parse XML for PMID {pmid}: {e}")
        return {}



def process_papers(pmids, debug=False):
    """Extract required fields and filter authors from non-academic institutions."""
    processed_data = []

    for pmid in pmids:
        paper_details = fetch_paper_details(pmid)

        if not paper_details:
            print(f"WARNING: Skipping PMID {pmid} due to missing data")
            continue  # Skip invalid papers

        processed_data.append(paper_details)

        if debug:
            print(f"Processed paper {pmid}: {paper_details['Title']}")

    return processed_data
