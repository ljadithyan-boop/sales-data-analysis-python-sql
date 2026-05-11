"""
RetailSales Analytics — Python Analysis Script
Tools: pandas, matplotlib, sqlite3
Run: python analysis.py
"""

import pandas as pd
import sqlite3
import matplotlib.pyplot as plt
import matplotlib.ticker as mticker
import os

# ──────────────────────────────────────────────────────────────
# STEP 1: LOAD DATA FROM EXCEL
# ──────────────────────────────────────────────────────────────

print("=" * 55)
print(" RetailSales Analytics — Python Script")
print("=" * 55)

# Load the Excel file into a DataFrame (a table in Python)
df = pd.read_excel("RetailSales_Dataset.xlsx", sheet_name="Sales_Data")

print(f"\n✅ Data loaded: {df.shape[0]} rows × {df.shape[1]} columns")
print("\n📋 First 5 rows:")
print(df.head())

print("\n📊 Data types & null check:")
print(df.info())


# ──────────────────────────────────────────────────────────────
# STEP 2: DATA CLEANING
# ──────────────────────────────────────────────────────────────

print("\n🔧 Cleaning data...")

# Convert Date column to proper datetime type
df["Date"] = pd.to_datetime(df["Date"])

# Add helper columns
df["Month"]       = df["Date"].dt.to_period("M").astype(str)   # "2024-01"
df["Month_Name"]  = df["Date"].dt.strftime("%b %Y")            # "Jan 2024"
df["Quarter"]     = "Q" + df["Date"].dt.quarter.astype(str)   # "Q1"

# Check for missing values
print(f"   Missing values: {df.isnull().sum().sum()} (should be 0)")
print(f"   Date range: {df['Date'].min().date()} → {df['Date'].max().date()}")


# ──────────────────────────────────────────────────────────────
# STEP 3: SAVE TO SQLite DATABASE (connects to your SQL script!)
# ──────────────────────────────────────────────────────────────

conn = sqlite3.connect("sales_database.db")

df_sql = df[["OrderID","Date","Customer","Region","Category",
             "Product","Quantity","UnitPrice","Discount(%)","TotalSales","Salesperson"]]
df_sql.columns = ["order_id","order_date","customer","region","category",
                  "product","quantity","unit_price","discount_pct","total_sales","salesperson"]
df_sql.to_sql("sales", conn, if_exists="replace", index=False)

print("\n✅ Data saved to SQLite → sales_database.db")
print("   (Open in DB Browser for SQLite to run your SQL queries)")


# ──────────────────────────────────────────────────────────────
# STEP 4: ANALYSIS WITH PANDAS
# ──────────────────────────────────────────────────────────────

print("\n" + "─" * 55)
print("📈 KEY METRICS")
print("─" * 55)

total_rev    = df["TotalSales"].sum()
total_orders = len(df)
avg_order    = df["TotalSales"].mean()

print(f"   Total Revenue   : ₹{total_rev:,.2f}")
print(f"   Total Orders    : {total_orders}")
print(f"   Avg Order Value : ₹{avg_order:,.2f}")

# Revenue by Category
print("\n📦 Revenue by Category:")
cat_summary = (df.groupby("Category")["TotalSales"]
                 .agg(["sum","count","mean"])
                 .rename(columns={"sum":"Revenue","count":"Orders","mean":"Avg Order"})
                 .sort_values("Revenue", ascending=False))
cat_summary["Revenue"] = cat_summary["Revenue"].map("₹{:,.0f}".format)
cat_summary["Avg Order"] = cat_summary["Avg Order"].map("₹{:,.0f}".format)
print(cat_summary.to_string())

# Revenue by Region
print("\n🗺️  Revenue by Region:")
region_summary = (df.groupby("Region")["TotalSales"]
                    .agg(["sum","count"])
                    .rename(columns={"sum":"Revenue","count":"Orders"})
                    .sort_values("Revenue", ascending=False))
region_summary["Revenue"] = region_summary["Revenue"].map("₹{:,.0f}".format)
print(region_summary.to_string())

# Top Salesperson
print("\n🏆 Top Salesperson:")
top_sp = (df.groupby("Salesperson")["TotalSales"]
            .sum()
            .sort_values(ascending=False)
            .reset_index())
top_sp.columns = ["Salesperson", "Revenue"]
print(f"   {top_sp.iloc[0]['Salesperson']} with ₹{top_sp.iloc[0]['Revenue']:,.0f}")


# ──────────────────────────────────────────────────────────────
# STEP 5: VISUALIZATIONS (4 charts → saved as PNG)
# ──────────────────────────────────────────────────────────────

print("\n🎨 Generating charts...")

BLUE_PALETTE = ["#1F4E79","#2E75B6","#5BA3D9","#A8D1F0","#D4E8F8"]
plt.rcParams.update({"font.family": "DejaVu Sans", "axes.spines.top": False,
                     "axes.spines.right": False})

fig, axes = plt.subplots(2, 2, figsize=(14, 10))
fig.suptitle("RetailSales Analytics Dashboard  |  2024", fontsize=16,
             fontweight="bold", color="#1F4E79", y=1.01)

# ── Chart 1: Revenue by Category (bar) ───────────────────────
ax1 = axes[0, 0]
cat_rev = df.groupby("Category")["TotalSales"].sum().sort_values(ascending=False)
bars = ax1.bar(cat_rev.index, cat_rev.values, color=BLUE_PALETTE[:len(cat_rev)])
ax1.set_title("Revenue by Category", fontweight="bold", color="#1F4E79")
ax1.set_ylabel("Revenue (₹)")
ax1.yaxis.set_major_formatter(mticker.FuncFormatter(lambda x, _: f"₹{x/1000:.0f}K"))
for bar, val in zip(bars, cat_rev.values):
    ax1.text(bar.get_x() + bar.get_width()/2, bar.get_height() + 500,
             f"₹{val/1000:.0f}K", ha="center", va="bottom", fontsize=8, fontweight="bold")

# ── Chart 2: Monthly Revenue Trend (line) ────────────────────
ax2 = axes[0, 1]
monthly = df.groupby("Month")["TotalSales"].sum().reset_index()
ax2.plot(monthly["Month"], monthly["TotalSales"], marker="o",
         color="#1F4E79", linewidth=2.5, markersize=6)
ax2.fill_between(monthly["Month"], monthly["TotalSales"], alpha=0.15, color="#2E75B6")
ax2.set_title("Monthly Revenue Trend", fontweight="bold", color="#1F4E79")
ax2.set_ylabel("Revenue (₹)")
ax2.yaxis.set_major_formatter(mticker.FuncFormatter(lambda x, _: f"₹{x/1000:.0f}K"))
ax2.set_xticks(range(0, len(monthly["Month"]), 2))
ax2.set_xticklabels(monthly["Month"].iloc[::2], rotation=45, ha="right", fontsize=8)

# ── Chart 3: Revenue by Region (pie) ─────────────────────────
ax3 = axes[1, 0]
region_rev = df.groupby("Region")["TotalSales"].sum()
wedges, texts, autotexts = ax3.pie(
    region_rev.values,
    labels=region_rev.index,
    autopct="%1.1f%%",
    colors=BLUE_PALETTE[:len(region_rev)],
    startangle=90,
    pctdistance=0.8,
)
for text in autotexts:
    text.set_fontsize(9); text.set_fontweight("bold")
ax3.set_title("Revenue Share by Region", fontweight="bold", color="#1F4E79")

# ── Chart 4: Top Salesperson (horizontal bar) ────────────────
ax4 = axes[1, 1]
sp_rev = df.groupby("Salesperson")["TotalSales"].sum().sort_values()
bars_h = ax4.barh(sp_rev.index, sp_rev.values, color="#2E75B6")
ax4.set_title("Revenue by Salesperson", fontweight="bold", color="#1F4E79")
ax4.set_xlabel("Revenue (₹)")
ax4.xaxis.set_major_formatter(mticker.FuncFormatter(lambda x, _: f"₹{x/1000:.0f}K"))
for bar, val in zip(bars_h, sp_rev.values):
    ax4.text(bar.get_width() + 200, bar.get_y() + bar.get_height()/2,
             f"₹{val/1000:.0f}K", va="center", fontsize=8, fontweight="bold")

plt.tight_layout()
plt.savefig("sales_charts.png", dpi=150, bbox_inches="tight")
plt.close()
print("   ✅ Charts saved → sales_charts.png")


# ──────────────────────────────────────────────────────────────
# STEP 6: EXPORT CLEAN DATA FOR POWER BI
# ──────────────────────────────────────────────────────────────

df.to_csv("sales_clean_for_powerbi.csv", index=False)
print("   ✅ Clean CSV saved → sales_clean_for_powerbi.csv")

conn.close()
print("\n🎉 All done! Files created:")
print("   • sales_database.db     → open in DB Browser for SQLite")
print("   • sales_charts.png      → 4 analysis charts")
print("   • sales_clean_for_powerbi.csv → import into Power BI")
print("=" * 55)
