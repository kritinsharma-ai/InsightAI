from pathlib import Path
import pandas as pd

PROJECT_ROOT = Path(__file__).resolve().parent.parent
DATA_FILE = PROJECT_ROOT / "02_DATA" / "novamart_orders_raw.csv"

data = pd.read_csv(DATA_FILE)

# Calculate revenue before discount
data["Gross_Revenue"] = data["Quantity"] * data["Unit_Price"]

# Calculate discount and revenue after discount
data["Discount_Amount"] = (
    data["Gross_Revenue"] * data["Discount_Pct"] / 100
)

data["Net_Revenue"] = (
    data["Gross_Revenue"] - data["Discount_Amount"]
)

print("\n---------- First five order with revenue---------------")
print(data[
        [
            "Order_ID",
            "Product",
            "Quantity",
            "Unit_Price",
            "Discount_Pct",
            "Gross_Revenue",
            "Net_Revenue",
        ]
    ].head().to_string(index=False)
)

print("\n-----------Revenue Summary---------------")
print(data[["Gross_Revenue","Discount_Amount","Net_Revenue"]].sum().round(2))


# Product-level performance analysis
product_summary = (
    data.groupby("Product")
    .agg(
        Orders=("Order_ID", "count"),
        Units_Sold=("Quantity", "sum"),
        Gross_Revenue=("Gross_Revenue", "sum"),
        Discount_Amount=("Discount_Amount", "sum"),
        Net_Revenue=("Net_Revenue", "sum"),
    )
    .sort_values("Net_Revenue", ascending=False)
)

print("\n--- Product Performance Ranking ---")
print(product_summary.round(2).to_string())

print("\n--- Top Product by Net Revenue ---")
print(product_summary["Net_Revenue"].idxmax())

print("\n--- Top Product by Units Sold ---")
print(product_summary["Units_Sold"].idxmax())

                           


