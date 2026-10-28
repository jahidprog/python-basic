"""
Dataset: Iris
Goal: Analyze flower measurements across different species.
Plots: Pairplot / Scatterplot
"""
import seaborn as sns
import matplotlib.pyplot as plt

# Load dataset
df = sns.load_dataset("iris")
print("Iris Dataset Head:")
print(df.head())

# Plot 1: Sepal length vs Sepal width by species
plt.figure(figsize=(8, 5))
sns.scatterplot(data=df, x="sepal_length", y="sepal_width", hue="species", style="species", s=80)
plt.title("Iris: Sepal Length vs Sepal Width")
plt.xlabel("Sepal Length (cm)")
plt.ylabel("Sepal Width (cm)")
plt.tight_layout()
plt.show()

# Plot 2: Pairplot across all numeric features
sns.pairplot(df, hue="species", corner=True)
plt.suptitle("Iris: Pairwise Feature Comparison", y=1.02)
plt.show()