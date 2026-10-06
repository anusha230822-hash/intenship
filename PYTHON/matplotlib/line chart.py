import matplotlib.pyplot as plt
months = ["Jan", "Feb", "Mar", "Apr", "May"] 
sales = [10000, 15000, 12000, 18000, 22000] 
plt.plot(months, sales) 
plt.title("Monthly Sales") 
plt.xlabel("Month") 
plt.ylabel("Sales") 
plt.show()