#Real-Time Data Analyst Example
import pandas as pd


data = { "Employee": ["A", "B", "C", "D", "E", "F"],
        "Department": ["IT", "HR", "IT", "Sales", "HR", "IT"], 
        "Salary": [40000, 30000, 50000, 35000, 32000, 60000], 
        "Experience": [2, 1, 4, 3, 2, 6] } 
df = pd.DataFrame(data) 
#Question 1: Employees earning above ₹40,000 
print(df[df["Salary"] > 40000])
#Question 2: Average salary 
print(df["Salary"].mean())
#Question 3: Highest salary 
print(df["Salary"].max())
#Question 4: Employee with highest salary 
print(df.loc[df["Salary"].idxmax()])
#Question 5: Average salary by department 
print(df.groupby("Department")["Salary"].mean())
#Question 6: Number of employees by department 
print(df["Department"].value_counts())
#Question 7: Employees with more than 3 years experience 
print(df[df["Experience"] > 3])
#Question 8: Add annual salary 
df["AnnualSalary"] = df["Salary"] * 12 
print(df)
