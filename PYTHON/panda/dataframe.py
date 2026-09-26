import pandas as pd 
data = { "Name": ["Anu", "Ravi", "Kiran", "Sita", "Rahul"], 
        "Age": [22, 25, 21, 24, 27],
        "City": ["Rajahmundry", "Hyderabad", "Chennai", "Rajahmundry", "Hyderabad"],
        "Salary": [25000, 45000, 30000, 35000, 55000],
        "Department": ["IT", "HR", "IT", "Finance", "IT"] }
df = pd.DataFrame(data)
print(df) 

#greaterthan 30000
result = df[df["Salary"] > 30000]
print(result) 
#multiple conditions
result = df[ (df["Salary"] > 30000) & (df["Department"] == "IT") ]
print(result) 
#OR  condition
result = df[ (df["City"] == "Hyderabad") | (df["City"] == "Rajahmundry") ] 
print(result) 
#filtering data using isin() method
result = df[df["City"].isin(["Hyderabad", "Chennai"])]
print(result) 
#Sorting Data
#Sort salary ascending
df = df.sort_values("Salary")
print(df)
#Sort salary descending 
df = df.sort_values("Salary", ascending=False)
print(df)
#Sort by multiple columns
df = df.sort_values(["Department", "Salary"], ascending=[True, False])
print(df)
#Create a New Column
df["Bonus"] = df["Salary"] * 0.10
print(df) 
#Calculate Total Salary 
df["TotalSalary"] = df["Salary"] + df["Bonus"] 
print(df) 
#Conditional Column with  np.where() 
import numpy as np
df["Level"] = np.where( df["Salary"] >= 40000, "Senior", "Junior" )
print(df) 
#groupby()
result = df.groupby("Department")["Salary"].mean() 
print(result) 
# Multiple Aggregations 
result = df.groupby("Department")["Salary"].agg( ["count", "sum", "mean", "min", "max"] ) 
print(result) 
# Group By City
result = df.groupby("City")["Salary"].mean() 
print(result)
 #Group By Multiple Columns 
result = df.groupby( ["City", "Department"] )["Salary"].mean() 
print(result) 
#value_counts() 
print(df["Department"].value_counts()) 
#City-wise employee count 
print(df["City"].value_counts())
data = { "Name": ["Anu", "Ravi", "Kiran", "Sita"], "Age": [22, None, 21, 24], "Salary": [25000, 45000, None, 35000] }
df = pd.DataFrame(data)
print(df) 
#Find missing values
print(df.isnull().sum()) 
#Count all missing values
print(df.isnull().sum().sum())
# Remove rows with missing values
clean_df = df.dropna()
print(clean_df)
#Fill Age with average age 
df["Age"] = df["Age"].fillna(df["Age"].mean()) 
print(df) 
#Fill Salary with 0 
df["Salary"] = df["Salary"].fillna(0) 
print(df) 
#  Remove Duplicate Data 
df = df.drop_duplicates()
df = df.drop_duplicates(subset=["Name"])
#Rename Columns 
df.rename( 
          columns={ "Salary": "MonthlySalary", "Age": "EmployeeAge" }, inplace=True ) 
print(df)  
#  loc[]
print(df.loc[0]) 
#Select specific columns:
print(df.loc[:, ["Name", "MonthlySalary"]])
result = df.loc[df["MonthlySalary"] > 30000] 
print(result) 
#  iloc[]
print(df.iloc[0])
print(df.iloc[0:3])
print(df.iloc[0:3, 0:2]) 
