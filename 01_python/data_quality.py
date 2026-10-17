
import pandas as pd


def check_data_quality(data):
    missing_values = data.isnull().sum().sum()
    duplicate_rows = data.duplicated().sum()
    invalid_prices = (data["Price"] <= 0).sum()
    invalid_quantities = (data["Quantity"] <= 0).sum()

    expected_revenue = data["Price"] * data["Quantity"]
    revenue_matches = (data["Revenue"] == expected_revenue).all()

    quality_passed = (
        missing_values == 0
        and duplicate_rows == 0
        and invalid_prices == 0
        and invalid_quantities == 0
        and revenue_matches
    )

    print("\n========== DATA QUALITY CHECK ==========")
    print(f"Missing values: {missing_values}")
    print(f"Duplicate rows: {duplicate_rows}")
    print(f"Invalid prices: {invalid_prices}")
    print(f"Invalid quantities: {invalid_quantities}")
    print(f"Revenue calculations valid: {revenue_matches}")
    print(f"Overall status: {'PASS' if quality_passed else 'FAIL'}")
    print("========================================")

    return quality_passed

