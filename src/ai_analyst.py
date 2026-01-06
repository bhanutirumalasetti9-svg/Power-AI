import json

# Load insights
with open("../reports/insights.json", "r") as f:
    insights = json.load(f)

# -------- AI ANALYST LOGIC --------

def generate_executive_summary(insights):
    return (
        f"The dataset contains {insights['total_records']} records "
        f"across {insights['total_columns']} attributes. "
        f"Salary analysis shows variations across departments, "
        f"indicating different investment levels in human resources."
    )

def generate_key_insights(insights):
    text = []
    for dept, salary in insights["average_salary_by_department"].items():
        text.append(
            f"The {dept} department has an average salary of {salary}, "
            f"which reflects its compensation strategy."
        )
    return text

def generate_recommendations(insights):
    dept = insights["highest_salary"]["department"]
    value = insights["highest_salary"]["value"]
    return (
        f"The {dept} department shows the highest salary allocation "
        f"({value}). Management may review whether this investment "
        f"is aligned with business outcomes."
    )

# -------- AI OUTPUT --------

print("\n--- POWER AI : AUTOMATIC AI ANALYST ---\n")

print("📌 Executive Summary:")
print(generate_executive_summary(insights))

print("\n📊 Key Insights:")
for insight in generate_key_insights(insights):
    print("-", insight)

print("\n💡 AI Recommendation:")
print(generate_recommendations(insights))
