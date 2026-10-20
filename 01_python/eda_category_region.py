from pathlib import Path
import pandas as pd

PROJECT_ROOT = Path(__file__).resolve().parent.parent
DATA_FILE = PROJECT_ROOT / "02_Data" / "novamart_orders_raw.csv"

data = pd.read_csv(DATA_FILE)

# Calculate net revenue 
data["Gross_Revenue"] = data["Quantity"] * data["Unit_Price"]
data["Discount_Amount"] = (data["Gross_Revenue"] * data["Discount_Pct"] / 100 )
data["Net_Revenue"] = data["Gross_Revenue"] - data["Discount_Amount"]

# Category Performance 
category_summary = (data.groupby("Category").agg(Orders=("Order_ID", "count"),
                   Units_Sold=("Quantity", "sum"),
                   Net_Revenue=("Net_Revenue", "sum"),).sort_values("Net_Revenue",ascending=False))
print("\n-------------------Category Performance------------------")
print(category_summary.round(2).to_string())

# Regional Performance 
region_summary = data.groupby("Region").agg(orders = ("Order_ID", "count"),
        Units_Sold=("Quantity", "sum"),
        Net_Revenue=("Net_Revenue", "sum"),
    ).sort_values("Net_Revenue", ascending=False)

print("\n----------------Regional Perfromance----------------")
print(region_summary.round(2).to_string())

print("\nTop Category:", category_summary["Net_Revenue"].idxmax())
print("Top region", region_summary["Net_Revenue"].idxmax())


