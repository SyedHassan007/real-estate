import pandas as pd

def calculate_business_kpis(df):
    if df.empty:
        return {}
    avg_price_per_sqft = df['price_per_sqft'].mean()
    df = df.copy()
    df['rental_yield'] = (df['annual_rent'] / df['price']) * 100
    avg_rental_yield = df['rental_yield'].mean()
    occupancy_rate = (df['occupancy'].sum() / len(df)) * 100
    avg_days_on_market = df['days_on_market'].mean()
    monthly_transactions = df.groupby(pd.Grouper(key='date', freq='M')).size().reset_index(name='transaction_volume')
    revenue_by_type = df.groupby('property_type')['price'].sum().reset_index(name='total_revenue')
    property_value_growth = 5.0  # simulated
    return {
        'avg_price_per_sqft': avg_price_per_sqft,
        'avg_rental_yield': avg_rental_yield,
        'occupancy_rate': occupancy_rate,
        'avg_days_on_market': avg_days_on_market,
        'monthly_transactions': monthly_transactions,
        'revenue_by_type': revenue_by_type,
        'property_value_growth': property_value_growth
    }

def calculate_customer_kpis(df):
    if df.empty:
        return {}
    df = df.copy()
    affordability_index = df['price'].mean() / df['buyer_income'].mean()
    df['cost_of_living'] = df['rent'] * 1.5
    cost_by_neighborhood = df.groupby('neighborhood')['cost_of_living'].mean().reset_index()
    df['neighborhood_score'] = (df['rating'] * 0.6) + (df['amenities_score'] * 0.4)
    top_neighborhoods = df.groupby('neighborhood')['neighborhood_score'].mean().sort_values(ascending=False).reset_index()
    mortgage_burden = 28.0
    monthly_trends = df.groupby(df['date'].dt.month).agg(avg_price=('price', 'mean'),
                                                         avg_rent=('rent', 'mean')).reset_index()
    monthly_trends['month'] = monthly_trends['date'].apply(lambda m: pd.to_datetime(str(m), format='%m').month_name())
    return {
        'affordability_index': affordability_index,
        'cost_by_neighborhood': cost_by_neighborhood,
        'top_neighborhoods': top_neighborhoods,
        'mortgage_burden': mortgage_burden,
        'monthly_trends': monthly_trends
    }
