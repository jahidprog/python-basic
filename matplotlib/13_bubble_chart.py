import matplotlib.pyplot as plt

projects = ["RAG", "Classifier", "Chatbot", "Vision"]
weeks = [3, 2, 4, 5]
complexity = [6, 4, 8, 9]
impact = [250, 150, 400, 500]
plt.scatter(weeks, complexity, s=impact, alpha=0.55, edgecolors="black")
for i, project in enumerate(projects):
    plt.annotate(project, (weeks[i], complexity[i]), xytext=(5, 5), textcoords="offset points")
plt.title("Project Effort vs Complexity (Bubble Size = Impact)")
plt.xlabel("Time (weeks)")
plt.ylabel("Complexity")
plt.grid(alpha=0.25)
plt.show()
