
from pathlib import Path

PROJECT_ROOT = Path(__file__).resolve().parent.parent
DATA_DIR = PROJECT_ROOT / "02_Data"
OUTPUT_FILE = DATA_DIR / "novamart_eda_recommendations.txt"

recommendations = """
INSIGHTAI — NOVAMART BUSINESS RECOMMENDATIONS
=============================================

1. PROTECT THE ELECTRONICS REVENUE BASE
Electronics generated the largest share of net revenue in this
simulated dataset. Monitor stock availability, product margins,
returns, and supplier costs before increasing investment.

2. DEVELOP A HEADPHONES SALES STRATEGY
Headphones led product unit sales in the analysis. Test suitable
bundles and complementary offers, and compare conversion rates
and profit margins before scaling promotions.

3. INVESTIGATE REGIONAL DIFFERENCES
Central led regional net revenue, while South sold the most units
but generated the lowest regional net revenue. Compare product
mix, average selling price, and discount rates by region.

4. INVESTIGATE MONTHLY PERFORMANCE
July was the strongest month, with net revenue of Rs. 1,787,525.
March was the weakest, with net revenue of Rs. 1,028,605.
Compare order counts, units sold, product mix, and discounts
to identify what explains this difference.

5. MONITOR DISCOUNT EFFECTIVENESS
Compare discounted and non-discounted orders. Evaluate whether
discounts increase units sold enough to justify the revenue given
up, and include product costs before judging profitability.

6. IMPROVE FUTURE ANALYSIS
Add product costs, returns, customer identifiers, and order status
when suitable data becomes available. These fields would support
profit analysis, repeat-purchase analysis, and return-rate tracking.

IMPORTANT LIMITATION
These findings use simulated order data created for learning.
They demonstrate an analytical workflow and do not establish
real-world customer behavior or actual market seasonality.
"""

OUTPUT_FILE.write_text(recommendations.strip() + "\n", encoding="utf-8")

print("Business recommendations report created.")
print("Saved to:", OUTPUT_FILE)

