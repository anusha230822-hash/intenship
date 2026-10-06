import matplotlib.pyplot as plt
months = ["Jan", "Feb", "Mar", "Apr"] 
sales = [100, 150, 120, 180] 
plt.fill_between(months, sales, alpha=0.5) 
plt.plot(months, sales) 
plt.title("Sales Area Chart") 
plt.xlabel("Month") 
plt.ylabel("Sales") 
plt.show()