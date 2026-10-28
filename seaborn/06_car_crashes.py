"""
Dataset: Car Crashes
Goal: Examine state-level driving factors and crash rates.
Plots: Heatmap / Correlation Matrix / Pairwise Scatter
"""
import seaborn as sns
import matplotlib.pyplot as plt

# Load dataset
df = sns.load_dataset("car_crashes")
print("Car Crashes Dataset Head:")
print(df.head())

# Plot 1: Correlation Matrix of driving attributes
plt.figure(figsize=(8, 6))
numeric_df = df.drop(columns=["abbrev"])
sns.heatmap(numeric_df.corr(), annot=True, cmap="coolwarm", fmt=".2f", vmin=-1, vmax=1)
plt.title("Car Crashes: Attribute Correlation Matrix")
plt.tight_layout()
plt.show()

# Plot 2: Alcohol vs Total Crashes
plt.figure(figsize=(8, 5))
sns.regplot(data=df, x="alcohol", y="total", color="teal", marker="o")
plt.title("Car Crashes: Alcohol Involvement vs Total Crashes")
plt.xlabel("Speeding/Alcohol-Involved Crash Rate")
plt.ylabel("Total Crashes per Billion Miles")
plt.tight_layout()
plt.show()
