
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
