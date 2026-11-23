"""Fit a single-feature linear model with gradient descent.

Run from the repository root with:
    python ML/Supervised/LinearRegression/gradient_descent_linear_regression.py
"""

import numpy as np
from sklearn.metrics import mean_absolute_error, r2_score
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler


def main():
    # House sizes (square feet) and sale prices (thousands of dollars).
    sizes = np.array([650, 800, 950, 1100, 1250, 1400, 1550, 1700, 1850, 2000], dtype=float)
    prices = np.array([155, 180, 205, 225, 250, 275, 295, 325, 345, 375], dtype=float)
    features = sizes.reshape(-1, 1)

    x_train, x_test, y_train, y_test = train_test_split(
        features, prices, test_size=0.2, random_state=42
    )

    # Scaling keeps gradient descent steps stable. Fit only on training data.
    scaler = StandardScaler()
    x_train_scaled = scaler.fit_transform(x_train).ravel()
    x_test_scaled = scaler.transform(x_test).ravel()

    slope = 0.0
    intercept = 0.0
    learning_rate = 0.05
    epochs = 2_000
    sample_count = len(y_train)

    for _ in range(epochs):
        predictions = slope * x_train_scaled + intercept
        errors = predictions - y_train
        slope_gradient = (2 / sample_count) * np.dot(errors, x_train_scaled)
        intercept_gradient = (2 / sample_count) * errors.sum()
        slope -= learning_rate * slope_gradient
        intercept -= learning_rate * intercept_gradient

    predictions = slope * x_test_scaled + intercept
    price_per_sqft = slope / scaler.scale_[0] * 1000

    print("Linear Regression with Gradient Descent: House Prices")
    print(f"Estimated price change per square foot: ${price_per_sqft:.2f}")
    print(f"Mean absolute error: ${mean_absolute_error(y_test, predictions):.2f} thousand")
    print(f"R-squared: {r2_score(y_test, predictions):.3f}")
    print("\nTest predictions (thousands of dollars):")
    for actual, predicted in zip(y_test, predictions):
        print(f"Actual: ${actual:.1f}k | Predicted: ${predicted:.1f}k")


if __name__ == "__main__":
    main()
