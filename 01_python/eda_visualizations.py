from pathlib import Path
import pandas as pd
import matplotlib.pyplot as plt

PROJECT_ROOT = Path(__file__).resolve().parent.parent
DATA_FILE = PROJECT_ROOT /"02_Data"/ "novamart_orders_raw.csv"
CHART_DIR = PROJECT_ROOT /"03_Visualizations"

CHART_DIR.mkdir(parents=True, exist_ok=True)

data = pd.read_csv(DATA_FILE)

data["Gross Revenue"] = data["Quantity"] * data["Unit_Price"]
data["Discount_Amount"] = (data["Gross Revenue"] * data["Discount_Pct"] / 100 )
data["Net_Revenue"] = data["Gross Revenue"] - data["Discount_Amount"]

# 1 Net Revenue By Category.
category_revenue = (data.groupby("Category")["Net_Revenue"].sum().sort_values(ascending=False))

plt.figure(figsize=(9,5))
category_revenue.plot(kind="bar")
plt.title("Novamart Net Revenue by Category")
plt.xlabel("Category")
plt.ylabel("Net_Revenue ")
plt.xticks(rotation=0)
plt.tight_layout()
plt.savefig(CHART_DIR / "eda_category_revenue.png",dpi=200)
plt.close()

# 2 Net Revenue by Region
region_revenue = (data.groupby("Region")["Net_Revenue"].sum().sort_values(ascending=False))

plt.figure(figsize=(9,5))
region_revenue.plot(kind="bar")
plt.title("Novamart Net Revenue by Region")
plt.xlabel("Region")
plt.ylabel("Net_Revenue")
plt.xticks(rotation=0)
plt.tight_layout()
plt.savefig(CHART_DIR / "eda_region_revenue.png", dpi=200)
plt.close()

print("Category Chart Saved :(eda_category_revenue.png)")
print("Regional Chart Saved : (eda_region_revenue.png)")
print("\n Chart folder :",CHART_DIR)






                  




                











