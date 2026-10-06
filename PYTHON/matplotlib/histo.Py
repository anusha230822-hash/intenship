import matplotlib.pyplot as plt
marks = [45, 50, 52, 55, 60, 62, 65, 68, 70, 72, 75, 78, 80, 82, 85, 90]
plt.hist(marks, bins=10, edgecolor='black')
plt.title("Distribution of Marks")
plt.xlabel("Marks")
plt.ylabel("Frequency")
plt.show()