import json
from pptx import Presentation
import os

def generate_ppt_report():
    with open("reports/insights.json", "r") as f:
        insights = json.load(f)

    prs = Presentation()

    slide = prs.slides.add_slide(prs.slide_layouts[0])
    slide.shapes.title.text = "Power AI"
    slide.placeholders[1].text = "Automated Data Analysis Report"

    slide = prs.slides.add_slide(prs.slide_layouts[1])
    slide.shapes.title.text = "Dataset Overview"
    slide.placeholders[1].text = (
        f"Total Records: {insights['total_records']}\n"
        f"Total Columns: {insights['total_columns']}"
    )

    slide = prs.slides.add_slide(prs.slide_layouts[1])
    slide.shapes.title.text = "Average Salary by Department"
    tf = slide.placeholders[1].text_frame
    tf.text = ""

    for dept, salary in insights["average_salary_by_department"].items():
        p = tf.add_paragraph()
        p.text = f"{dept}: {salary}"
        p.level = 1

    slide = prs.slides.add_slide(prs.slide_layouts[1])
    slide.shapes.title.text = "Key Insight"
    slide.placeholders[1].text = (
        f"Highest salary is in the "
        f"{insights['highest_salary']['department']} department "
        f"({insights['highest_salary']['value']})."
    )

    os.makedirs("reports", exist_ok=True)
    output_path = "reports/PowerAI_Presentation.pptx"
    prs.save(output_path)

    return output_path
