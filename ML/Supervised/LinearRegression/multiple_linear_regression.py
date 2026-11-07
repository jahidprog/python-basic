"""Predict insurance charges with multiple linear regression.

Run from any directory with:
    python ML/Supervised/LinearRegression/multiple_linear_regression.py
"""

from pathlib import Path

import pandas as pd
from sklearn.compose import ColumnTransformer
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score
from sklearn.model_selection import train_test_split
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import OneHotEncoder


DATA_PATH = Path(__file__).with_name("insurance.csv")
TARGET = "charges"


def main():
    data = pd.read_csv(DATA_PATH)
    features = data.drop(columns=TARGET)
    target = data[TARGET]

    categorical_columns = features.select_dtypes(include="object").columns.tolist()
    numeric_columns = features.select_dtypes(exclude="object").columns.tolist()

    preprocessing = ColumnTransformer(
        transformers=[
            ("categorical", OneHotEncoder(handle_unknown="ignore"), categorical_columns),
            ("numeric", "passthrough", numeric_columns),
        ]
    )
    model = Pipeline(
        steps=[
            ("preprocessing", preprocessing),
            ("regression", LinearRegression()),
        ]
    )

    features_train, features_test, target_train, target_test = train_test_split(
        features, target, test_size=0.2, random_state=42
    )
    model.fit(features_train, target_train)
    predictions = model.predict(features_test)

    print("Multiple Linear Regression: Insurance Charges")
    print(f"Mean absolute error: ${mean_absolute_error(target_test, predictions):,.2f}")
    print(f"Root mean squared error: ${mean_squared_error(target_test, predictions) ** 0.5:,.2f}")
    print(f"R-squared: {r2_score(target_test, predictions):.3f}")

    comparison = pd.DataFrame(
        {"actual_charges": target_test, "predicted_charges": predictions},
        index=target_test.index,
    )
    print("\nFirst five test predictions:")
    print(comparison.head().round(2).to_string())


if __name__ == "__main__":
    main()
