import pandas as pd
df = pd.read_csv(r"C:\Users\ANUSHA\OneDrive\INTERNSHIP\PYTHON\panda\Assignment4_ECommerce_Dataset.csv")
print(df)
#most expensive product
print(df[df['Price'] == df['Price'].max()])
#cheapest product
print(df[df['Price'] == df['Price'].min()])
#avg rate
print(df['Rating'].mean())
#category wise products
print(df.groupby('Category')['Product'].apply(list))
# Total inventory value (  Price × Quantity  ).
print(df['Price'].sum() * df['Quantity'].sum())