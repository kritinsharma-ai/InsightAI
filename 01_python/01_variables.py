
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