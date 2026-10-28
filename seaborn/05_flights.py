"""
Dataset: Flights
Goal: Visualize air passenger trends over time.
Plots: Heatmap / Line plot
"""
import seaborn as sns
import matplotlib.pyplot as plt

# Load dataset
df = sns.load_dataset("flights")
print("Flights Dataset Head:")
print(df.head())

# Plot 1: Monthly passenger trend over years
plt.figure(figsize=(10, 5))
sns.lineplot(data=df, x="year", y="passengers", hue="month", marker="o")
plt.title("Flights: Monthly Passengers Over Years")
plt.xlabel("Year")
plt.ylabel("Number of Passengers")
plt.legend(bbox_to_anchor=(1.05, 1), loc='upper left')
plt.tight_layout()
plt.show()

# Plot 2: Pivot heatmap of Passengers (Month vs Year)
pivot_df = df.pivot(index="month", columns="year", values="passengers")
plt.figure(figsize=(10, 6))
sns.heatmap(pivot_df, annot=True, fmt="d", cmap="YlGnBu", cbar_kws={'label': 'Passengers'})
plt.title("Flights: Passengers Heatmap (Month vs Year)")
plt.tight_layout()
plt.show()