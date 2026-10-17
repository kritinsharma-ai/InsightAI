from pathlib import Path
import pandas as pd
PROJECT_ROOT = Path(__file__).resolve().parent.parent
DATA_DIR = PROJECT_ROOT / "02_data"


def generate_executive_report():
    product_path = DATA_DIR / "novamart_product_analysis.csv"
    category_path = DATA_DIR / "novamart_category_analysis.csv"
    insights_path = DATA_DIR / "novamart_business_insights.txt"

    products = pd.read_csv(product_path)
    categories = pd.read_csv(product_path)
    insights = insights_path.read_text (encoding = "utf=8")

    report = f"""
NOVAMART EXECUTIVE BUSINESS REPORT
==================================

PRODUCT PERFORMANCE 
--------------------
{products.to_string(index = False)}


CATEGORY PERFORMANCE 
{categories.to_string()}


BUSINESS INSIGHTS & RECOMMENDATIONS.
{insights}

Generated Automatically by INSIGHTSAI . 
"""

    report_path = DATA_DIR / "novamart_executive_report.txt"
    report_path.write_text(report,encoding = "utf=8")

    print(f"Executive report saved : {report_path}")
    return report_path

if __name__ == "__main__":
    generate_executive_report()





