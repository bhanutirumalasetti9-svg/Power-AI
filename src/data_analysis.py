import pandas as pd

# Load cleaned data
df = pd.read_csv("../data/sample.csv")

# Clean again (temporary – later we modularize)
df["Age"] = df["Age"].fillna(df["Age"].mean())
df["Salary"] = df["Salary"].fillna(df["Salary"].mean())
df["Department"] = df["Department"].fillna("Unknown")


print("\n--- POWER AI INSIGHTS ---\n")

print("1. Dataset Overview")
print(f"Total Records: {len(df)}")
print(f"Total Columns: {len(df.columns)}\n")

print("2. Numerical Summary")
print(df.describe(), "\n")

print("3. Average Salary by Department")
print(df.groupby("Department")["Salary"].mean(), "\n")

print("4. Key Insight:")
highest_paid = df.loc[df["Salary"].idxmax()]
print(f"Highest salary is in {highest_paid['Department']} department with salary {highest_paid['Salary']}")
