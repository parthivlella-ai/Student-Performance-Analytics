"""
app.py
======
Student Performance Analytics System - Web Dashboard

A browser-based interactive dashboard built with Streamlit for the EWB Courses
Python with AI project assignment. Reuses analytical functions from functions.py.
"""

import os
import pandas as pd
import streamlit as st
import numpy as np

# Reusable functions from functions.py
from functions import (
    load_and_validate_data,
    process_student_data,
    calculate_class_summary,
    calculate_subject_analysis,
    calculate_department_analysis,
    get_top_performers,
    SUBJECT_COLUMNS,
    PASSING_MARK,
)

# -----------------------------------------------------------------------------
# 1. Page Configuration
# -----------------------------------------------------------------------------
st.set_page_config(
    page_title="Student Performance Analytics System",
    page_icon="🎓",
    layout="wide",
    initial_sidebar_state="expanded",
)

# -----------------------------------------------------------------------------
# 2. Custom CSS for Enhanced UI
# -----------------------------------------------------------------------------
st.markdown(
    """
    <style>
    /* Metric Card Styling */
    div[data-testid="stMetric"] {
        background-color: #f8fafc;
        border: 1px solid #e2e8f0;
        padding: 14px 18px;
        border-radius: 10px;
        box-shadow: 0 1px 3px rgba(0,0,0,0.05);
    }
    div[data-testid="stMetric"]:hover {
        border-color: #3b82f6;
        box-shadow: 0 4px 6px -1px rgba(59, 130, 246, 0.15);
        transition: all 0.2s ease-in-out;
    }
    /* Section Headers */
    .section-title {
        font-size: 1.25rem;
        font-weight: 600;
        color: #1e293b;
        margin-top: 1rem;
        margin-bottom: 0.5rem;
    }
    /* Callout Card */
    .highlight-card {
        background: linear-gradient(135deg, #eff6ff 0%, #dbeafe 100%);
        border-left: 5px solid #2563eb;
        padding: 12px 16px;
        border-radius: 8px;
        margin-bottom: 1rem;
    }
    </style>
    """,
    unsafe_allow_html=True,
)

# -----------------------------------------------------------------------------
# 3. Sidebar: Configuration, Upload & Filters
# -----------------------------------------------------------------------------
st.sidebar.title("🎓 Navigation & Filters")
st.sidebar.markdown("**Student Performance Analytics System**")
st.sidebar.caption("Python with AI | EWB Courses")

st.sidebar.markdown("---")

# Option to use default or upload custom CSV
data_source = st.sidebar.radio(
    "Data Source",
    options=["Default ('students.csv')", "Upload Custom CSV"],
    index=0,
)

uploaded_file = None
base_dir = os.path.dirname(os.path.abspath(__file__))
default_filepath = os.path.join(base_dir, "students.csv")

if data_source == "Upload Custom CSV":
    uploaded_file = st.sidebar.file_uploader("Upload CSV File", type=["csv"])
    file_to_load = uploaded_file if uploaded_file is not None else default_filepath
else:
    file_to_load = default_filepath

# -----------------------------------------------------------------------------
# 4. Data Loading & Validation (Using functions.py)
# -----------------------------------------------------------------------------
try:
    if not os.path.exists(default_filepath) and data_source == "Default ('students.csv')":
        st.error(f"Default dataset '{default_filepath}' not found in the project root directory.")
        st.stop()

    # Load and validate raw dataset
    raw_df = load_and_validate_data(file_to_load)

    # Process metrics using reusable function
    processed_df = process_student_data(raw_df)

except FileNotFoundError:
    st.error(f"Could not find the dataset file: '{file_to_load}'. Please ensure the file exists.")
    st.stop()
except ValueError as ve:
    st.error(f"Dataset Validation Error: {ve}")
    st.info("Please verify column headers, numeric bounds (0-100), and ensure Student IDs are unique.")
    st.stop()
except Exception as e:
    st.error(f"Unexpected error loading dataset: {e}")
    st.stop()

# -----------------------------------------------------------------------------
# 5. Sidebar Filtering Controls
# -----------------------------------------------------------------------------
st.sidebar.markdown("### Filter Students")

# Department Filter
departments = ["All"] + sorted(processed_df["Department"].unique().tolist())
selected_dept = st.sidebar.selectbox("Department", departments, index=0)

# Grade Filter
grades = ["All"] + sorted(processed_df["Grade"].unique().tolist())
selected_grade = st.sidebar.selectbox("Grade", grades, index=0)

# Pass / Fail Filter
status_options = ["All", "Pass", "Fail"]
selected_status = st.sidebar.radio("Result Status", status_options, index=0)

# Apply Filters
filtered_df = processed_df.copy()

if selected_dept != "All":
    filtered_df = filtered_df[filtered_df["Department"] == selected_dept]

if selected_grade != "All":
    filtered_df = filtered_df[filtered_df["Grade"] == selected_grade]

if selected_status != "All":
    filtered_df = filtered_df[filtered_df["Result"] == selected_status]

# -----------------------------------------------------------------------------
# 6. Main Dashboard Header
# -----------------------------------------------------------------------------
st.title("Student Performance Analytics System")
st.markdown(
    "Automated performance evaluation, grade computation, and academic insights "
    "powered by **Python**, **Pandas**, and **NumPy**."
)

# -----------------------------------------------------------------------------
# 7. KPI Metrics Cards
# -----------------------------------------------------------------------------
summary = calculate_class_summary(processed_df)

col1, col2, col3, col4 = st.columns(4)
with col1:
    st.metric(
        label="Total Students",
        value=summary["total_students"],
        help="Total number of evaluated students in the dataset.",
    )
with col2:
    st.metric(
        label="Class Average",
        value=f"{summary['class_average']}%",
        delta=f"Max: {summary['highest_average']}% | Min: {summary['lowest_average']}%",
        delta_color="off",
    )
with col3:
    st.metric(
        label="Pass Rate",
        value=f"{summary['pass_percentage']}%",
        delta=f"{summary['pass_count']} Passed / {summary['fail_count']} Failed",
        delta_color="normal" if summary["pass_percentage"] >= 80 else "inverse",
    )
with col4:
    st.metric(
        label="Average Attendance",
        value=f"{summary['average_attendance']}%",
        help="Overall average attendance across all students.",
    )

st.markdown("---")

# -----------------------------------------------------------------------------
# 8. Interactive Tabs Layout
# -----------------------------------------------------------------------------
tab_overview, tab_subjects, tab_departments, tab_honor, tab_support, tab_rules = st.tabs(
    [
        "📋 Student Records",
        "📊 Subject Analysis",
        "🏢 Department Performance",
        "🏆 Top Performers",
        "⚠️ Academic Support",
        "📖 Grading Rules",
    ]
)

# -----------------------------------------------------------------------------
# TAB 1: Student Records & Download
# -----------------------------------------------------------------------------
with tab_overview:
    st.markdown("### Student Performance Table")
    st.caption(
        f"Showing {len(filtered_df)} of {len(processed_df)} student records based on active filters."
    )

    display_cols = [
        "Student_ID",
        "Name",
        "Department",
        "Python",
        "Mathematics",
        "Statistics",
        "Attendance",
        "Total_Marks",
        "Average_Marks",
        "Grade",
        "Result",
    ]

    st.dataframe(
        filtered_df[display_cols],
        use_container_width=True,
        hide_index=True,
    )

    # Export / Download Button
    csv_data = processed_df.to_csv(index=False).encode("utf-8")
    st.download_button(
        label="📥 Download Complete Processed Results (CSV)",
        data=csv_data,
        file_name="student_results.csv",
        mime="text/csv",
        help="Download the complete dataset including calculated totals, averages, grades, and pass/fail statuses.",
    )

# -----------------------------------------------------------------------------
# TAB 2: Subject-wise Analysis
# -----------------------------------------------------------------------------
with tab_subjects:
    st.markdown("### Subject Performance Comparison")
    subject_stats, strongest_subject = calculate_subject_analysis(processed_df)

    st.markdown(
        f"""
        <div class="highlight-card">
            ⭐ <strong>Strongest Subject:</strong> <u>{strongest_subject}</u> with the highest class average of 
            <strong>{subject_stats[strongest_subject]['average']}%</strong>.
        </div>
        """,
        unsafe_allow_html=True,
    )

    # Prepare DataFrame for chart and table
    subj_chart_data = pd.DataFrame(
        {
            "Subject": list(subject_stats.keys()),
            "Average Marks": [stats["average"] for stats in subject_stats.values()],
            "Highest Marks": [stats["highest"] for stats in subject_stats.values()],
            "Lowest Marks": [stats["lowest"] for stats in subject_stats.values()],
        }
    ).set_index("Subject")

    col_chart, col_table = st.columns([3, 2])

    with col_chart:
        st.markdown("#### Subject Averages Chart")
        st.bar_chart(subj_chart_data["Average Marks"], use_container_width=True)

    with col_table:
        st.markdown("#### Subject Statistics")
        st.dataframe(subj_chart_data, use_container_width=True)

# -----------------------------------------------------------------------------
# TAB 3: Department Performance
# -----------------------------------------------------------------------------
with tab_departments:
    st.markdown("### Department-wise Performance")
    dept_df = calculate_department_analysis(processed_df)

    col_d1, col_d2 = st.columns([3, 2])
    with col_d1:
        st.markdown("#### Average Marks by Department")
        dept_chart_data = dept_df.set_index("Department")[["Average_Marks"]]
        st.bar_chart(dept_chart_data, use_container_width=True)

    with col_d2:
        st.markdown("#### Department Summary Table")
        st.dataframe(dept_df, use_container_width=True, hide_index=True)

# -----------------------------------------------------------------------------
# TAB 4: Top Performers (Honor Roll)
# -----------------------------------------------------------------------------
with tab_honor:
    st.markdown("### 🏆 Academic Honor Roll (Top 3 Performers)")
    top_3 = get_top_performers(processed_df, top_n=3)

    cols = st.columns(3)
    medals = ["🥇 Rank 1", "🥈 Rank 2", "🥉 Rank 3"]

    for i, (_, row) in enumerate(top_3.iterrows()):
        with cols[i]:
            st.markdown(
                f"""
                <div style="background:#ffffff; border:1px solid #cbd5e1; border-radius:10px; padding:18px; text-align:center; box-shadow:0 2px 4px rgba(0,0,0,0.06);">
                    <h3 style="margin-bottom:4px; color:#1e40af;">{medals[i]}</h3>
                    <h4 style="margin:4px 0; color:#0f172a;">{row['Name']}</h4>
                    <p style="color:#64748b; font-size:0.9rem; margin-bottom:12px;">ID: {row['Student_ID']} | {row['Department']}</p>
                    <div style="font-size:1.8rem; font-weight:700; color:#16a34a;">{row['Average_Marks']}%</div>
                    <p style="margin:4px 0; font-size:0.95rem;">Grade: <strong>{row['Grade']}</strong></p>
                    <span style="background-color:#dcfce7; color:#15803d; font-size:0.8rem; padding:3px 10px; border-radius:12px; font-weight:600;">{row['Result']}</span>
                </div>
                """,
                unsafe_allow_html=True,
            )

# -----------------------------------------------------------------------------
# TAB 5: Academic Support (Failing Students)
# -----------------------------------------------------------------------------
with tab_support:
    st.markdown("### ⚠️ Students Requiring Academic Support")
    st.caption(
        f"A student is identified as requiring support if they score below {PASSING_MARK} marks in ANY subject."
    )

    failed_students = processed_df[processed_df["Result"] == "Fail"]

    if failed_students.empty:
        st.success("🎉 All students have passed all subjects! No students currently require remediation.")
    else:
        st.warning(f"Found {len(failed_students)} student(s) scoring below the passing mark of {PASSING_MARK}.")

        for _, row in failed_students.iterrows():
            low_subjects = [
                f"**{sub}** ({row[sub]} marks)"
                for sub in SUBJECT_COLUMNS
                if row[sub] < PASSING_MARK
            ]
            deficit_text = ", ".join(low_subjects)

            st.error(
                f"**{row['Name']}** (`{row['Student_ID']}`) - Department: *{row['Department']}*\n\n"
                f"• Average Score: **{row['Average_Marks']}%** (Grade: **{row['Grade']}**)\n\n"
                f"• Deficit Subject(s) (< {PASSING_MARK}): {deficit_text}\n\n"
                f"• Attendance: **{row['Attendance']}%**"
            )

# -----------------------------------------------------------------------------
# TAB 6: Grading & Passing Rules
# -----------------------------------------------------------------------------
with tab_rules:
    st.markdown("### Documented Grading & Evaluation Rules")

    col_r1, col_r2 = st.columns(2)

    with col_r1:
        st.markdown("#### Letter Grading Scale")
        grading_rules = pd.DataFrame(
            {
                "Score Range": [
                    "90% to 100%",
                    "80% to 89.99%",
                    "70% to 79.99%",
                    "60% to 69.99%",
                    "50% to 59.99%",
                    "Below 50%",
                ],
                "Grade": ["A+", "A", "B", "C", "D", "F"],
                "Classification": [
                    "Outstanding",
                    "Excellent",
                    "Good",
                    "Average",
                    "Below Average",
                    "Fail",
                ],
            }
        )
        st.table(grading_rules)

    with col_r2:
        st.markdown("#### Pass / Fail Criteria")
        st.info(
            f"""
            - **Passing Threshold:** A student must score at least **{PASSING_MARK} marks** in **EVERY individual subject** (Python, Mathematics, Statistics).
            - **Single-Subject Failure Rule:** If a student scores below {PASSING_MARK} in even one subject, their overall result is marked as **Fail**, regardless of total or average marks.
            - **Attendance Requirement:** Minimum required attendance is recommended at **75%**.
            """
        )

# -----------------------------------------------------------------------------
# 9. Footer
# -----------------------------------------------------------------------------
st.markdown("---")
st.markdown(
    """
    <div style="text-align: center; color: #64748b; font-size: 0.85rem;">
        Student Performance Analytics System | Developed by <strong>Parthiv Lella</strong> | EWB Courses - Python with AI
    </div>
    """,
    unsafe_allow_html=True,
)
