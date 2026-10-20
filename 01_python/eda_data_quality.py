from pathlib import Path
import pandas as pd
PROJECT_ROOT = Path(__file__).resolve().parent.parent
DATA_FILE = PROJECT_ROOT / "02_Data" / "novamart_orders_raw.csv"

data = pd.read_csv(DATA_FILE)

print("\n---------- Missing values per coloum----------")
print(data.isnull().sum())

print("\n --------------Total Missing Values---------")
print(data.isnull().sum().sum())

print("\n-------Duplicate Rows----------")
print(data.duplicated().sum())

print("\n------------ Duplicate Order IDs--------")
print(data["Order_ID"].duplicated().sum())






