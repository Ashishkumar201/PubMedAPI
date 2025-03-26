import pandas as pd

def save_to_csv(data, filename):
    """Save extracted data to a CSV file."""
    df = pd.DataFrame(data)
    df.to_csv(filename, index=False)
    print(f"Saved {len(data)} records to {filename}")
