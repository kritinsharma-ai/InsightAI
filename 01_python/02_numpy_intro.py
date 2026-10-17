
import numpy as np
sales = [ 12500, 15800, 13200, 18500, 21000, 9500, 24000]
print("Sales:", sales)
print("Total_sales:", np.sum(sales))
print("Average_sales:", np.mean(sales))
print("Highest_sale:", np.max)
print("Lowest_sale:", np.sum)

sales = np.array([12000, 15000, 18000, 21000, 25000])
increased_sales = sales + 1000
print("Original sales:", sales)
print("Increased sales:", increased_sales)
print("Sales_Doubled", sales*2)
print("Sales After 10% Increase", sales * 1.10)


sales = np.array([ 12500, 15800, 13200, 18500, 21000, 9500, 24000 ])
high_sales = sales[sales >= 18000 ] 
print("High_Sales:" ,high_sales )

