import os
import pandas as pd

def project_root():
    return os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))

def run_etl():
    """Basic ETL for real estate dataset."""
    root = project_root()
    raw_path = os.path.join(root, 'data', 'raw', 'real_estate_raw_data.csv')
    processed_path = os.path.join(root, 'data', 'processed', 'real_estate_processed_data.csv')
    try:
        df = pd.read_csv(raw_path)
        df['date'] = pd.to_datetime(df['date'])
        df.drop_duplicates(inplace=True)
        df['price_per_sqft'] = df['price'] / df['size_sqft']
        df['annual_rent'] = df['rent'] * 12
        os.makedirs(os.path.dirname(processed_path), exist_ok=True)
        df.to_csv(processed_path, index=False)
        print(f"ETL process completed. Data saved to {processed_path}")
        return df
    except FileNotFoundError:
        print("Error: Raw data file not found. Please run data_generator.py first.")
        return None

if __name__ == '__main__':
    run_etl()
