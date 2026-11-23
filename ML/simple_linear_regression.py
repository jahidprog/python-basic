"""Fit and evaluate a single-feature linear regression model.

Run from the repository root with:
    python ML/Supervised/LinearRegression/simple_linear_regression.py
"""

import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_absolute_error, r2_score
from sklearn.model_selection import train_test_split


def main():
    # A small house-size dataset keeps this example self-contained.
    data = pd.DataFrame(
        {
            "size_sqft": [650, 800, 950, 1100, 1250, 1400, 1550, 1700, 1850, 2000],
            "price_thousands": [155, 180, 205, 225, 250, 275, 295, 325, 345, 375],
        }
    )
    features = data[["size_sqft"]]
    target = data["price_thousands"]

    features_train, features_test, target_train, target_test = train_test_split(
        features, target, test_size=0.2, random_state=42
    )

    model = LinearRegression()
    model.fit(features_train, target_train)
    predictions = model.predict(features_test)

    print("Simple Linear Regression: House Prices")
    print(f"Intercept: ${model.intercept_:.2f} thousand")
    print(f"Price change per square foot: ${model.coef_[0] * 1000:.2f}")
    print(f"Mean absolute error: ${mean_absolute_error(target_test, predictions):.2f} thousand")
    print(f"R-squared: {r2_score(target_test, predictions):.3f}")

    results = pd.DataFrame(
        {"actual_price_thousands": target_test, "predicted_price_thousands": predictions},
        index=target_test.index,
    )
    print("\nTest predictions:")
    print(results.sort_index().round(2).to_string())


if __name__ == "__main__":
    main()
