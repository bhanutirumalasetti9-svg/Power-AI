import pandas as pd

df = pd.read_csv("../data/sample.csv")

df = df.drop_duplicates()
df["Age"].fillna(df["Age"].mean(), inplace=True)
df["Salary"].fillna(df["Salary"].mean(), inplace=True)
df["Department"].fillna("Unknown", inplace=True)

print("Cleaned Data:")
print(df)
