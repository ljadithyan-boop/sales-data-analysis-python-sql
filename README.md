# 🛒 BehindTheCart — Retail Sales Analysis Pipeline

![Python](https://img.shields.io/badge/Python-3776AB?style=flat&logo=python&logoColor=white)
![Pandas](https://img.shields.io/badge/Pandas-150458?style=flat&logo=pandas&logoColor=white)
![SQLite](https://img.shields.io/badge/SQLite-003B57?style=flat&logo=sqlite&logoColor=white)
![Power BI](https://img.shields.io/badge/Power%20BI-F2C811?style=flat&logo=powerbi&logoColor=black)
![Excel](https://img.shields.io/badge/Excel-217346?style=flat&logo=microsoftexcel&logoColor=white)

> A complete end-to-end retail sales analysis pipeline — from raw Excel data to an interactive Power BI dashboard — built on 10,000+ rows of superstore sales data.

---

## 📌 Project Overview

**BehindTheCart** is a final-year BCA data analytics project that simulates a real-world retail data pipeline. It covers every stage of the analytics workflow: data ingestion, cleaning, SQL querying, exploratory analysis, and visual reporting.

---

## 🗂️ Project Structure
sales-data-analysis-python-sql/
│
├── data/
│   ├── superstore_raw.xlsx        # Original raw dataset
│   └── superstore_cleaned.csv     # Cleaned & processed data
│
├── database/
│   └── sales_database.db          # SQLite database
│
├── scripts/
│   ├── 01_data_cleaning.py        # Data cleaning with Pandas
│   ├── 01_sales_schema.sql        # SQL schema & queries
│   └── 02_eda_analysis.py         # Exploratory data analysis
│
├── visuals/
│   └── BehindTheCart_v3_Final.pptx  # Project presentation deck
│
├── dashboard/
│   └── BehindTheCart_Dashboard.pbix # Power BI dashboard
│
└── README.md
---

## 🔄 Pipeline Stages

### Stage 1 — Data Ingestion & Cleaning
- Raw data loaded from `superstore_raw.xlsx` using **Pandas**
- Handled missing values, duplicates, and data type corrections
- Standardised column names and date formats
- Output: `superstore_cleaned.csv`

### Stage 2 — SQL Database
- Designed schema and created tables using **SQLite**
- Loaded cleaned CSV into the database
- Wrote SQL queries for aggregations, filtering, and joins
- Output: `sales_database.db`

### Stage 3 — Exploratory Data Analysis
- Analysed sales trends, category performance, and regional insights
- Generated charts and statistical summaries using **Matplotlib/Seaborn**
- Output: `sales_charts.png`

### Stage 4 — Power BI Dashboard
- Connected Power BI to the cleaned dataset
- Built interactive visuals with slicers for date, region, and category
- KPIs tracked: Revenue, Profit, Orders, Margin %
- Output: `BehindTheCart_Dashboard.pbix`

---

## 📊 Key Insights
- 📈 Sales peak in **Q4** every year (Nov–Dec)
- 🖥️ **Technology** is the highest revenue category
- 🌍 **West region** leads in total sales volume
- 📉 **Furniture** has the lowest profit margins despite high sales

---

## 🛠️ Tools & Technologies

| Tool | Purpose |
|------|---------|
| Python (Pandas) | Data cleaning & EDA |
| SQLite | Database storage & querying |
| Power BI Desktop | Interactive dashboard |
| Microsoft Excel | Raw data source |
| Matplotlib / Seaborn | EDA visualisations |

---

## 🚀 How to Run

1. Clone the repo
```bash
   git clone https://github.com/ljadithyan-boop/sales-data-analysis-python-sql.git
```
2. Install dependencies
```bash
   pip install pandas matplotlib seaborn
```
3. Run data cleaning
```bash
   python scripts/01_data_cleaning.py
```
4. Run EDA
```bash
   python scripts/02_eda_analysis.py
```
5. Open `dashboard/BehindTheCart_Dashboard.pbix` in Power BI Desktop

---

## 👤 Author

**Adithyan LJ** — Final Year BCA Student, Data Analytics  
📍 Bengaluru | [LinkedIn](https://linkedin.com/in/your-profile) | [GitHub](https://github.com/ljadithyan-boop)
