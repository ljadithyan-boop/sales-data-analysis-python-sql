-- ============================================================
--  RetailSales Analytics Project
--  SQL Script  |  Beginner-Friendly with Comments
--  Tool: SQLite (works in DB Browser for SQLite — free & easy)
-- ============================================================


-- ──────────────────────────────────────────────────────────────
-- STEP 1: CREATE THE TABLE
-- ──────────────────────────────────────────────────────────────

CREATE TABLE IF NOT EXISTS sales (
    order_id      TEXT PRIMARY KEY,   -- Unique order identifier
    order_date    TEXT,               -- Date as YYYY-MM-DD text
    customer      TEXT,               -- Customer / store name
    region        TEXT,               -- North / South / East / West
    category      TEXT,               -- Product category
    product       TEXT,               -- Product name
    quantity      INTEGER,            -- Units sold
    unit_price    REAL,               -- Price per unit
    discount_pct  INTEGER,            -- Discount percentage (0, 5, 10, 15, 20)
    total_sales   REAL,               -- Final sale value after discount
    salesperson   TEXT                -- Employee name
);


-- ──────────────────────────────────────────────────────────────
-- STEP 2: CHECK YOUR DATA (always do this first!)
-- ──────────────────────────────────────────────────────────────

-- See all records
SELECT * FROM sales LIMIT 10;

-- Count total records
SELECT COUNT(*) AS total_orders FROM sales;

-- Check date range
SELECT MIN(order_date) AS first_sale,
       MAX(order_date) AS last_sale
FROM sales;


-- ──────────────────────────────────────────────────────────────
-- STEP 3: BASIC ANALYSIS QUERIES
-- ──────────────────────────────────────────────────────────────

-- Q1: Total Revenue
SELECT ROUND(SUM(total_sales), 2) AS total_revenue
FROM sales;


-- Q2: Revenue by Region
SELECT   region,
         COUNT(*)                         AS total_orders,
         ROUND(SUM(total_sales), 2)       AS total_revenue,
         ROUND(AVG(total_sales), 2)       AS avg_order_value
FROM     sales
GROUP BY region
ORDER BY total_revenue DESC;


-- Q3: Revenue by Category
SELECT   category,
         COUNT(*)                   AS total_orders,
         ROUND(SUM(total_sales), 2) AS total_revenue,
         ROUND(AVG(unit_price), 2)  AS avg_unit_price
FROM     sales
GROUP BY category
ORDER BY total_revenue DESC;


-- Q4: Top 5 Best-Selling Products (by revenue)
SELECT   product,
         category,
         SUM(quantity)              AS total_units_sold,
         ROUND(SUM(total_sales), 2) AS total_revenue
FROM     sales
GROUP BY product, category
ORDER BY total_revenue DESC
LIMIT    5;


-- Q5: Monthly Revenue Trend
--     strftime is SQLite's date function — extracts parts of a date
SELECT   strftime('%Y-%m', order_date)  AS month,
         COUNT(*)                        AS orders,
         ROUND(SUM(total_sales), 2)      AS monthly_revenue
FROM     sales
GROUP BY month
ORDER BY month;


-- Q6: Top Salesperson by Revenue
SELECT   salesperson,
         COUNT(*)                   AS orders_closed,
         ROUND(SUM(total_sales), 2) AS total_revenue,
         ROUND(AVG(total_sales), 2) AS avg_deal_size
FROM     sales
GROUP BY salesperson
ORDER BY total_revenue DESC;


-- Q7: Impact of Discount on Revenue
SELECT   discount_pct              AS discount,
         COUNT(*)                  AS orders,
         ROUND(AVG(total_sales),2) AS avg_revenue_per_order,
         ROUND(SUM(total_sales),2) AS total_revenue
FROM     sales
GROUP BY discount_pct
ORDER BY discount_pct;


-- Q8: Best customer by total spend
SELECT   customer,
         COUNT(*)                   AS total_orders,
         ROUND(SUM(total_sales), 2) AS lifetime_value
FROM     sales
GROUP BY customer
ORDER BY lifetime_value DESC
LIMIT    5;


-- ──────────────────────────────────────────────────────────────
-- STEP 4: INTERMEDIATE QUERIES
-- ──────────────────────────────────────────────────────────────

-- Q9: Which region has the highest average order value?
SELECT   region,
         ROUND(AVG(total_sales), 2) AS avg_order_value
FROM     sales
GROUP BY region
ORDER BY avg_order_value DESC
LIMIT 1;


-- Q10: Revenue contribution % per category
SELECT   category,
         ROUND(SUM(total_sales), 2)                      AS revenue,
         ROUND(SUM(total_sales) * 100.0 /
               (SELECT SUM(total_sales) FROM sales), 1)  AS revenue_pct
FROM     sales
GROUP BY category
ORDER BY revenue DESC;


-- Q11: Orders with discount > 10% (potential margin risk)
SELECT   order_id, product, quantity, unit_price,
         discount_pct, total_sales, salesperson
FROM     sales
WHERE    discount_pct > 10
ORDER BY total_sales DESC;


-- Q12: Filter — Electronics sales in the North region
SELECT   order_id, order_date, product, quantity,
         total_sales, salesperson
FROM     sales
WHERE    category = 'Electronics'
  AND    region   = 'North'
ORDER BY total_sales DESC;


-- ──────────────────────────────────────────────────────────────
-- STEP 5: CREATE A VIEW (like a saved query)
-- ──────────────────────────────────────────────────────────────

-- A VIEW is a virtual table — saves a complex query for reuse
CREATE VIEW IF NOT EXISTS vw_monthly_category_sales AS
SELECT   strftime('%Y-%m', order_date) AS month,
         category,
         ROUND(SUM(total_sales), 2)    AS revenue,
         COUNT(*)                      AS orders
FROM     sales
GROUP BY month, category
ORDER BY month, revenue DESC;

-- Use it like a table:
SELECT * FROM vw_monthly_category_sales;


-- ──────────────────────────────────────────────────────────────
-- NOTES FOR BEGINNERS
-- ──────────────────────────────────────────────────────────────
-- 1. Run this in "DB Browser for SQLite" (free download at sqlitebrowser.org)
-- 2. Import the Excel data: File > Import > Table from CSV
--    (Export Sales_Data sheet from Excel as CSV first)
-- 3. Run each query one at a time to understand the output
-- 4. Connect results to Power BI: use "ODBC" or load the .db file directly
-- ============================================================
