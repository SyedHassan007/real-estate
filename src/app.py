import streamlit as st
import pandas as pd
import plotly.express as px
from kpis import calculate_business_kpis, calculate_customer_kpis

st.set_page_config(page_title="Real Estate Analytics", layout="wide", initial_sidebar_state="expanded")
st.title("🏠 Real Estate Analytics Dashboard")
st.markdown("### An interactive tool for analyzing the housing market for investors and buyers.")

@st.cache_data
def load_data():
    try:
        df = pd.read_csv("data/processed/real_estate_processed_data.csv", parse_dates=['date'])
        return df
    except FileNotFoundError:
        st.error("Processed data file not found. Please run the ETL script first.")
        return pd.DataFrame()

df_raw = load_data()

if not df_raw.empty:
    tab1, tab2 = st.tabs(["📊 Business Insights", "🫂 Customer Insights"])

    with tab1:
        st.header("Business Insights")
        biz_kpis = calculate_business_kpis(df_raw)
        c1, c2, c3 = st.columns(3)
        c1.metric("Avg. Price per Sqft", f"${biz_kpis['avg_price_per_sqft']:.2f}")
        c2.metric("Avg. Rental Yield", f"{biz_kpis['avg_rental_yield']:.2f}%")
        c3.metric("Avg. Days on Market", f"{biz_kpis['avg_days_on_market']:.0f} days")

        st.subheader("Monthly Transaction Volume")
        st.plotly_chart(px.line(biz_kpis['monthly_transactions'], x='date', y='transaction_volume',
                                title='Monthly Property Transaction Volume'), use_container_width=True)

        st.subheader("Total Revenue by Property Type")
        st.plotly_chart(px.bar(biz_kpis['revenue_by_type'], x='property_type', y='total_revenue',
                               title='Total Revenue by Property Type'), use_container_width=True)

    with tab2:
        st.header("Customer Insights")
        customer_kpis = calculate_customer_kpis(df_raw)
        c1, c2, c3 = st.columns(3)
        c1.metric("Affordability Index", f"{customer_kpis['affordability_index']:.2f}")
        c2.metric("Mortgage Burden", f"{customer_kpis['mortgage_burden']:.0f}%")
        c3.metric("Avg. Cost of Living", f"${customer_kpis['cost_by_neighborhood']['cost_of_living'].mean():.2f}/month")

        st.subheader("Top Neighborhoods by Score")
        st.plotly_chart(px.bar(customer_kpis['top_neighborhoods'], x='neighborhood', y='neighborhood_score',
                               title='Top Neighborhoods by Score'), use_container_width=True)

        st.subheader("Best Time to Buy/Rent (Monthly Trends)")
        st.plotly_chart(px.line(customer_kpis['monthly_trends'], x='month', y=['avg_price', 'avg_rent'],
                                title='Monthly Price & Rent Trends'), use_container_width=True)
