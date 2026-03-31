import os
import pandas as pd
import numpy as np
import random
from datetime import date, timedelta

def project_root():
    return os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))

def generate_real_estate_data(num_records=10000, start_date=date(2024, 1, 1), end_date=date(2024, 12, 31)):
    """Generates synthetic real estate data."""
    cities = ['New York', 'Los Angeles', 'Chicago', 'Houston', 'Phoenix']
    neighborhoods = {
        'New York': ['Manhattan', 'Brooklyn', 'Queens'],
        'Los Angeles': ['Beverly Hills', 'Hollywood', 'Santa Monica'],
        'Chicago': ['Lincoln Park', 'River North', 'Wicker Park'],
        'Houston': ['The Heights', 'Downtown', 'River Oaks'],
        'Phoenix': ['Scottsdale', 'Tempe', 'Mesa']
    }
    property_types = ['Single Family', 'Condo', 'Townhouse', 'Apartment']

    data = []
    span_days = (end_date - start_date).days
    for _ in range(num_records):
        record_date = start_date + timedelta(days=random.randint(0, span_days))
        city = random.choice(cities)
        neighborhood = random.choice(neighborhoods[city])
        prop_type = random.choice(property_types)

        if city in ['New York', 'Los Angeles']:
            price_base = random.uniform(500000, 2000000)
            sqft_base = random.uniform(800, 3000)
        else:
            price_base = random.uniform(200000, 800000)
            sqft_base = random.uniform(1200, 4000)

        price = price_base * np.random.uniform(0.9, 1.1)
        size_sqft = sqft_base * np.random.uniform(0.95, 1.05)
        rent = price * np.random.uniform(0.003, 0.006)  # monthly rent
        occupancy = 1 if np.random.random() < 0.9 else 0
        days_on_market = np.random.randint(15, 200)
        rating = np.random.uniform(3.0, 5.0)
        amenities_score = np.random.uniform(1.0, 10.0)
        buyer_income = np.random.uniform(50000, 250000)

        data.append([record_date, city, neighborhood, prop_type, price, size_sqft,
                     rent, occupancy, days_on_market, rating, amenities_score, buyer_income])

    df = pd.DataFrame(data, columns=[
        'date','city','neighborhood','property_type','price','size_sqft',
        'rent','occupancy','days_on_market','rating','amenities_score','buyer_income'
    ])
    return df

if __name__ == '__main__':
    root = project_root()
    raw_path = os.path.join(root, 'data', 'raw', 'real_estate_raw_data.csv')
    os.makedirs(os.path.dirname(raw_path), exist_ok=True)
    df = generate_real_estate_data()
    df.to_csv(raw_path, index=False)
    print(f"Synthetic data generated and saved to {raw_path}")
