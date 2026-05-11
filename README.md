# 🛒 Behind the Cart — RetailSales Analytics Dashboard

![Python](https://img.shields.io/badge/Python-3.x-3776AB?style=flat&logo=python&logoColor=white)
![Pandas](https://img.shields.io/badge/Pandas-Data%20Analysis-150458?style=flat&logo=pandas&logoColor=white)
![SQLite](https://img.shields.io/badge/SQLite-Database-003B57?style=flat&logo=sqlite&logoColor=white)
![Power BI](https://img.shields.io/badge/Power%20BI-Dashboard-F2C811?style=flat&logo=powerbi&logoColor=black)
![Status](https://img.shields.io/badge/Status-Completed-2ea44f?style=flat)

> End-to-end retail sales analytics pipeline — from raw Excel data to an interactive Power BI dashboard — built as a BCA Final Year Project at IZEE Business School, Bengaluru (2026).

---

## 📌 Project Overview

Most retail businesses collect thousands of transactions but fail to analyse them effectively. **Behind the Cart** bridges that gap by building a complete data analytics pipeline that transforms raw sales data into actionable business intelligence.

**Dataset:** 500 retail transactions across 4 categories, 4 regions, and 6 salespersons — FY 2024.

---

## 🔧 Tech Stack

| Tool | Purpose |
|------|---------|
| Microsoft Excel | Raw data source |
| Python 3 + pandas | Data cleaning, transformation, EDA |
| matplotlib | Chart generation |
| SQLite | Relational database storage |
| SQL (12 queries) | Business analysis queries |
| Microsoft Power BI | Interactive dashboard |

---

## 🗂️ Project Structure

```
sales-data-analysis-python-sql/
│
├── 📁 data/
│   ├── superstore_raw..xlsx          # Raw dataset (500 rows × 11 columns)
│   └── superstore_cleaned.csv        # Cleaned data exported for Power BI
│
├── 📁 scripts/
│   ├── 01_data_cleaning.py           # Data ingestion, cleaning & SQLite export
│   ├── 02_eda_analysis.py            # EDA, groupby analysis & chart generation
│   └── 01_sales_schema..sql          # 12 SQL queries for business analysis
│
├── 📁 database/
│   └── sales_database.db             # SQLite database (open in DB Browser)
│
├── 📁 dashboard/
│   └── Sales_Dashboard.pbix          # Power BI dashboard file
│
├── 📁 visuals/
│   ├── BehindTheCart_v3_Final.pptx   # Final presentation deck (15 slides)
│   └── sales_charts.png              # 4 matplotlib charts (PNG export)
│
└── README.md
```

---

## ⚙️ How to Run

### 1. Clone the repo
```bash
git clone https://github.com/ljadithyan-boop/sales-data-analysis-python-sql.git
cd sales-data-analysis-python-sql
```

### 2. Install dependencies
```bash
pip install pandas matplotlib openpyxl
```

### 3. Run the pipeline
```bash
# Step 1 — Clean data and load into SQLite
python scripts/01_data_cleaning.py

# Step 2 — Run EDA and generate charts
python scripts/02_eda_analysis.py
```

### 4. Explore the database
Open `database/sales_database.db` in [DB Browser for SQLite](https://sqlitebrowser.org/) and run the queries from `scripts/01_sales_schema..sql`.

### 5. Open the dashboard
Open `dashboard/Sales_Dashboard.pbix` in Power BI Desktop.

---

## 📊 Key Findings

| Metric | Value |
|--------|-------|
| Total Revenue | ₹10,017K |
| Total Orders | 500 |
| Avg Order Value | ₹20,034 |
| Top Salesperson | Priya (₹2,071K) |
| Top Category | Electronics (82.3% revenue share) |
| Top Region | North (33.5% revenue share) |

### Insights
- **Electronics dominates** with 82% of revenue — driven by high unit-price products like laptops and phones
- **North region leads** with 33.5% share; West lags at 18.9% — a clear growth opportunity
- **Q4 recovery** — Nov–Dec surge signals seasonal demand peaks worth planning inventory around
- **Balanced sales team** — all 6 reps within ₹850K of each other; coaching bottom 2 can close the gap
- **Grocery gap** — only ₹63K revenue; SKU relevance needs urgent review

---

## 🗃️ SQL Queries Covered

- Total revenue, orders, avg order value
- Revenue by category, region, salesperson
- Monthly revenue trend
- Top 5 best-selling products
- Discount impact analysis
- Customer lifetime value
- Revenue contribution % per category
- Created a reusable `VIEW` for monthly category sales

---

## 📁 Deliverables

- ✅ `01_data_cleaning.py` — automated cleaning pipeline
- ✅ `02_eda_analysis.py` — full exploratory analysis
- ✅ `01_sales_schema..sql` — 12 business SQL queries
- ✅ `sales_database.db` — structured SQLite database
- ✅ `Sales_Dashboard.pbix` — interactive Power BI dashboard
- ✅ `BehindTheCart_v3_Final.pptx` — 15-slide presentation deck

---

## ⚠️ Limitations

- Dataset is **synthetic** (simulated, not from a live retail system)
- **No real-time data** — static FY 2024 snapshot only
- **No predictive model** — descriptive and diagnostic analysis only
- **No profitability data** — revenue tracked, not cost or margin

---

## 👤 Author

**Adithyan L J**
BCA Final Year · Data Analytics · IZEE Business School, Bengaluru (2023–2026)

[![LinkedIn](https://img.shields.io/badge/LinkedIn-Connect-0A66C2?style=flat&logo=linkedin)](https://linkedin.com/in/adithyan-lj-378181332)
[![Email](https://img.shields.io/badge/Email-ljadithyan%40gmail.com-EA4335?style=flat&logo=gmail)](mailto:ljadithyan@gmail.com)

---

*Built with Python, SQL, and Power BI as part of BCA Final Year Project — 2026*
