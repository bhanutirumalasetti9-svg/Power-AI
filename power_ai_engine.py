import pandas as pd
import json
import os

def run_power_ai(csv_path):
    # Load data
    df = pd.read_csv(csv_path)

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

    # Ensure reports folder exists
    os.makedirs("reports", exist_ok=True)

    # Save insights
    with open("reports/insights.json", "w") as f:
        json.dump(insights, f, indent=4)

    return insights
