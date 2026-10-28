"""
Dataset: MPG (Miles Per Gallon)
Goal: Investigate fuel efficiency and vehicle characteristics.
Plots: Scatter / Relational / Bar
"""
import seaborn as sns
import matplotlib.pyplot as plt

# Load dataset
df = sns.load_dataset("mpg")
print("MPG Dataset Head:")
print(df.head())

# Plot 1: Horsepower vs MPG by Origin
plt.figure(figsize=(8, 5))
sns.scatterplot(data=df, x="horsepower", y="mpg", hue="origin", style="cylinders", s=80)
plt.title("MPG: Horsepower vs Fuel Efficiency (MPG)")
plt.xlabel("Horsepower")
plt.ylabel("Miles Per Gallon (MPG)")
plt.tight_layout()
plt.show()

# Plot 2: Average MPG over Model Years by Origin
plt.figure(figsize=(8, 5))
sns.lineplot(data=df, x="model_year", y="mpg", hue="origin", marker="s")
plt.title("MPG: Fuel Efficiency Trends Over Model Years")
plt.xlabel("Model Year")
plt.ylabel("Mean MPG")
plt.tight_layout()
plt.show()