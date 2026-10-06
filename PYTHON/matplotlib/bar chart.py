import matplotlib.pyplot as plt
products = ["Laptop", "Mobile", "Tablet", "Watch"] 
sales = [50, 120, 80, 40] 
plt.bar(products, sales) 
plt.title("Product Sales") 
plt.xlabel("Product") 
plt.ylabel("Units Sold") 
plt.show()