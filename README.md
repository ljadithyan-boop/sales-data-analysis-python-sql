# 🐍 Sales Data Analysis — Python & SQL

> A full data analysis pipeline on a 10,000+ row e-commerce dataset using Python (Pandas), MySQL, and Power BI — covering data cleaning, EDA, SQL querying, and visualization.

---

## 🔍 Project Overview

This project simulates a real-world data analyst workflow: raw data comes in, gets cleaned and explored in Python, queried deeply with SQL, and finally visualized in Power BI. Each stage mirrors what an analyst does on the job.

---

## 🛠️ Tools & Technologies

| Tool | Usage |
|------|-------|
| Python (Pandas, NumPy) | Data loading, cleaning, EDA |
| MySQL | Advanced querying and aggregation |
| DB Browser for SQLite | Local database management |
| Power BI | Final visualization layer |
| Superstore Dataset | Source data (10,000+ rows) |

---

## 📌 Key Highlights

- **Cleaned a 10,000+ row dataset** — handled nulls, duplicates, and date parsing
- **5-dimension EDA** — category sales, top products, monthly trends, regional profit, customer segments
- **10+ Advanced SQL Queries** — JOINs, GROUP BY, subqueries, CTEs, and window functions
- **End-to-end pipeline** — raw CSV → cleaned data → SQL analysis → Power BI output

---

## 📂 Project Structure

```
├── data/
│   ├── superstore_raw.csv          # Original dataset
│   └── superstore_cleaned.csv      # Cleaned output from Python
│
├── python/
│   ├── 01_data_cleaning.py         # Null handling, deduplication, date parsing
│   └── 02_eda_analysis.py          # Exploratory data analysis + charts
│
├── sql/
│   ├── 01_basic_queries.sql        # SELECT, WHERE, ORDER BY
│   ├── 02_aggregations.sql         # GROUP BY, HAVING, COUNT, SUM
│   ├── 03_joins_subqueries.sql     # JOINs and nested queries
│   └── 04_cte_advanced.sql         # CTEs and multi-step analysis
│
├── dashboard/
│   └── Sales_Analysis.pbix         # Power BI file using cleaned data
│
└── README.md
```

---

## 🔬 Analysis Breakdown

### Stage 1 — Data Cleaning (Python)
- Loaded CSV using `pd.read_csv()`
- Identified and filled null values in key columns
- Removed 150+ duplicate records
- Parsed `Order Date` and `Ship Date` into proper datetime format
- Exported cleaned file for SQL and Power BI use

### Stage 2 — Exploratory Data Analysis (Python)
- Sales by Category and Sub-Category
- Top 10 products by total revenue
- Monthly sales trend (2018–2021)
- Regional profit comparison
- Customer segment contribution to revenue

### Stage 3 — SQL Analysis (MySQL)
- Total revenue and profit by region using `GROUP BY`
- Top customers by order value using `ORDER BY + LIMIT`
- Month-over-month sales using date functions
- Category profit ranking using CTEs
- Multi-table JOINs to combine order and customer data

### Stage 4 — Visualization (Power BI)
- Imported cleaned CSV into Power BI
- Built visual layer on top of the Python-SQL pipeline
- Reused DAX measures from the Sales Dashboard project

---

## 💡 Sample SQL Query

```sql
-- Top 5 regions by profit margin using CTE
WITH region_summary AS (
    SELECT 
        Region,
        SUM(Sales)  AS total_sales,
        SUM(Profit) AS total_profit
    FROM superstore
    GROUP BY Region
)
SELECT 
    Region,
    total_sales,
    total_profit,
    ROUND((total_profit / total_sales) * 100, 2) AS profit_margin_pct
FROM region_summary
ORDER BY profit_margin_pct DESC
LIMIT 5;
```

---

## 💡 What I Learned

- Building a multi-stage data pipeline from scratch
- Writing production-style SQL for business reporting
- Combining Python EDA output with SQL for deeper analysis
- Structuring a data project so others can read and reuse it

---

## 📬 Connect

**Adithyan L J**  
📧 ljadithyan@gmail.com  
🔗 [LinkedIn](https://www.linkedin.com/in/adithyan-lj-378181332)  
💻 [GitHub](https://github.com/adithyanlj)

---

> *Built as part of my Data Analyst portfolio — BCA Final Year, IZEE Business School, Bengaluru*
