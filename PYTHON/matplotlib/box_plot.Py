import matplotlib.pyplot as plt
#box plot
salary = [25000, 28000, 32000, 38000, 43000, 50000, 58000]
plt.boxplot(salary)
plt.title("Salary Distribution")
plt.ylabel("Salary")
plt.show()