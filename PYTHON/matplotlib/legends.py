import matplotlib.pyplot as plt
product1 = [10, 15, 20, 25, 30]
product2 = [5, 10, 15, 20, 25]
plt.plot(product1, label="Product A")
plt.plot(product2, label="Product B")
plt.legend()
plt.show()