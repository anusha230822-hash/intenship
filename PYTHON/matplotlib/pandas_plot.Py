import pandas as pd
import matplotlib.pyplot as plt
df = pd.read_csv("datasets/Sales_Data.csv")
plt.scatter(df["Total_Revenue"], df["Total_Profit"],marker='o',label="revenue vs profit")
plt.scatter(df["Total_Revenue"], df["Total_Cost"],marker='s',label="revenue vs cost")
plt.title("Revenue vs Profit and Cost")
plt.xlabel("Total Revenue")
plt.ylabel("Total Profit and Cost")
plt.legend()
plt.grid()
plt.show()
