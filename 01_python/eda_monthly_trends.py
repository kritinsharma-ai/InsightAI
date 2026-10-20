
from pathlib import Path
import pandas as pd
import matplotlib.pyplot as plt

PROJECT_ROOT = Path(__file__).resolve().parent.parent
DATA_FILE = PROJECT_ROOT / "02_Data" / "novamart_orders_raw.csv"
CHART_DIR = PROJECT_ROOT / "03_Visualizations"

CHART_DIR.mkdir(parents=True, exist_ok=True)

data = pd.read_csv(DATA_FILE)

# Convert order dates to datetime
data["Order_Date"] = pd.to_datetime(data["Order_Date"])

# Calculate revenue after discounts
data["Gross_Revenue"] = data["Quantity"] * data["Unit_Price"]
data["Discount_Amount"] = (
    data["Gross_Revenue"] * data["Discount_Pct"] / 100
)
data["Net_Revenue"] = data["Gross_Revenue"] - data["Discount_Amount"]

# Create a monthly period for grouping
data["Month"] = data["Order_Date"].dt.to_period("M")

monthly_summary = (
    data.groupby("Month")
    .agg(
        Orders=("Order_ID", "count"),
        Units_Sold=("Quantity", "sum"),
        Net_Revenue=("Net_Revenue", "sum"),
    )
    .sort_index()
)

print("\n--- Monthly Sales Performance ---")
print(monthly_summary.round(2).to_string())

print("\nBest month:", monthly_summary["Net_Revenue"].idxmax())
print("Lowest month:", monthly_summary["Net_Revenue"].idxmin())

# Plot monthly net revenue
plt.figure(figsize=(12, 6))
plt.plot(
    monthly_summary.index.astype(str),
    monthly_summary["Net_Revenue"],
    marker="o",
)
plt.title("NovaMart Monthly Net Revenue — 2025")
plt.xlabel("Month")
plt.ylabel("Net Revenue (₹)")
plt.xticks(rotation=45)
plt.grid(axis="y", linestyle="--", alpha=0.3)
plt.tight_layout()

chart_path = CHART_DIR / "eda_monthly_net_revenue.png"
plt.savefig(chart_path, dpi=200)
plt.close()

print("\nMonthly trend chart saved:", chart_path)

