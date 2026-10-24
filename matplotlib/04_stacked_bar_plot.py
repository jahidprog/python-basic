import matplotlib.pyplot as plt
import numpy as np

years = ["2022", "2023", "2024", "2025"]
python = np.array([40, 45, 50, 58])
sql = np.array([25, 30, 32, 35])
ml = np.array([10, 18, 25, 34])

plt.bar(years, python, label="Python")
plt.bar(years, sql, bottom=python, label="SQL")
plt.bar(years, ml, bottom=python + sql, label="Machine Learning")
plt.title("Stacked Bar Chart")
plt.xlabel("Year")
plt.ylabel("Hours Practiced")
plt.legend()
plt.show()
