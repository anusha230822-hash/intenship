import matplotlib.pyplot as plt
experience = [1, 2, 3, 4, 5, 6, 7] 
salary = [25000, 28000, 32000, 38000, 43000, 50000, 58000]
plt.scatter(experience, salary)
plt.title("Experience vs Salary")
plt.xlabel("Experience (years)")
plt.ylabel("Salary")
plt.show()