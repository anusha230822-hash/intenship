import matplotlib.pyplot as plt
salary = [    25000, 28000, 30000, 32000,    35000, 37000, 40000, 42000,    45000, 100000 ]
plt.boxplot(salary)
plt.title("Salary Distribution")
plt.ylabel("Salary")
plt.show()