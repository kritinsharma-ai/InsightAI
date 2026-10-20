from pathlib import Path
import pandas as pd

PROJECT_ROOT = Path(__file__).resolve().parent.parent
DATA_FILE = PROJECT_ROOT / "02_DATA" / "novamart_orders_raw.csv" 

data = pd.read_csv(DATA_FILE)

print("\n----------Original Data Types-----------")
print(data.dtypes)

# Convert order_date from text to date_time
data["Order_Date"] = pd.to_datetime(data["Order_Date"])

print("\n-----------Updated Data Type---------")
print(data["Order_Date"].dtype)

print("\n------------Earliest Order Date----------")
print(data["Order_Date"].min())

print("\n-------------Latest Order Date-----------")
print(data["Order_Date"].max()) 

print("\n-------------Numeric Summary-------------")
print(data[["Quantity", "Unit_Price", "Discount_Pct"]].describe())




