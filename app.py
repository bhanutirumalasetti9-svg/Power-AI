import streamlit as st
import os
from power_ai_engine import run_power_ai
from src.word_report_generator import generate_word_report
from src.ppt_generator import generate_ppt_report

st.set_page_config(page_title="Power AI", layout="centered")

st.title("Power AI")
st.write("Automatic AI Analyst for Data Analysis and Reporting")

# Session state to persist insights
if "insights" not in st.session_state:
    st.session_state.insights = None

uploaded_file = st.file_uploader("Upload your CSV file", type=["csv"])

if uploaded_file is not None:
    os.makedirs("data", exist_ok=True)
    file_path = f"data/{uploaded_file.name}"

    with open(file_path, "wb") as f:
        f.write(uploaded_file.getbuffer())

    st.success("File uploaded successfully!")

    if st.button("Run Power AI"):
        with st.spinner("Power AI is analyzing your data..."):
            st.session_state.insights = run_power_ai(file_path)

        st.success("Analysis completed!")

if st.session_state.insights:
    insights = st.session_state.insights

    st.subheader("AI Analyst Summary")
    st.write(
        f"The dataset contains {insights['total_records']} records across "
        f"{insights['total_columns']} columns. "
        f"The highest salary is observed in the "
        f"{insights['highest_salary']['department']} department."
    )

    st.subheader("Average Salary by Department")
    for dept, salary in insights["average_salary_by_department"].items():
        st.write(f"{dept}: {salary}")

    st.divider()

    col1, col2 = st.columns(2)

    with col1:
        if st.button("Generate Word Report"):
            try:
                path = generate_word_report()
                with open(path, "rb") as f:
                    st.download_button(
                        "Download Word Report",
                        f,
                        file_name="PowerAI_Report.docx"
                    )
            except Exception as e:
                st.error(f"Word report error: {e}")

    with col2:
        if st.button("Generate PowerPoint Report"):
            try:
                path = generate_ppt_report()
                with open(path, "rb") as f:
                    st.download_button(
                        "Download PowerPoint",
                        f,
                        file_name="PowerAI_Presentation.pptx"
                    )
            except Exception as e:
                st.error(f"PPT error: {e}")
