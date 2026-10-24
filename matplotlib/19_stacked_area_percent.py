import matplotlib.pyplot as plt

months = ["Jan", "Feb", "Mar", "Apr", "May", "Jun"]
python = [40, 38, 35, 32, 30, 28]
sql = [30, 30, 28, 27, 25, 24]
ml = [20, 22, 25, 28, 30, 32]
genai = [10, 10, 12, 13, 15, 16]
plt.stackplot(months, python, sql, ml, genai,
              labels=["Python", "SQL", "ML", "GenAI"])
plt.title("Stack Plot: Practice by Topic")
plt.xlabel("Month")
plt.ylabel("Hours")
plt.legend(loc="upper left")
plt.show()
