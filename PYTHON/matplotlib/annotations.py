import matplotlib.pyplot as plt
months = ["Jan", "Feb", "Mar", "Apr"]
sales = [100, 150, 120, 180]
plt.plot(months, sales, marker="o")
plt.annotate(
    "Highest Sales",
    xy=("Apr", 180),
    xytext=("Feb", 170),
    arrowprops={"arrowstyle": "->"}
)
plt.show()