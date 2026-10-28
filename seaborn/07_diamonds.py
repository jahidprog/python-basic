"""
Dataset: Diamonds
Goal: Analyze diamond attributes and price distributions.
Plots: Histogram / Displot / Boxplot
"""
import seaborn as sns
import matplotlib.pyplot as plt

# Load dataset
df = sns.load_dataset("diamonds")
print("Diamonds Dataset Head:")
print(df.head())

# Plot 1: Price distribution by Cut
plt.figure(figsize=(9, 5))
sns.boxplot(data=df, x="cut", y="price", hue="color")
plt.title("Diamonds: Price Distribution by Cut and Color")
plt.xlabel("Cut Quality")
plt.ylabel("Price ($)")
plt.yscale("log")  # Log scale for better visibility of skewed price data
plt.tight_layout()
plt.show()

# Plot 2: Carat vs Price with Clarity hue
plt.figure(figsize=(9, 5))
sns.scatterplot(data=df.sample(2000, random_state=42), x="carat", y="price", hue="clarity", alpha=0.7)
plt.title("Diamonds: Carat vs Price (Sample of 2000)")
plt.xlabel("Carat Weight")
plt.ylabel("Price ($)")
plt.tight_layout()
plt.show()