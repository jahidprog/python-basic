import matplotlib.pyplot as plt

months = ["Jan", "Feb", "Mar", "Apr", "May", "Jun"]
python_hours = [10, 12, 15, 18, 22, 25]
scores = [60, 65, 68, 75, 80, 85]
topics = ["Python", "SQL", "ML", "GenAI"]
hours = [25, 16, 20, 30]

fig, axes = plt.subplots(2, 2, figsize=(11, 7), layout="constrained")
axes[0, 0].plot(months, python_hours, marker="o")
axes[0, 0].set_title("Python Practice")
axes[0, 0].set_ylabel("Hours")
axes[0, 1].bar(topics, hours)
axes[0, 1].set_title("Hours by Topic")
axes[1, 0].plot(months, scores, marker="s")
axes[1, 0].set_title("Quiz Scores")
axes[1, 0].set_ylabel("Score")
axes[1, 1].scatter(python_hours, scores)
axes[1, 1].set_title("Python Hours vs Quiz Score")
axes[1, 1].set_xlabel("Python Hours")
axes[1, 1].set_ylabel("Score")
fig.suptitle("Learning Progress Dashboard")
plt.show()
