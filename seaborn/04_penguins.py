"""
Dataset: Penguins
Goal: Study physical dimensions of penguin species.
Plots: KDE Plot / Box plot
"""
import seaborn as sns
import matplotlib.pyplot as plt

# Load dataset
df = sns.load_dataset("penguins")
print("Penguins Dataset Head:")
print(df.head())

# Plot 1: Flipper Length vs Body Mass
plt.figure(figsize=(8, 5))
sns.scatterplot(data=df, x="flipper_length_mm", y="body_mass_g", hue="species", style="sex", s=90)
plt.title("Penguins: Flipper Length vs Body Mass")
plt.xlabel("Flipper Length (mm)")
plt.ylabel("Body Mass (g)")
plt.tight_layout()
plt.show()

# Plot 2: Bill Length Distribution by Island
plt.figure(figsize=(8, 5))
sns.boxplot(data=df, x="island", y="bill_length_mm", hue="species")
plt.title("Penguins: Bill Length by Island")
plt.xlabel("Island")
plt.ylabel("Bill Length (mm)")
plt.tight_layout()
plt.show()