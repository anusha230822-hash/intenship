import matplotlib.pyplot as plt
week = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
study_hours = [8, 7, 6, 5, 4, 3, 2]
plt.subplot(2, 2, 1)
plt.plot(week, study_hours)
plt.title("Study Hours")
plt.xlabel("Day")
plt.ylabel("Hours")
plt.xticks(rotation=45)
plt.grid()

plt.subplot(2, 2, 2)
plt.bar(week, study_hours)
plt.title("Study Hours Bar Chart")
plt.xlabel("Day")
plt.ylabel("Hours")
plt.xticks(rotation=45)
plt.grid()

plt.subplot(2, 2, 3)
plt.scatter(week, study_hours)
plt.title("Study Hours Scatter Plot")
plt.xlabel("Day")
plt.ylabel("Hours")
plt.xticks(rotation=45)
plt.grid()

plt.subplot(2, 2, 4)
plt.hist(study_hours, bins=5)
plt.title("Study Hours Histogram")
plt.xlabel("Hours")
plt.ylabel("Frequency")
plt.grid()

plt.tight_layout()
plt.show()