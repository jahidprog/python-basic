"""
Dataset: Titanic
Goal: Explore passenger survival demographics.
Plots: Count plot / Bar plot
"""
import seaborn as sns
import matplotlib.pyplot as plt

# Load dataset
df = sns.load_dataset("titanic")
print("Titanic Dataset Head:")
print(df.head())

# Plot 1: Survival counts by Passenger Class and Sex
plt.figure(figsize=(8, 5))
sns.countplot(data=df, x="class", hue="survived", palette="Set2")
plt.title("Titanic: Survival Counts by Class")
plt.xlabel("Passenger Class")
plt.ylabel("Count")
plt.legend(title="Survived", labels=["No", "Yes"])
plt.tight_layout()
plt.show()

# Plot 2: Survival Rate by Deck
plt.figure(figsize=(8, 5))
sns.barplot(data=df, x="deck", y="survived", palette="crest", errorbar=None)
plt.title("Titanic: Survival Rate by Deck")
plt.xlabel("Deck")
plt.ylabel("Survival Rate (0 - 1)")
plt.tight_layout()
plt.show()