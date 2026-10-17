
from pathlib import Path

import pandas as pd

from data_quality import check_data_quality
from business_analysis import (
    analyze_product_performance,
    analyze_category_performance,
)
from reporting import export_report, export_text_report
from pipeline_logging import logger
from datetime import datetime
from time import perf_counter
from Visualization import (plot_project_revenue , 
                            plot_category_revenue,)
from executive_report import generate_executive_report 

def generate_business_insights(data):
    total_revenue = data["Revenue"].sum()
    total_units = data["Quantity"].sum()

    product_revenue = data.groupby("Product")["Revenue"].sum()
    top_product = product_revenue.idxmax()
    top_product_revenue = product_revenue.max()

    lowest_product = product_revenue.idxmin()
    lowest_product_revenue = product_revenue.min()

    category_revenue = data.groupby("Category")["Revenue"].sum()
    top_category = category_revenue.idxmax()
    top_category_revenue = category_revenue.max()

    insights = f"""
INSIGHTAI — NOVAMART BUSINESS INSIGHTS
=====================================

Total Revenue: ₹{total_revenue:,.0f}
Total Units Sold: {total_units}

Top Product: {top_product} — ₹{top_product_revenue:,.0f}
Lowest-Revenue Product: {lowest_product} — ₹{lowest_product_revenue:,.0f}
Top Category: {top_category} — ₹{top_category_revenue:,.0f}

Business Recommendations
------------------------
1. Investigate what drives {top_product}'s strong revenue performance.
2. Review pricing, demand, and marketing for {lowest_product}.
3. Prioritize profitable opportunities within the {top_category} category.

Note: Revenue alone does not establish product profitability.
"""

    return insights

def main():
    start_time = perf_counter()
    run_started_at = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    logger.info("InsightAI pipeline started.")
    logger.info("Run started at: %s", run_started_at)

    data_path = (
        Path(__file__).resolve().parent.parent
        / "02_Data"
        / "novamart_cleaned.csv"
    )

    try:
        data = pd.read_csv(data_path)
        logger.info("Dataset rows: %s", data.shape[0])
        logger.info("Dataset columns: %s", data.shape[1])
        logger.info("Cleaned dataset loaded: %s", data_path.name)

        quality_passed = check_data_quality(data)

        if not quality_passed:
            logger.error("Data quality validation failed. Pipeline stopped.")
            return

        logger.info("Data quality validation passed.")

        product_results = analyze_product_performance(data)
        logger.info("Product analysis completed.")

        category_results = analyze_category_performance(data)
        logger.info("Category analysis completed.")

        
        # Generate and save business insights
        insights_text = generate_business_insights(data)

        export_text_report(
            insights_text,
            "novamart_business_insights.txt"
        )
        


        logger.info("Business insights report generated.")

        plot_project_revenue(data)
        plot_category_revenue(data)

        logger.info("Product and category charts generated.")

        export_report(
            product_results,
            "novamart_product_analysis.csv",
        )

        export_report(
            category_results,
            "novamart_category_analysis.csv",
            index=True,
        )

        # generate the consolidated executive report
        generate_executive_report()
        logger.info("Executive Report Generated Successfully.")


        logger.info("Analysis reports exported successfully.")
        logger.info("InsightAI pipeline completed successfully.")
        elapsed_seconds = perf_counter() - start_time
        logger.info("Pipeline duration: %.2f seconds", elapsed_seconds)
        logger.info("InsightAI pipeline completed successfully.")
    
    except Exception:
        logger.exception("Pipeline failed because of an unexpected error.")
        raise



if __name__ == "__main__":
    main()
  

