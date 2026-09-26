
import pandas as pd
df = pd.read_csv(r"C:\Users\ANUSHA\OneDrive\INTERNSHIP\PYTHON\panda\Assignment2_Weather_Dataset.csv")
print(df)
# avg temp
print(df['Temperature'].mean())
#hottest city
print(df[df['Temperature'] == df['Temperature'].max()])
#coldest city
print(df[df['Temperature'] == df['Temperature'].min()])
#city above 35 c
print(df[df['Temperature'] > 35])
#sort by rainfall
print(df.sort_values(by='Rainfall', ascending=False))