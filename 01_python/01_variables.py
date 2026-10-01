
business_name = "NovaMart"
daily_sales = 18500
customers_today = 125

print(business_name)
print(daily_sales)
print(customers_today)

monday_sales = 12500
tuesday_sales = 15800
wednesday_sales = 11200
thursday_sales = 18500
friday_sales = 21000

total_sales = (monday_sales + tuesday_sales + wednesday_sales + thursday_sales + friday_sales)
print(total_sales)
average_sales = total_sales / 5
print(average_sales)
highest_sales = max(monday_sales, tuesday_sales, wednesday_sales, thursday_sales, friday_sales)
print(highest_sales)
lowest_sales = min(monday_sales, tuesday_sales, wednesday_sales, thursday_sales, friday_sales)
print(lowest_sales)
daily_target = 15000
target_difference = average_sales - daily_target
print(target_difference)
if average_sales >= daily_target:
   print("Daily sales target achieved")
else:
   print("Daily sales target not achieved")


if average_sales >= 20000:
    print("excellent")
elif average_sales <= 20000 and average_sales >= 15000:
    print("good")
else:
    print("poor")    

sales = [12500, 15800, 11200, 18500, 21000]
print(sales)
print(sales[0])
print(sales[4])
print(len(sales))
print(sum(sales))
average_sales = sum(sales) / len(sales)
print(average_sales)
sales.append(17500)
print(sales)
print(len(sales))
sales[2] = 13200
print(sales[2])
print(sales)
sales.pop(5)
print(sales)
print(len(sales))
for sale in sales:
    print(sale)
total = 0
for sale in sales:
    total = total + sale
    print(total)
for sale in sales:
    if sale > 15000:
        print(sale)
for sale in sales:
    if sale < 15000:
        print(sale)
for sale in sales:
    if sale >= 15000:
        print("Above target")
    else:
        print("below target")

for sale in sales:
    if sale >= 20000:
        print("Excellent")
    elif sale >= 15000 and sale <= 20000:
        print("Good")
    else:
        print("Needs Improvement")



def calculate_total(sales):
    total = 0

    for sale in sales:
        total = total + sale

    return total

total_sales = calculate_total(sales)
print(total_sales)   

def calculate_average(sales):
    total = sum(sales)
    
    average = total / len(sales)
    return average
average_sales = calculate_average(sales)
print(average_sales)

def find_highest_sale(sales):
    sales = max(sales)
    return sales
sales =  find_highest_sale(sales)
print(sales)

sales = [12500, 15800, 13200, 18500, 21000]
def find_lowest_sale(sales):
    sales = min(sales)
    return sales
sales = find_lowest_sale(sales)
print(sales)

customer_name = "Rahul"
product = "iPhone 16"
category = "Electronics"

message = customer_name + " purchased " + product
print(message)
message = f"{customer_name} purchased {product} in the {category} category."
print(message)
customer_name = "   Rahul   "
clean_name = customer_name.strip()
print(clean_name)
category = "Electronics"
new_category = category.replace("Electronics", "TECH & Elctronics")
print(new_category)
customer_info = "Rahul,Electronics,125000"
parts = customer_info.split(",")
print(parts)
raw_data = "  Rahul , Electronics , 125000  "
data = raw_data.strip().split(",")
print(data)
print(data[0].strip())
print(data[1].strip())
print(data[2].strip())

customer_name = input("Enter customer name: " )
print("Customer name is " + customer_name)

customer_spending = int(input("Enter customer spending "))
print("Customer spending is " + str(customer_spending))

price = int(input("Enter product price"))
quantity = int(input("Enter product quantitiy"))
total_sales = price * quantity
print("Total sales is " + str(total_sales))

name = input("Customer_name")
price = int(input("prduct_price"))
product = input("product_name")
quantity = int(input("quantity_purchased"))
total_purchase = price * quantity 
print(f"{name} purchased {quantity} {product} units for a total of {total_purchase}")

Product = input("Product_name")
category = input("Category_name")
price = int(input("Product_price"))
stock = int(input("Product_stock"))
total_inventory_value = price * stock
print(Product)
print(category)
print(price)
print(stock)
print(total_inventory_value)

products = [
    {"name": "iPhone 16", "category": "Electronics", "price": 79999},
    {"name": "Nike Shoes", "category": "Fashion", "price": 5999},
    {"name": "Air Fryer", "category": "Home", "price": 8999}
]
for product in products:
    if product["name"] == "iPhone16":
        print(f"{product['name']} - {product['category']} - {product['price']}")
    if product["name"] == "Nike Shoes":
        print(f"{product['name']} - {product['category']} - {product['price']}")
    if product["name"] == "Air Fryer":
        print(f"{product['name']} - {product['category']} - {product['price']}")

    sales_data = [
    {"product": "iPhone 16", "price": 79999, "quantity": 2},
    {"product": "Nike Shoes", "price": 5999, "quantity": 5},
    {"product": "Air Fryer", "price": 8999, "quantity": 3}
]
for product in sales_data:
    if product["product"] == "iPhone16":
        sales = product["price"] * product["quantity"]
        print(f"{product['product']} - sales: {sales}")
    if product["product"] == "Nike Shoes":
        sales = product["price"] * product["quantity"]
        print(f"{product['product']} - sales: {sales}")
    if product["product"] == "Air Fryer":
        sales = product["price"] * product["quantity"]
        print(f"{product['product']} - sales: {sales}")

sales = [12500, 18500, 9200, 24500, 19800, 31000, 15700]
for sale in sales:
    if sale >= 24500:
       print(f"Highest_sales: {sale}")
    if sale <= 12500:
        print(f"Lowest_sales: {sale}")
    Total_sales = sum(sales)
    print(f"Total_sales: {Total_sales}")  
    Average_sales = Total_sales / len(sales)
    print(f"Average_sales: {Average_sales}") 

    sales = [12000, 15000, 18000, 21000, 25000]

i = 0

while i < len(sales):
    print(sales[i])
    i += 1

i = 0 
while i < 5 : 
    print(i)
    i += 1

sales = [12000, 15000, 18000, 21000, 25000]
i = 0 
while i < len(sales):
    print(sales[i])
    i += 1 

sales = [12000, 15000, 18000, 21000, 25000]

i = 0
high_sales_days = 0

while i < len(sales):

    if sales[i] >= 18000:
        print(sales[i])
        high_sales_days += 1

    i += 1
print("High Sales Days:", high_sales_days)

sales = [12000, 15000, 18000, 31000, 25000]

for sale in sales:
    print(sale)
if sale > 25000:
    print("Limit exceeded!")

sales = [12000, 15000, 18000, 21000, 25000]

for sale in sales:

    if sale < 18000:
        continue

    print("High Sale:", sale)      
try:
    price = int(input("Enter product price: "))
    print("Price:", price)

except ValueError:
    print("Please enter a valid number.")

sales = [12500, 15800, 13200, 18500, 21000, 9500, 24000]
for sale in sales :
    total_sales = sum(int(sale))
print(total_sales)

Average_sales = total_sales / sale
print(Average_sales)

Highest_sale = max(int(sale))
print(Highest_sale)

lowest_sale =  min(int(sale))
print(lowest_sale)

sales = [ 12500, 15800, 13200, 18500, 21000, 9500, 24000]

for i in range(7):
    sale = int(input(f"Enter sale {i + 1}: "))
    sales.append(sale)
Total_sales = sum(sales)
Average_sales = Total_sales / len(sales)
Highest_sale = max(sales)
Lowest_sale = min(sales)
if sales >= 15000:
    print("sale")
print(f'Total_Sales: {Total_sales}')
print(f'Average_sales: {Average_sales}')
print(f'Highest_sale: {Highest_sale}')
print(f'Lowest_sale: {Lowest_sale}')
