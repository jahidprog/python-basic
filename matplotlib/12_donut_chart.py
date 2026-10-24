import matplotlib.pyplot as plt

labels = ["Python", "SQL", "ML", "GenAI"]
hours = [35, 20, 25, 20]
fig, ax = plt.subplots()
ax.pie(hours, labels=labels, autopct="%1.1f%%", startangle=90,
       wedgeprops={"width": 0.42, "edgecolor": "white"})
ax.set_title("Learning Time Split")
plt.show()
