import numpy as np

# Fit a simple line: prediction = weight*x + bias
x = np.array([1.0, 2.0, 3.0, 4.0])
y_true = np.array([3.0, 5.0, 7.0, 9.0])  # Underlying pattern: y = 2x + 1

weight = 0.5
bias = 0.0
learning_rate = 0.05

def predict(values, w, b):
    return w * values + b

def mean_squared_error(actual, predicted):
    return np.mean((actual - predicted) ** 2)

predicted = predict(x, weight, bias)
loss = mean_squared_error(y_true, predicted)
print("Initial predictions:", predicted)
print(f"Initial MSE loss: {loss:.4f}")

# Gradients of MSE for prediction = weight*x + bias
error = predicted - y_true
dw = (2 / len(x)) * np.sum(error * x)
db = (2 / len(x)) * np.sum(error)
print(f"Gradient for weight: {dw:.4f}")
print(f"Gradient for bias: {db:.4f}")

# Update parameters in the opposite direction of the gradient
weight -= learning_rate * dw
bias -= learning_rate * db

new_predicted = predict(x, weight, bias)
new_loss = mean_squared_error(y_true, new_predicted)
print("\nUpdated weight:", round(float(weight), 4))
print("Updated bias:", round(float(bias), 4))
print("Updated predictions:", np.round(new_predicted, 3))
print(f"Updated MSE loss: {new_loss:.4f}")
