
import numpy as np
import pandas as pd 
from datetime import datetime 

from data_quality import check_data_quality

from business_analysis import (
    analyze_product_performance,
    analyze_category_performance
)

from reporting import export_report

data = {
    "Product": ["Laptop", "Phone", "Shoes", "Headphones", "Watch"],
    "Category": ["Electronics", "Electronics", "Fashion", "Electronics", "Fashion"],
    "Price": [50000, 30000, 3000, 5000, 4000],
    "Quantity": [2, 3, 5, 4, 2]
}

df = pd.DataFrame(data)

print(df)

# NovaMart revenue for five days, in rupees
daily_sales = np.array([1200, 1800, 1500, 2200, 2500])
print("Daily sales:", daily_sales)
print("Total sales:", np.sum(daily_sales))
print("Average daily sales:", np.mean(daily_sales))
print("Highest daily revenue:", np.max(daily_sales))
print("Lowest daily revenue:", np.min(daily_sales))
print("Revenue range:", np.max(daily_sales) - np.min(daily_sales))
high_sales = daily_sales[daily_sales > 1800]
print("Days with sales above 1800:", high_sales)
print("Number of high sales days:", len(high_sales))
high_sales_percentage = (len(high_sales) / len(daily_sales)) * 100
print("high sales days percentage ", high_sales_percentage, "%")
print("Revenue from high sales days:", np.sum(high_sales))
high_sales_revenue_percentage = (np.sum(high_sales) / np.sum(daily_sales)) * 100
print("High sales revenue percentage:", round(high_sales_revenue_percentage, 2), "%")
low_sales = daily_sales[daily_sales < 1500]
print("Days with sales below 1500:", low_sales)
print("Revenue from low sales days:", np.sum(low_sales))
low_sales_percentage = (len(low_sales) / len(daily_sales)) * 100
print("Low sales days percentage:", low_sales_percentage, "%")


print(df.shape)
print(df.columns)
print(df.dtypes)
print(df.head())
print(df.describe())
df[ "Revenue"] = df["Price"] * df["Quantity"]
print(df)
print("Total Revenue:", df["Revenue"].sum())
print(df.loc[df["Revenue"].idxmax()])
print(df.loc[df["Revenue"].idxmin()])
print("Average Revenue per product:", df["Revenue"].mean())
print(df.groupby("Category")["Revenue"].sum())
category_revenue = df.groupby("Category")["Revenue"].sum()
print("Best performing category:", category_revenue.idxmax())
category_revenue_percentage = (category_revenue / df["Revenue"].sum()) * 100
print("Rvenue percentage by category:")
print(category_revenue_percentage)

sorted_products = df.sort_values("Revenue", ascending = False)
print(sorted_products["Product"] , ["Revenue"])
print("Total units sold:", df["Quantity"].sum())
print(df.loc[df["Quantity"].idxmax()])

df["Revenue_per_Unit "] = df["Revenue"] / df["Quantity"]
print(df[["Product", "Revenue_per_Unit "]])

print(df.loc[df["Revenue_per_Unit "].idxmax()])

high_revenue_products = df[df["Revenue"] > 20000]
print(high_revenue_products[["Product", "Revenue"]])

electronics_high_revenue = df[(df["Category"] == "Electronics") & (df["Revenue"] > 20000)]
print(electronics_high_revenue[["Product", "Revenue"]])

print("High-revenue electronics products:", len(electronics_high_revenue))

electronics = df[df["Category"] == "Electronics"]
print("Average Electronics Revenue:", electronics["Revenue"].mean())

average_category_revenue = df.groupby("Category")["Revenue"].mean()
print("Average revenue by category:")
print(average_category_revenue)

print("Most expensive product:")
print(df.loc[df["Price"].idxmax(), ["Product", "Price"]])

print("Cheapest Product:")
print(df.loc[df["Price"].idxmin(),["Product","Price"]])

product_revenue = df[["Product" , "Revenue"]].sort_values("Revenue" , ascending=False)
print("Product revenue ranking:")
print(product_revenue)

df["Revenue_Percentage"] = (df["Revenue"] / df["Revenue"].sum()) * 100
print(df[["Product","Revenue","Revenue_Percentage"]])

print("Missing values:")
print(df.isnull().sum())

print("Duplicate rows:", df.duplicated().sum())

print("Dataset Information:")
df.info()

data = {
    "Product": ["Laptop", "Phone", "Shoes", "Headphones", "Watch"],
    "Category": ["Electronics", "Electronics", "Fashion", "Electronics", "Fashion"],
    "Price": [50000, 30000, None, 5000, 4000],
    "Quantity": [2, 3, 5, 4, 2]
}
df = pd.DataFrame(data)
print(df.isnull().sum())
print("Rows with missing price:")
print(df[df["Price"].isnull()])

median_price = df["Price"].median()
print("Median_price:", median_price)

df["Price"] = df["Price"].fillna(median_price)
print("Price after filling missing value:")
print(df[["Product", "Price"]])

print("Missing value after cleaning:")
print(df.isnull().sum())

df["Revenue"] = df["Price"] * df["Quantity"]
print(df[["Product", "Price", "Quantity", "Revenue"]])

df["Revenue_Per_Unit"] = df["Revenue"] / df["Quantity"]
df["Revenue_Percentage"] = (df["Revenue"] / df["Revenue"].sum()) * 100
print("Updated Dependent Matrix:")
print(df[["Product", "Revenue", "Revenue_Per_Unit", "Revenue_Percentage"]])

df = pd.concat([df, df.iloc[[1]]], ignore_index = True)

print("Data after adding duplicate:")
print(df)

print("Number of Duplicate Rows:", df.duplicated().sum())

df = df.drop_duplicates()

print("Data after removing duplicates:")
print(df)

print("Duplicate rows remaining:", df.duplicated().sum())

print("Invalid Prices:")
print(df[df["Price"] <= 0])

print("Invalid Quantities:")
print(df[df["Quantity"] <= 0])

print("Data Quality Summary:")
print("Total Rows:", len(df))
print("Total Columns:", len(df.columns))
print("Missing Values:", df.isnull().sum().sum())
print("Duplicate Rows:", df.duplicated().sum())
print("Invalid Prices:", (df["Price"] <= 0).sum())
print("Invalid Quantities:", (df["Quantity"] <= 0).sum())

df.to_csv("../02_Data/novamart_cleaned.csv", index=False)

print("Cleaned dataset saved successfully.")


cleaned_df = pd.read_csv("../02_Data/novamart_cleaned.csv")

print("Cleaned dataset loaded from CSV:")
print(cleaned_df)

      
print("Loaded dataset shape:", cleaned_df.shape)
print("Loaded dataset columns:")
print(cleaned_df.columns)


print("Data types:")
print(cleaned_df.dtypes)


print("Numerical summary:")
print(cleaned_df.describe())

print("Products by category:")
print(cleaned_df["Category"].value_counts())

category_counts = cleaned_df["Category"].value_counts()

print("Most Common Category:", category_counts.idxmax())
print("Number of product in that Category:", category_counts.max())

category_revenue = cleaned_df.groupby("Category")["Revenue"].sum()
print("Revenue by category:")
print(category_revenue)

best_category = category_revenue.idxmax()
best_category_revenue = category_revenue.max()

print("Best performing category:", best_category)
print("revenue:", best_category_revenue)

category_revenue_percentage = (category_revenue / cleaned_df["Revenue"].sum()) * 100
print("Revenue Contribution by category:")
print(category_revenue_percentage)

top_quantity_product = cleaned_df.loc[cleaned_df["Quantity"].idxmax()]
print("Top selling product by quantity:") 
print(top_quantity_product["Product"])

top_revenue_product = cleaned_df.loc[cleaned_df["Revenue"].idxmax()]
print("Top product by revenue:")
print(top_revenue_product["Product"])


highest_revenue_per_unit = cleaned_df.loc[cleaned_df["Revenue_Per_Unit"].idxmax()]
print("Highest revenue per unit:")
print(highest_revenue_per_unit[["Product","Revenue_Per_Unit"]])


product_performance = cleaned_df[["Product", "Quantity", "Revenue", "Revenue_Per_Unit"]].sort_values(("Revenue"), ascending = False)
print("Product performance")
print(product_performance)




total_revenue = cleaned_df["Revenue"].sum()
total_units = cleaned_df["Quantity"].sum()
print("Total Revenue:" , total_revenue)
print("Total Units sold:" , total_units)


average_revenue_per_unit = total_revenue / total_units
print("Average Revenue per Unit:", average_revenue_per_unit)


average_price = cleaned_df["Price"].mean()
print("Average Price:", average_price)


median_price = cleaned_df["Price"].median()
print("Median Price:", median_price)


price_range = cleaned_df["Price"].max() - cleaned_df["Price"].mean()
print("Price Range:", price_range)


revenue_range = cleaned_df["Revenue"].max() - cleaned_df["Revenue"].min()
print("Revenue Range:", revenue_range)


revenue_std = cleaned_df["Revenue"].std() 
print("Revenue Standard Deviation:", revenue_std)


median_revenue = cleaned_df["Revenue"].median()
print("Median Revenue:", median_revenue)


median_quantity = cleaned_df["Quantity"].median()
print("Median Quantity:", median_quantity)



# Calculate the correlation between Price and Quantity
price_quantity_correlation = cleaned_df["Price"].corr(cleaned_df["Quantity"])
print("Price Quantity Correlation:", price_quantity_correlation)

# Check Revenue vs Quantity
revenue_quantity_correlation = cleaned_df["Revenue"].corr(cleaned_df["Quantity"])
print("Revenue Quantity Correlation:", revenue_quantity_correlation)


# Calculate Revenue vs Price correlation
revenue_price_correlation = cleaned_df["Revenue"].corr(cleaned_df["Price"])
print("Revenue Price Correlation:", revenue_price_correlation)



# Create a simple business insight
print("\n --- Business Insight ---")


print(f"{best_category} is the highest revenue category"
f"with{best_category_revenue:,.0f} in revenue." )

print(f"{top_revenue_product["Product"]} is the top product by revenue "
f"with{top_revenue_product["Revenue"]:,.0f}.")

print(
    f"{top_quantity_product['Product']} sells the highest number of units "
    f"with {top_quantity_product['Quantity']} units."
)


# Calculate each product's revenue contribution
cleaned_df["Product_Revenue_Percentage"] = (cleaned_df["Revenue"] / cleaned_df["Revenue"].sum() * 100) 
print("Product Revenue Contribution:")
print(cleaned_df[["Product" , "Revenue" , "Product_Revenue_Percentage"]].sort_values("Product_Revenue_Percentage", ascending = False ))


# Identify the top 2 revenue contributors
top_2_Revenue_products = cleaned_df[["Product", "Revenue", "Product_Revenue_Percentage"]].sort_values("Revenue", ascending = False ).head(2)

print("Top 2 Revenue Contributing Products:")
print(top_2_Revenue_products)


# Calculate the combined revenue of the top 2 products
top_2_revenue = top_2_Revenue_products["Revenue"].sum()
top_2_revenue_percentage = ( top_2_revenue / cleaned_df["Revenue"].sum()) * 100
print("Top 2 products revenue:", top_2_revenue)
print("Top 2 products revenue contribution:", top_2_revenue_percentage )


# Calculate revenue concentration
remaining_revenue = cleaned_df["Revenue"].sum() - top_2_revenue
remaining_revenue_percentage = ( remaining_revenue / cleaned_df["Revenue"].sum()) * 100
print("Remaining Products Revenue:",remaining_revenue)
print("Remaining Products Revenue Contribution:",remaining_revenue_percentage)


# Identify the lowest-revenue product
lowest_revenue_product = cleaned_df.loc[cleaned_df["Revenue"].idxmin ()]
print("\n --- Lowest Revenue Product ---")
print(lowest_revenue_product[["Product","Revenue"]])


# calculate the bottom 2 products by revenue
bottom_2_products = cleaned_df[["Product","Revenue"]].sort_values("Revenue", ascending = True ).head(2)
print("\n--- Bottom 2 Products by Revenue ---")
print(bottom_2_products)


# Calculate the combined revenue of the bottom 2 products
bottom_2_revenue = bottom_2_products["Revenue"].sum()

bottom_2_percentage = ( bottom_2_revenue / cleaned_df["Revenue"].sum()) * 100
print("\n --- Bottom two products revenue analysis ---")
print("Combined Revenue :", bottom_2_revenue)
print("Contibution to total revenue :", round(bottom_2_percentage , 2),"%" )


# Calculate the revenue contribution of the top 3 products
top_3_products = cleaned_df[["Product","Revenue"]].sort_values(("Revenue"), ascending = False).head(3)
top_3_revenue = top_3_products["Revenue"].sum()

top_3_percentage = ( top_3_revenue / cleaned_df["Revenue"].sum() ) * 100

print("\n--- Top 3 Products Revenue Analysis --- ")
print(top_3_products)
print("Combined Revenue :" , top_3_revenue)
print("Revenue Contribution :" , round(top_3_percentage, 2),"%" )


# Compare the top 3 products with the remaining products
other_products_revenue = (cleaned_df["Revenue"].sum() - top_3_revenue)
other_products_percentage = (other_products_revenue / cleaned_df["Revenue"].sum()) * 100
print("\n --- Top 3 vs Remaining Products --- ")
print("Top 3 products revenue :" , top_3_revenue)
print("Top 3 contribution :" , round(top_3_percentage,2) ,"%" )
print("Remaining Products Revenue:", other_products_revenue)
print("Remaining Products contribution:", other_products_percentage)


# Calculate each product's revenue rank
cleaned_df["Revenue_Rank"] = cleaned_df["Revenue"].rank(ascending = False , method = "dense" ).astype(int)

print("\n--- Product Revenue Ranking ---")
print(cleaned_df[["Product","Revenue","Revenue_Rank",]].sort_values("Revenue_Rank"))


# Calculate quantity rank
cleaned_df["Quantity_Rank"] = cleaned_df["Quantity"].rank(ascending = False , method = "dense").astype(int)

print("\n --- Quantity ranking ---")
print(cleaned_df[["Product","Quantity","Quantity_Rank" ]].sort_values("Quantity_Rank"))


# identify products that rank in the top 3 by revenue

cleaned_df["Top_3_Revenue_Product"] = (
    cleaned_df["Revenue_Rank"] <= 3
)

print("\n--- Top 3 Revenue Product Flag ---")
print(
    cleaned_df[
        ["Product", "Revenue", "Revenue_Rank", "Top_3_Revenue_Product"]
    ].sort_values("Revenue_Rank")
)


# Filter the top 3 products into a separate table

top_3_revenue_table = cleaned_df[cleaned_df["Top_3_Revenue_Product"]][["Product","Revenue","Quantity" ,"Revenue_Rank"]].sort_values("Revenue_Rank")
print("\n --- Top 3 Revenue Products ---")
print(top_3_revenue_table)


# Create a business KPI summary.
print("\n==== Novamart KPI Summary ====")
print(f"Total Revenue:{cleaned_df["Revenue"].sum():,.0f}")
print(f"Total Units Sold:{cleaned_df["Quantity"].sum():,.0f}")
print(f"Number of Products:{cleaned_df["Product"].nunique()}")
print(f"Highest Revenue Product:{top_revenue_product["Product"]}")
print(f"Lowest Revenue Product:{lowest_revenue_product["Product"]}")
print(f"Best Revenue Category:{best_category}")

print("==================================")



# Save KPI Summary.


# Add total revenue contribution validation
total_revenue_contribution = cleaned_df["Product_Revenue_Percentage"].sum()

print("\n --- Revenue Contribution Validation ---")
print( "Total product revenue contribution : ", round(total_revenue_contribution ,2),"%" )


# Validate the total revenue.
calculated_total_revenue = cleaned_df["Revenue"].sum()
expected_total_revenue = 320500

print("\n ---- Total Revenue Validation ----")
print("Calculated Revenue :", calculated_total_revenue)
print("Expected Revenue :", expected_total_revenue)
print("Revenue Matches :", calculated_total_revenue == expected_total_revenue)


# Validate that revenue equals Price × Quantity.
expected_product_revenue = cleaned_df["Price"] * cleaned_df["Quantity"]

revenue_check = cleaned_df["Revenue"] == expected_product_revenue

print("\n ---- Product Revenue Validation ---")
print("Revenue Correct For Every Product :" , revenue_check.all())
print("\n ---- Products With Incorrect Revenue :" )
print(cleaned_df.loc[~revenue_check, [ "Product" , "Price" , "Quantity" , "Revenue" ]] )


# Create a single overall data-quality status . 
data_quality_passed = (cleaned_df.isnull().sum().sum() == 0 
and cleaned_df.duplicated().sum() == 0 
and (cleaned_df["Price"] > 0).all()
and (cleaned_df["Quantity"] > 0).all()
and revenue_check.all())

print("\n ---- Overall Data Quality Checks----")
if data_quality_passed :
    print("PASS : All Data Quality Checks Succeded")
else :
    print("Fail : One Or More Data Quality Checks Needs Attention")


# Save the data quality status checks in variable.
print("PASS: All Data Quality Checks Succeeded.") 
if data_quality_passed : 
    quality_status = "Pass"
else : 
    quality_status = "Fail"
print("\n ---- Overall Data Quality Status ----")
print("Status :", quality_status )



# Add the quality status to your KPI report . 

kpi_report = f"""
========== NOVAMART KPI SUMMARY ==========

Business Performance Report
Data Quality Status: {quality_status}
Total Revenue: ₹{cleaned_df['Revenue'].sum():,.0f}
Total Units Sold: {cleaned_df['Quantity'].sum():,.0f}
Number of Products: {cleaned_df['Product'].nunique()}
Highest Revenue Product: {top_revenue_product['Product']}
Lowest Revenue Product: {lowest_revenue_product['Product']}
Best Revenue Category: {best_category}


==========================================
"""
import os

print("Report file path:", os.path.abspath("../02_Data/novamart_kpi_report.txt"))
print(kpi_report)
print("Status line present:", f"Data Quality Status: {quality_status}" in kpi_report)
print("Actual quality status:", repr(quality_status))
print("Report contains status label:", "Data Quality Status:" in kpi_report)
with open("../02_Data/novamart_kpi_report.txt", "w", encoding="utf-8") as file:
    file.write(kpi_report)
print("Saved report contains status:", "Data Quality Status:" in kpi_report)
print("KPI report saved successfully.")
print("Report generated by:", __file__)


# Create a category performance table . 
category_performance = cleaned_df.groupby("Category").agg(Total_Revenue=("Revenue","sum") , Total_Units_Sold =("Quantity","sum") , Number_of_Products = ("Product","nunique")).sort_values("Total_Revenue" , ascending = False)
print("\n ----- Category Performance Report -----")
print(category_performance)


# Identify the highest-revenue category automatically.
best_category_row = category_performance.iloc[0]
print("\n ----- Best Category Summary -----")
print("Best Category :", category_performance.index[0])
print("Total Revenue :", best_category_row["Total_Revenue"])
print("Units Sold :", best_category_row["Total_Units_Sold"])
print("Number Of Products :", best_category_row["Number_of_Products"])


# Calculate each category's share of total revenue . 
category_performance["Revenue_Contribution_Percent"] = ( category_performance["Total_Revenue"] / category_performance["Total_Revenue"].sum() ) * 100
print("\n ---- Category Revenue Contribution ----")
print(category_performance[["Total_Revenue","Revenue_Contribution_Percent"]].round(2))


# Add a performance label to each category . 
category_performance["Performance_Label"] = category_performance["Revenue_Contribution_Percent"].apply(lambda percentage: ("High_Contribution" if percentage >= 50 else "Low_Contribution"))
print("\n ---- Category Performance Labels ----")
print(category_performance[["Total_Revenue","Revenue_Contribution_Percent","Performance_Label"]].round(2))

# Save the category performance table to CSV.
category_performance.to_csv("../02_Data/novamart_category_performance.csv",index = True )
print(" Category Performance Report Saved Successfully")


#  Save category insights to a text report.
category_report = f""""  
============== NOVAMART CATEGORY REPORT ============

Category Performance Summary 

Best Revenue Category : {category_performance.index[0]}

Total Category Revenue : 
{category_performance["Total_Revenue"].sum():,.0f}

Category Performance Details:
{category_performance.to_string()}


===================================================================
"""

with open("../02_Data/novamart_category_report.txt","w" , encoding = "utf-8") as file : file.write(category_report)
print("Category Report Saved Successfully ")


# Create a reusable business insights report.
total_revenue = cleaned_df["Revenue"].sum()
total_units = cleaned_df["Quantity"].sum()

top_product = cleaned_df.loc[cleaned_df["Revenue"].idxmax()]
lowest_product = cleaned_df.loc[cleaned_df["Revenue"].idxmin()]

best_category = category_performance.index[0]

business_insights = f"""
========================= NOVAMART BUSINESS INSIGHTS ==============================

1. Overall Performance
Novamart Total Revenue {total_revenue:,.0f}
in revenue and sold {total_units} units.

2. Best Selling Revenue Product
{top_product["Product"]}generated
{top_product["Revenue"]:,.0f}in revenue.

3. Lowest Revenue Product
{lowest_product["Product"]}generated
{lowest_product["Revenue"]:,.0f}in revenue .

4. Leading Revenue Category
{best_category}is leading category by Total Revenue.

5. Business Recommendation.
Review the performance , pricing , and demand for lower-revenue product before deciding whether to change pricing or marketing.



========================================================================================================================================
"""

with open("../02_data/novamart_business_insights.txt",
"w", 
encoding = "utf-8")as file:
         file.write(business_insights)


print("Business Insights Report Saved Successfully")


# Add automated product recommendations.

def recommend_action(row):
     if row ["Revenue_Rank"] == 1:
          return "Protect Performance and monitor Demand"
     elif row["Revenue_Rank"] <= 3:
          return "Monitor Sales and explore Growth"
     else:
          return "Investigate pricing", "demand" , "marketing"
cleaned_df["Recommended_Action"] = cleaned_df.apply(recommend_action , axis = 1 )

recommendation_report = cleaned_df[["Product","Revenue","Revenue_Rank", "Recommended_Action"]].sort_values("Revenue_Rank")

print("\n ------- Product Recommendations ------------")
print(recommendation_report.to_string(index = False))

recommendation_report.to_csv("../02_data/novamart_product_recommendations.csv",index=False)

print("\n Product Recommendations Saved Successfully")


# Create a consolidated product performance report.
product_dashboard = cleaned_df[
                  ["Product",
                   "Category",
                    "Price",
                    "Quantity",
                    "Revenue",
                    "Revenue_Percentage",
                    "Revenue_Rank",
                    "Quantity_Rank",
                    "Recommended_Action"   ]].sort_values("Revenue",ascending = False)

print("\n ---------------- NOVAMART PRODUCT DASHBOARD -----------------")
print(product_dashboard.round(2).to_string(index=False))
product_dashboard.to_csv("../02_Data/novamart_product_dashboard.csv",index=False)

print("\n Product Dashboard Saved Successfully.")



# Reusable business summary function

def generate_business_summary(data):
    total_revenue = data["Revenue"].sum()
    total_units = data["Quantity"].sum()
    total_products = data["Product"].nunique()
    average_revenue = data["Revenue"].mean()

    print("\n========== BUSINESS SUMMARY ==========")
    print(f"Total revenue: ₹{total_revenue:,.0f}")
    print(f"Total units sold: {total_units}")
    print(f"Unique products: {total_products}")
    print(f"Average revenue per product: ₹{average_revenue:,.2f}")
    print("======================================")

    return {
        "total_revenue": total_revenue,
        "total_units": total_units,
        "total_products": total_products,
        "average_revenue": average_revenue
    }


summary = generate_business_summary(cleaned_df)


# Reusable data quality function.


quality_passed = check_data_quality(cleaned_df)



# Reusable product performance function

product_analysis = analyze_product_performance(cleaned_df)


   
# Reusable category performance function

category_analysis = analyze_category_performance(cleaned_df)
   


# Reusable CSV report exporter



# Export the latest analysis results
export_report(
    product_analysis,
    "novamart_product_analysis.csv"
)

export_report(
    category_analysis,
    "novamart_category_analysis.csv"
)



# Main application entry point

def main():
    print("\nStarting InsightAI — NovaMart Analytics")
    print("========================================")

    summary = generate_business_summary(cleaned_df)
    quality_passed = check_data_quality(cleaned_df)
    product_results = analyze_product_performance(cleaned_df)
    category_results = analyze_category_performance(cleaned_df)

    export_report(
        product_results,
        "novamart_product_analysis.csv"
    )

    export_report(
        category_results,
        "novamart_category_analysis.csv"
    )

    print("\n========== PIPELINE SUMMARY ==========")
    print("Total revenue:", f"₹{summary['total_revenue']:,.0f}")
    print("Data quality:", "PASS" if quality_passed else "FAIL")
    print("Product analysis: Complete")
    print("Category analysis: Complete")
    print("======================================")


if __name__ == "__main__":
    main()


                                   
     

     
     












                                                          



