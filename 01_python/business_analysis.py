
def analyze_product_performance(data):
    result = data.copy()

    result["Revenue_Rank"] = (
        result["Revenue"]
        .rank(ascending=False, method="dense")
        .astype(int)
    )

    result["Quantity_Rank"] = (
        result["Quantity"]
        .rank(ascending=False, method="dense")
        .astype(int)
    )

    result["Revenue_Percentage"] = (
        result["Revenue"] / result["Revenue"].sum()
    ) * 100

    return result.sort_values("Revenue", ascending=False)


def analyze_category_performance(data):
    result = data.groupby("Category").agg(
        Total_Revenue=("Revenue", "sum"),
        Total_Units_Sold=("Quantity", "sum"),
        Number_of_Products=("Product", "nunique")
    )

    result["Revenue_Contribution_Percent"] = (
        result["Total_Revenue"]
        / result["Total_Revenue"].sum()
    ) * 100

    return result.sort_values("Total_Revenue", ascending=False)

