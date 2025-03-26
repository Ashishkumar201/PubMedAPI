import argparse
from pubmed.fetcher import fetch_papers
from pubmed.processor import process_papers
from pubmed.writer import save_to_csv

def main():
    parser = argparse.ArgumentParser(description="Fetch research papers from PubMed.")
    parser.add_argument("query", type=str, help="Search query for PubMed")
    parser.add_argument("-f", "--file", type=str, help="Output CSV filename", default=None)
    parser.add_argument("-d", "--debug", action="store_true", help="Enable debug mode")
    args = parser.parse_args()

    if args.debug:
        print(f"Fetching papers with query: {args.query}")

    papers = fetch_papers(args.query, debug=args.debug)
    processed_data = process_papers(papers, debug=args.debug)

    if args.file:
        save_to_csv(processed_data, args.file)
        print(f"Results saved to {args.file}")
    else:
        print("Results:")
        for paper in processed_data:
            print(paper)

if __name__ == "__main__":
    main()
