import pandas as pd

# Load raw data
df = pd.read_csv("../data/sample.csv")

# Clean data
df = df.drop_duplicates()
df["Age"] = df["Age"].fillna(df["Age"].mean())
df["Salary"] = df["Salary"].fillna(df["Salary"].mean())
df["Department"] = df["Department"].fillna("Unknown")

# Create Power BI friendly dataset
powerbi_df = df.groupby("Department").agg(
    Average_Salary=("Salary", "mean"),
    Employee_Count=("Name", "count")
).reset_index()

# Save for Power BI
powerbi_df.to_csv("../reports/powerbi_data.csv", index=False)

print("✅ powerbi_data.csv generated for Power BI")
