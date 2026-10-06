import matplotlib.pyplot as plt
months = ["Jan", "Feb", "Mar", "Apr", "May", "Jun"]
sales = [100, 120, 115, 140, 160, 155]
plt.bar(months, sales)
plt.title("monthly sales")
plt.xlabel("months")
plt.ylabel("sales")
plt.annotate("highest sales",
             xy=(4, 160),
             xytext=(3, 140),
             arrowprops=dict(arrowstyle="->", color='black'))
plt.annotate("lowest sales",
             xy=(0, 100),
             xytext=(1, 120),
             arrowprops=dict(arrowstyle="->", color='black'))
plt.show()