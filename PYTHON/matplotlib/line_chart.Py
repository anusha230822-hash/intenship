import matplotlib.pyplot as plt
months = ["Jan", "Feb", "Mar", "Apr", "May", "Jun"] 
sales = [100, 120, 115, 140, 160, 155]
plt.plot(months, sales, marker='o')
plt.title("monthly sales")
plt.xlabel("months")
plt.ylabel("sales")
plt.grid()
plt.legend()
plt.show()
