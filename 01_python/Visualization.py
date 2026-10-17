from matplotlib.ticker import StrMethodFormatter
from pathlib import Path
import matplotlib.pyplot as plt

PROJECT_ROOT = Path(__file__).resolve().parent.parent
DATA_DIR = PROJECT_ROOT / "02_Data"
CHART_DIR = PROJECT_ROOT / "03_Visualizations"


def plot_project_revenue(data):
    CHART_DIR.mkdir(parents=True , exist_ok=True)

    product_data = data.sort_values("Revenue",ascending=False)

    plt.figure(figsize=(12,7))

    bars = plt.bar(product_data["Product"],product_data["Revenue"])

    # Highlight the highest and lowestrevenue product.
    bars[0].set_color("green")
    bars[-1].set_color("red")

    # Display revenue labels above the bars.
    plt.bar_label(bars,fmt="%.0f" , padding = 3)
    plt.bar_label(
    bars,
    fmt="₹%.0f",
    padding=3 )


    # Add each product revenue contribution percentage.
    
        

    # Calculate each product's share of total revenue.
    total_revenue = product_data["Revenue"].sum()

    product_data["Revenue_Percentage"] = ( product_data["Revenue"] / total_revenue )* 100

    print("\n ----------------- Product Revenue Contribution----------------")
    print(product_data[["Product","Revenue","Revenue_Percentage"]].round(2).to_string(index=False))


    # Add an average revenue reference line.
    average_revenue = product_data["Revenue"].mean()

    plt.axhline(y = average_revenue,linestyle ='--',label = f"Average Revenue:{average_revenue:,.0f}")
    plt.legend()

    total_revenue = product_data["Revenue"].sum()
    plt.title("Novamart Product Revenue Analysis - 2026\n"
              f"Total Revenue:,{total_revenue:,.0f}")

    plt.xlabel("Product")
    plt.ylabel("Revenue")
    plt.gca().yaxis.set_major_formatter(StrMethodFormatter("{x:,.0f}"))

    plt.grid(axis = "y",linestyle ='--',alpha =0.3 )
    plt.xticks(rotation=20)
    plt.tight_layout()

    chart_path = CHART_DIR / "product_revenue.png"
    plt.savefig(chart_path,dpi = 300 ,bbox_inches = "tight",facecolor = "white" )
    plt.close()

    print(f"Revenue Chart Saved : {chart_path}")
    plt.ylim(0,product_data["Revenue"].max() * 1.18)
    
def plot_category_revenue(data):
    CHART_DIR.mkdir(parents=True, exist_ok=True)

    category_data = (
        data.groupby("Category")["Revenue"]
        .sum()
        .sort_values(ascending=False)
    )

    plt.figure(figsize=(9, 6))

    bars = plt.bar(
        category_data.index,
        category_data.values
    )
    chart_path = CHART_DIR / "category_revenue.png"

    plt.savefig(
        chart_path,
        dpi=300,
        bbox_inches="tight",
        facecolor="white"
    )
    plt.close()

    print(f"Category revenue chart saved: {chart_path}")


if __name__ == "__main__":
    import pandas as pd

    data_path = DATA_DIR / "novamart_cleaned.csv"
    df = pd.read_csv(data_path)

    print("Dataset loaded successfully.")
    print(df[["Product", "Revenue"]])

    plot_project_revenue(df)
    plot_category_revenue(df)



    
    


