import pandas as pd
df = pd.read_csv(r"C:\Users\ANUSHA\OneDrive\INTERNSHIP\PYTHON\panda\Assignment3_Bank_Dataset.csv")
print(df)
#highest balance
print(df[df['Balance'] == df['Balance'].max()])
#lowest balance
print(df[df['Balance'] == df['Balance'].min()])
#  Customers with loans > ₹5 lakh. 
print(df[df['Loan'] > 500000])
#city wise customers
print(df.groupby('City').count())
#total balance
print(df['Balance'].sum())