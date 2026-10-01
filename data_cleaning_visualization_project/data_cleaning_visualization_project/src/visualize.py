import pandas as pd
import matplotlib.pyplot as plt
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parents[1]
INPUT_FILE = BASE_DIR / "data" / "processed" / "retail_sales_cleaned.csv"
FIG_DIR = BASE_DIR / "outputs" / "figures"
FIG_DIR.mkdir(parents=True, exist_ok=True)

df = pd.read_csv(INPUT_FILE, parse_dates=["order_date"])

# 1. Monthly revenue trend
monthly = df.set_index("order_date").resample("ME")["revenue"].sum()
plt.figure(figsize=(10, 5))
monthly.plot(marker="o")
plt.title("Monthly Revenue Trend")
plt.xlabel("Month")
plt.ylabel("Revenue")
plt.grid(alpha=0.3)
plt.tight_layout()
plt.savefig(FIG_DIR / "01_monthly_revenue_trend.png", dpi=150)
plt.close()

# 2. Revenue by region
region = df.groupby("region")["revenue"].sum().sort_values(ascending=False)
plt.figure(figsize=(8, 5))
region.plot(kind="bar")
plt.title("Revenue by Region")
plt.xlabel("Region")
plt.ylabel("Revenue")
plt.xticks(rotation=0)
plt.tight_layout()
plt.savefig(FIG_DIR / "02_revenue_by_region.png", dpi=150)
plt.close()

# 3. Profit by category
category = df.groupby("category")["profit"].sum().sort_values(ascending=False)
plt.figure(figsize=(8, 5))
category.plot(kind="bar")
plt.title("Profit by Category")
plt.xlabel("Category")
plt.ylabel("Profit")
plt.xticks(rotation=0)
plt.tight_layout()
plt.savefig(FIG_DIR / "03_profit_by_category.png", dpi=150)
plt.close()

# 4. Product revenue
product = df.groupby("product")["revenue"].sum().sort_values(ascending=True)
plt.figure(figsize=(9, 5))
product.plot(kind="barh")
plt.title("Revenue by Product")
plt.xlabel("Revenue")
plt.ylabel("Product")
plt.tight_layout()
plt.savefig(FIG_DIR / "04_revenue_by_product.png", dpi=150)
plt.close()

# 5. Quantity vs revenue
plt.figure(figsize=(8, 5))
plt.scatter(df["quantity"], df["revenue"], alpha=0.6)
plt.title("Quantity vs Revenue")
plt.xlabel("Quantity")
plt.ylabel("Revenue")
plt.grid(alpha=0.3)
plt.tight_layout()
plt.savefig(FIG_DIR / "05_quantity_vs_revenue.png", dpi=150)
plt.close()

print("All visualizations saved to outputs/figures/")
