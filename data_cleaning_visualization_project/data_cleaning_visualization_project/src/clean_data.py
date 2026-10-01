import pandas as pd
import numpy as np
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parents[1]
RAW_FILE = BASE_DIR / "data" / "raw" / "retail_sales_raw.csv"
OUTPUT_FILE = BASE_DIR / "data" / "processed" / "retail_sales_cleaned.csv"

df = pd.read_csv(RAW_FILE)

# Standardize column names
df.columns = (
    df.columns.str.strip()
              .str.lower()
              .str.replace(" ", "_")
)

# Convert data types
df["order_date"] = pd.to_datetime(df["order_date"], errors="coerce")
numeric_cols = ["quantity", "unit_price", "discount", "revenue", "cost", "profit"]
for col in numeric_cols:
    df[col] = pd.to_numeric(df[col], errors="coerce")

# Remove exact duplicate records
before_duplicates = len(df)
df = df.drop_duplicates()
duplicates_removed = before_duplicates - len(df)

# Handle missing values
df["region"] = df["region"].fillna("Unknown")
df["quantity"] = df["quantity"].fillna(df["quantity"].median())
df["discount"] = df["discount"].fillna(df["discount"].median())
df["cost"] = df["cost"].fillna(df["cost"].median())

# Treat unrealistic values using IQR capping
def cap_iqr(series):
    q1 = series.quantile(0.25)
    q3 = series.quantile(0.75)
    iqr = q3 - q1
    lower = q1 - 1.5 * iqr
    upper = q3 + 1.5 * iqr
    return series.clip(lower, upper)

for col in ["quantity", "unit_price"]:
    df[col] = cap_iqr(df[col])

# Recalculate derived measures after cleaning
df["revenue"] = df["quantity"] * df["unit_price"] * (1 - df["discount"])
df["profit"] = df["revenue"] - df["cost"]
df["profit_margin"] = np.where(
    df["revenue"] != 0,
    df["profit"] / df["revenue"],
    0
)

# Sort and save
df = df.sort_values("order_date").reset_index(drop=True)
df.to_csv(OUTPUT_FILE, index=False)

print("Cleaning completed.")
print(f"Rows after cleaning: {len(df)}")
print(f"Duplicate rows removed: {duplicates_removed}")
print(f"Missing values remaining: {int(df.isna().sum().sum())}")
print(f"Saved to: {OUTPUT_FILE}")
