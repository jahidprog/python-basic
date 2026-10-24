import matplotlib.pyplot as plt

months = ["Jan", "Feb", "Mar", "Apr", "May", "Jun"]
python = [20, 25, 30, 35, 40, 45]
sql = [15, 18, 20, 22, 25, 28]
ml = [5, 8, 12, 18, 25, 32]

plt.stackplot(months, python, sql, ml, labels=["Python", "SQL", "Machine Learning"])
plt.title("Stack Plot: Learning Time by Topic")
plt.xlabel("Month")
plt.ylabel("Hours")
plt.legend(loc="upper left")
plt.show()
