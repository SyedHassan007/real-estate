# 🏡 real-estate-kpis

### End-to-End Data Analytics Project on the Real Estate Sector

Welcome to the **real-estate** repository!  
This is a portfolio-ready project showcasing how to build an **end-to-end data analytics solution** for the **real estate industry**, targeted at both **business stakeholders** (investors, developers, agencies) and **customers** (homebuyers, renters).  

---

## 💡 Project Overview

The real estate market is complex, with multiple stakeholders making decisions based on price, rent, occupancy, affordability, and timing.  
This project demonstrates how data can simplify those decisions by transforming raw housing data into **actionable KPIs**.  

Key highlights:
- **Python ETL Pipeline** → generate synthetic housing data, clean it, and engineer KPIs.
- **Streamlit Web App** → interactive dashboards with insights for **businesses** and **customers**.
- **Power BI Dashboard** → professional visualizations for deeper reporting.
- **Excel Summary** → pivot tables with KPI breakdowns for quick reviews.
- **Deployment** → Streamlit app hosted on **DuckDNS** for public demo.

---

## 💾 Data & Sources

Due to the proprietary nature of real estate data, this project uses a **realistic synthetic dataset** generated with Python (`src/data_generator.py`).  
It includes:

- **Property Metrics:** price, size, rent, days on market.  
- **Location Data:** city, neighborhood, property type.  
- **Customer Demographics:** buyer income.  
- **Quality Metrics:** ratings, amenities score.  

---

## 📊 Key Performance Indicators (KPIs)

### Business KPIs (for investors & agencies)
| KPI | Formula | Description |
|---|---|---|
| **Avg. Price per Sqft** | mean(`price` / `size_sqft`) | Market value benchmark. |
| **Rental Yield** | (`annual_rent` / `price`) * 100 | ROI on rental property. |
| **Occupancy Rate** | % of properties rented | Market demand signal. |
| **Avg. Days on Market** | mean(`days_on_market`) | Liquidity of housing market. |
| **Transaction Volume** | count per month | Activity level of property sales. |
| **Revenue by Type** | sum(`price`) by property_type | Which property types drive revenue. |
| **Property Value Growth** | simulated 5% YoY | Long-term appreciation trend. |

### Customer KPIs (for buyers & renters)
| KPI | Formula | Description |
|---|---|---|
| **Affordability Index** | avg(`price`) / avg(`buyer_income`) | Lower = more affordable. |
| **Cost of Living** | rent + 50% (utilities) | Average monthly expenses. |
| **Top Neighborhoods** | weighted avg(rating, amenities) | Lifestyle + quality score. |
| **Mortgage Burden** | simulated 28% | Standard share of income to housing. |
| **Best Time to Buy/Rent** | monthly avg price/rent | Identifies seasonal trends. |

---

## 🚀 Getting Started

Clone the repository and set up locally:

```bash
# Clone repo
git clone https://github.com/YourUsername/real-estate-kpis.git
cd Real-Estate

# Create virtual environment
python -m venv venv
.\venv\Scripts\activate # On Linux source venv/bin/activate

# Install dependencies
pip install -r requirements.txt

# Generate synthetic dataset
python src/data_generator.py

# Run ETL pipeline
python src/etl.py

# Launch Streamlit app
streamlit run src/app.py
```

---

## 📂 Repository Structure
* `real-estate-kpis/`
* `├─ data/                     # raw + processed datasets`
* `│  ├─ raw/`
* `│  └─ processed/`
* `├─ notebooks/                # Jupyter notebooks`
* `│  ├─ 01_data_collection.ipynb`
* `│  ├─ 02_data_cleaning_eda.ipynb`
* `│  ├─ 03_kpi_engineering.ipynb`
* `│  └─ 04_visualizations.ipynb`
* `├─ src/                      # Core scripts`
* `│  ├─ data_generator.py      # Synthetic dataset generator`
* `│  ├─ etl.py                 # ETL pipeline`
* `│  ├─ kpis.py                # KPI calculations`
* `│  └─ app.py                 # Streamlit app`
* `├─ powerbi/                  # Power BI dashboard (.pbix)`
* `├─ excel/                    # Excel KPI summary`
* `├─ tests/                    # Unit tests for KPIs`
* `├─ README.md`
* `├─ requirements.txt`
* `├─ LICENSE`
* `└─ .gitignore`


---

## 🖼️ Sample Visuals

- **Monthly Transaction Volume:** 📈 A line chart showing property sales activity across the year.  
- **Top Neighborhoods by Score:** 🏘️ A bar chart ranking the most attractive neighborhoods.  

---

### 📌 Deliverables

* **Streamlit App**
* **Power BI Dashboard**
* **Excel Summary**

---

### 🤝 Contribution

This project is open-source and portfolio-focused.
Feel free to fork, raise issues, or submit PRs to improve.

---

### 📧 Contact

* **Name:** Syed Allahdad Hassan
* **LinkedIn:** [LinkedIn](https://www.linkedin.com/in/syed-hassan-7b610829a/)
* **GitHub:** [GitHub](https://github.com/SyedHassan007/)