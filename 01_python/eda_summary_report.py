
from pathlib import Path
import pandas as pd

PROJECT_ROOT = Path(__file__).resolve().parent.parent
DATA_FILE = PROJECT_ROOT / "02_Data" / "novamart_orders_raw.csv"
OUTPUT_FILE = PROJECT_ROOT / "02_Data" / "novamart_eda_summary.txt"

data = pd.read_csv(DATA_FILE)
data["Order_Date"] = pd.to_datetime(data["Order_Date"])

data["Gross_Revenue"] = data["Quantity"] * data["Unit_Price"]
data["Discount_Amount"] = (
    data["Gross_Revenue"] * data["Discount_Pct"] / 100
)
data["Net_Revenue"] = data["Gross_Revenue"] - data["Discount_Amount"]
data["Month"] = data["Order_Date"].dt.to_period("M")

# Overall KPIs
total_orders = data["Order_ID"].nunique()
total_units = data["Quantity"].sum()
gross_revenue = data["Gross_Revenue"].sum()
discount_amount = data["Discount_Amount"].sum()
net_revenue = data["Net_Revenue"].sum()

# Product, category, region, and monthly performance
product_summary = data.groupby("Product")["Net_Revenue"].sum()
category_summary = data.groupby("Category")["Net_Revenue"].sum()
region_summary = data.groupby("Region")["Net_Revenue"].sum()
monthly_summary = data.groupby("Month")["Net_Revenue"].sum()

report = f"""
INSIGHTAI — NOVAMART EDA SUMMARY
================================

OVERALL KPIs
------------
Unique Orders: {total_orders}
Units Sold: {total_units:,}
Gross Revenue: ₹{gross_revenue:,.2f}
Discounts: ₹{discount_amount:,.2f}
Net Revenue: ₹{net_revenue:,.2f}

TOP-PERFORMING PRODUCT
---------------------
{product_summary.idxmax()}: ₹{product_summary.max():,.2f}

TOP-PERFORMING CATEGORY
-----------------------
{category_summary.idxmax()}: ₹{category_summary.max():,.2f}

TOP-PERFORMING REGION
---------------------
{region_summary.idxmax()}: ₹{region_summary.max():,.2f}

MONTHLY PERFORMANCE
-------------------
Best Month: {monthly_summary.idxmax()}
Best Month Net Revenue: ₹{monthly_summary.max():,.2f}

Lowest Month: {monthly_summary.idxmin()}
Lowest Month Net Revenue: ₹{monthly_summary.min():,.2f}

DATA QUALITY
------------
Missing Values: {data.isnull().sum().sum()}
Duplicate Rows: {data.duplicated().sum()}
Unique Order IDs: {data["Order_ID"].nunique()}
Dataset Rows: {len(data)}

NOTE
----
This report analyzes simulated NovaMart order data for 2025.
Revenue is calculated after listed discounts, before costs and taxes.
"""

OUTPUT_FILE.write_text(report.strip() + "\n", encoding="utf-8")

print("EDA summary report generated successfully.")
print("Report path:", OUTPUT_FILE)

