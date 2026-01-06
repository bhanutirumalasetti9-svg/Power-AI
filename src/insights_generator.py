import pandas as pd
import json

# Load data
df = pd.read_csv("../data/sample.csv")

# Clean data
df = df.drop_duplicates()
df["Age"] = df["Age"].fillna(df["Age"].mean())
df["Salary"] = df["Salary"].fillna(df["Salary"].mean())
df["Department"] = df["Department"].fillna("Unknown")

# Generate insights
insights = {
    "total_records": int(len(df)),
    "total_columns": int(len(df.columns)),
    "average_salary_by_department": df.groupby("Department")["Salary"].mean().to_dict(),
    "highest_salary": {
        "department": df.loc[df["Salary"].idxmax()]["Department"],
        "value": float(df["Salary"].max())
    }
}

# Save insights
with open("../reports/insights.json", "w") as f:
    json.dump(insights, f, indent=4)

print("✅ insights.json created successfully")
