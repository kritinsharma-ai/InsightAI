
from pathlib import Path
import pandas as pd

PROJECT_ROOT = Path(__file__).resolve().parent.parent
DATA_FILE = PROJECT_ROOT / "02_Data" / "novamart_orders_raw.csv"

# Load the dataset
data = pd.read_csv(DATA_FILE)

# Inspect its basic structure
print("\n--- First 5 Rows ---")
print(data.head())

print("\n--- Dataset Shape ---")
print(data.shape)

print("\n--- Column Names ---")
print(data.columns.tolist())

print("\n--- Data Types and Non-Null Counts ---")
data.info()

from pathlib import Path
import pandas as pd

PROJECT_ROOT = Path(__file__).resolve().parent.parent
DATA_FILE = PROJECT_ROOT / "02_Data" / "novamart_orders_raw.csv"

# Load the dataset
data = pd.read_csv(DATA_FILE)

# Inspect its basic structure
print("\n--- First 5 Rows ---")
print(data.head())

print("\n--- Dataset Shape ---")
print(data.shape)

print("\n--- Column Names ---")
print(data.columns.tolist())

print("\n--- Data Types and Non-Null Counts ---")
data.info()



