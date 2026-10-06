import matplotlib.pyplot as plt
fig, ax = plt.subplots() 
ax.plot([1, 2, 3], [10, 20, 30]) 
ax.set_title("Sales Trend") 
ax.set_xlabel("Month") 
ax.set_ylabel("Sales") 
plt.show()