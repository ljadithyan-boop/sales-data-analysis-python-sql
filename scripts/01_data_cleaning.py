# ============================================================
# 01_data_cleaning.py
# Sales Data Analysis — Data Cleaning Stage
# Author: Adithyan L J
# Dataset: Retail Sales Dataset (superstore_raw.csv)
# ============================================================

import pandas as pd
import numpy as np
import os

# ─── 1. LOAD DATA ────────────────────────────────────────────
print("=" * 55)
print("  STAGE 1: Loading Data")
print("=" * 55)

df = pd.read_csv("superstore_raw.csv")

print(f"✅ Dataset loaded successfully")
print(f"   Rows    : {df.shape[0]}")
print(f"   Columns : {df.shape[1]}")
print(f"\nColumn Names:\n{list(df.columns)}\n")

# ─── 2. INITIAL INSPECTION ───────────────────────────────────
print("=" * 55)
print("  STAGE 2: Initial Inspection")
print("=" * 55)

print("\n📋 First 5 Rows:")
print(df.head())

print("\n📊 Data Types:")
print(df.dtypes)

print("\n📈 Basic Statistics:")
print(df.describe())

# ─── 3. CHECK MISSING VALUES ─────────────────────────────────
print("\n" + "=" * 55)
print("  STAGE 3: Missing Values")
print("=" * 55)

missing = df.isnull().sum()
missing_pct = (df.isnull().sum() / len(df)) * 100
missing_df = pd.DataFrame({
    "Missing Count": missing,
    "Missing %": missing_pct.round(2)
})
missing_df = missing_df[missing_df["Missing Count"] > 0]

if missing_df.empty:
    print("✅ No missing values found!")
else:
    print(f"⚠️  Columns with missing values:\n{missing_df}")

    # Fill numeric columns with median
    numeric_cols = df.select_dtypes(include=[np.number]).columns
    for col in numeric_cols:
        if df[col].isnull().sum() > 0:
            median_val = df[col].median()
            df[col].fillna(median_val, inplace=True)
            print(f"   ✅ Filled '{col}' nulls with median: {median_val}")

    # Fill categorical columns with mode
    cat_cols = df.select_dtypes(include=["object"]).columns
    for col in cat_cols:
        if df[col].isnull().sum() > 0:
            mode_val = df[col].mode()[0]
            df[col].fillna(mode_val, inplace=True)
            print(f"   ✅ Filled '{col}' nulls with mode: {mode_val}")

# ─── 4. REMOVE DUPLICATES ────────────────────────────────────
print("\n" + "=" * 55)
print("  STAGE 4: Duplicate Records")
print("=" * 55)

before = len(df)
df.drop_duplicates(inplace=True)
after = len(df)
removed = before - after

if removed == 0:
    print("✅ No duplicate rows found!")
else:
    print(f"⚠️  Removed {removed} duplicate rows")
    print(f"   Before: {before} rows → After: {after} rows")

# ─── 5. FIX DATA TYPES ───────────────────────────────────────
print("\n" + "=" * 55)
print("  STAGE 5: Fixing Data Types")
print("=" * 55)

# Detect and convert date columns
date_keywords = ["date", "Date", "DATE"]
for col in df.columns:
    if any(kw in col for kw in date_keywords):
        try:
            df[col] = pd.to_datetime(df[col], errors="coerce")
            print(f"✅ Converted '{col}' to datetime")
        except Exception as e:
            print(f"⚠️  Could not convert '{col}': {e}")

# Detect and fix numeric columns stored as strings
for col in df.select_dtypes(include="object").columns:
    cleaned = df[col].str.replace(r"[₹$,\s]", "", regex=True)
    try:
        df[col] = pd.to_numeric(cleaned)
        print(f"✅ Converted '{col}' from string to numeric")
    except (ValueError, AttributeError):
        pass  # Column is genuinely text, leave as-is

# ─── 6. STANDARDIZE TEXT COLUMNS ─────────────────────────────
print("\n" + "=" * 55)
print("  STAGE 6: Standardizing Text")
print("=" * 55)

text_cols = df.select_dtypes(include="object").columns
for col in text_cols:
    df[col] = df[col].str.strip()        # Remove leading/trailing spaces
    df[col] = df[col].str.title()        # Title Case
print(f"✅ Stripped whitespace and applied Title Case to {len(text_cols)} text columns")

# ─── 7. STANDARDIZE COLUMN NAMES ─────────────────────────────
print("\n" + "=" * 55)
print("  STAGE 7: Standardizing Column Names")
print("=" * 55)

original_cols = list(df.columns)
df.columns = (
    df.columns
    .str.strip()
    .str.lower()
    .str.replace(" ", "_")
    .str.replace(r"[^a-z0-9_]", "", regex=True)
)
print("✅ Column names standardized:")
for old, new in zip(original_cols, df.columns):
    if old != new:
        print(f"   '{old}' → '{new}'")

# ─── 8. ADD DERIVED COLUMNS ──────────────────────────────────
print("\n" + "=" * 55)
print("  STAGE 8: Adding Derived Columns")
print("=" * 55)

# Try to add Year, Month, Quarter from any date column found
date_cols = df.select_dtypes(include="datetime64").columns
for col in date_cols:
    df[f"{col}_year"]    = df[col].dt.year
    df[f"{col}_month"]   = df[col].dt.month
    df[f"{col}_quarter"] = df[col].dt.quarter
    print(f"✅ Extracted Year, Month, Quarter from '{col}'")

# Try to add Profit Margin if both profit and sales columns exist
col_list = list(df.columns)
if "profit" in col_list and "sales" in col_list:
    df["profit_margin_pct"] = ((df["profit"] / df["sales"]) * 100).round(2)
    df["profit_margin_pct"].replace([np.inf, -np.inf], 0, inplace=True)
    print("✅ Added 'profit_margin_pct' column")

# ─── 9. FINAL VALIDATION ─────────────────────────────────────
print("\n" + "=" * 55)
print("  STAGE 9: Final Validation")
print("=" * 55)

print(f"   Total Rows    : {df.shape[0]}")
print(f"   Total Columns : {df.shape[1]}")
print(f"   Missing Values: {df.isnull().sum().sum()}")
print(f"   Duplicates    : {df.duplicated().sum()}")
print(f"\n✅ Dataset is clean and ready for analysis!")

# ─── 10. EXPORT CLEAN DATA ───────────────────────────────────
print("\n" + "=" * 55)
print("  STAGE 10: Exporting Cleaned Data")
print("=" * 55)

output_path = "superstore_cleaned.csv"
df.to_csv(output_path, index=False)
print(f"✅ Cleaned dataset saved to '{output_path}'")
print(f"   File size: {os.path.getsize(output_path) / 1024:.1f} KB")
print("\n" + "=" * 55)
print("  ✅ DATA CLEANING COMPLETE")
print("=" * 55)
