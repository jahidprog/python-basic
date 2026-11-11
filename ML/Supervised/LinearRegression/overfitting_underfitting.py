"""Compare underfitting and overfitting with polynomial regression.

Run from the repository root with:
    python ML/Supervised/LinearRegression/overfitting_underfitting.py

Requires NumPy, Matplotlib, and scikit-learn.
"""

import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error
from sklearn.model_selection import train_test_split
from sklearn.pipeline import make_pipeline
from sklearn.preprocessing import PolynomialFeatures


def main():
    # The hidden pattern is curved, so a straight line is too simple.
    rng = np.random.default_rng(42)
    X = np.linspace(-3, 3, 40).reshape(-1, 1)
    y = np.sin(X[:, 0]) + rng.normal(0, 0.2, size=len(X))

    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.3, random_state=42
    )

    # Degree 1 is too simple; degree 4 captures the main pattern; degree 15
    # is flexible enough to chase noise in the training points.
    degrees = {"Underfitting (degree 1)": 1,
               "Reasonable fit (degree 4)": 4,
               "Overfitting (degree 15)": 15}
    x_curve = np.linspace(X.min(), X.max(), 300).reshape(-1, 1)

    fig, axes = plt.subplots(1, len(degrees), figsize=(15, 4), sharey=True)
    for axis, (label, degree) in zip(axes, degrees.items()):
        model = make_pipeline(PolynomialFeatures(degree), LinearRegression())
        model.fit(X_train, y_train)

        train_mse = mean_squared_error(y_train, model.predict(X_train))
        test_mse = mean_squared_error(y_test, model.predict(X_test))
        print(f"{label}: train MSE = {train_mse:.3f}, test MSE = {test_mse:.3f}")

        axis.scatter(X_train, y_train, color="tab:blue", label="Training data")
        axis.scatter(X_test, y_test, color="tab:orange", label="Test data")
        axis.plot(x_curve, model.predict(x_curve), color="tab:red", label="Model")
        axis.set_title(label)
        axis.set_xlabel("x")
        axis.grid(alpha=0.25)

    axes[0].set_ylabel("y")
    axes[-1].legend(loc="best")
    fig.suptitle("Model complexity: underfitting vs. overfitting")
    fig.tight_layout()
    plt.show()


if __name__ == "__main__":
    main()
