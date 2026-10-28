"""
Dataset: Tips
Goal: Analyze restaurant tipping behavior.
Plots: Violin plot / Relational Scatterplot
"""
import seaborn as sns
import matplotlib.pyplot as plt

# Load dataset
df = sns.load_dataset("tips")
print("Tips Dataset Head:")
print(df.head())

# Plot 1: Total bill vs Tip colored by smoker status and day
plt.figure(figsize=(8, 5))
sns.scatterplot(data=df, x="total_bill", y="tip", hue="day", style="time", size="size", sizes=(20, 200))
plt.title("Tips: Total Bill vs Tip")
plt.xlabel("Total Bill ($)")
plt.ylabel("Tip ($)")
plt.tight_layout()
plt.show()

# Plot 2: Violin plot showing total bill distribution across days
plt.figure(figsize=(8, 5))
sns.violinplot(data=df, x="day", y="total_bill", hue="sex", split=True, inner="quart")
plt.title("Tips: Total Bill Distribution by Day & Sex")
plt.xlabel("Day of Week")
plt.ylabel("Total Bill ($)")
plt.tight_layout()
plt.show()