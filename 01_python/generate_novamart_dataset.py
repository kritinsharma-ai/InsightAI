import csv
import random 
print("Dataset generator script is running...")
print("Running module name:", __name__)
from datetime import date , timedelta
from pathlib import Path

# Make the generated dataset reproducible.
random.seed(42)

PROJECT_ROOT = Path(__file__).resolve().parent.parent 
DATA_DIR = PROJECT_ROOT / "02_Data"
OUTPUT_FILE = DATA_DIR / "novamart_orders_raw.csv"

products = [{"product": "Laptop", "category": "Electronics", "price": 50000},
    {"product": "Phone", "category": "Electronics", "price": 30000},
    {"product": "Headphones", "category": "Electronics", "price": 5000},
    {"product": "Watch", "category": "Fashion", "price": 4000},
    {"product": "Shoes", "category": "Fashion", "price": 3500},
    {"product": "T-Shirt", "category": "Fashion", "price": 800},
    {"product": "Backpack", "category": "Accessories", "price": 1800},
    {"product": "Sunglasses", "category": "Accessories", "price": 1200},
]

REGIONS = ["North","South","East","West","Central"]
PAYMENT_METHODS = ["UPI","Card","Cash","Netbanking"]
CUSTOMER_TYPES = ["New","Returning"]

START_DATE = date(2025,1,1)
END_DATE = date(2025,12,31)

TOTAL_ORDERS = 500

def random_order_date():
    days = (END_DATE - START_DATE).days
    return START_DATE + timedelta(days=random.randint(0,days))

def generate_dataset():
    DATA_DIR.mkdir(parents=True,exist_ok=True)

    with OUTPUT_FILE.open("w",newline ="" , encoding = "utf-8")as file:
        fieldnames = [
            "Order_ID",
            "Order_Date",
            "Product",
            "Category",
            "Region",
            "Quantity",
            "Unit_Price",
            "Discount_Pct",
            "Payment_Method",
            "Customer_Type",
        ]

        writer = csv.DictWriter(file,fieldnames=fieldnames)
        writer.writeheader()


        for order_number in range(1, TOTAL_ORDERS +1):
            product = random.choice(products)

            writer.writerow({"Order_ID": f"NM{order_number:05d}",
                "Order_Date": random_order_date().isoformat(),
                "Product": product["product"],
                "Category": product["category"],
                "Region": random.choice(REGIONS),
                "Quantity": random.randint(1, 5),
                "Unit_Price": product["price"],
                "Discount_Pct": random.choice([0, 0, 5, 10, 15, 20]),
                "Payment_Method": random.choice(PAYMENT_METHODS),
                "Customer_Type": random.choice(CUSTOMER_TYPES),
            })

            print(f"Dataset Format Generated Successfully:{OUTPUT_FILE.name}")
            print(f"Total Orders Records : {TOTAL_ORDERS}")


            
if __name__ == "__main__":
    print("Main entry point reached.")
    print(f"Output path: {OUTPUT_FILE}")
    generate_dataset()
    print("Dataset generation function finished.")




                  
                  




