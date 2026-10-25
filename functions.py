"""
functions.py
============
Student Performance Analytics System - Helper Functions

This module provides reusable functions for loading, validating,
processing, and analyzing student performance records using Python,
NumPy, and Pandas.
"""

import numpy as np
import pandas as pd

# Expected columns in the input CSV file
REQUIRED_COLUMNS = [
    "Student_ID",
    "Name",
    "Department",
    "Python",
    "Mathematics",
    "Statistics",
    "Attendance",
]

# Subject marks columns to analyze
SUBJECT_COLUMNS = ["Python", "Mathematics", "Statistics"]

# Minimum passing mark required in EVERY subject
PASSING_MARK = 35


def load_and_validate_data(filepath: str) -> pd.DataFrame:
    """
    Reads the student CSV file and validates its integrity:
    1. Checks if all required columns are present.
    2. Checks for missing/null values.
    3. Checks for duplicate Student_IDs.
    4. Validates that marks and attendance fall in the range 0 to 100.

    Parameters:
        filepath (str): Path to the CSV file.

    Returns:
        pd.DataFrame: Validated DataFrame.

    Raises:
        FileNotFoundError: If the file path does not exist.
        ValueError: If validation rules are violated.
    """
    # 1. Read CSV using Pandas
    df = pd.read_csv(filepath)

    # 2. Check for missing columns
    missing_cols = [col for col in REQUIRED_COLUMNS if col not in df.columns]
    if missing_cols:
        raise ValueError(f"Missing required columns in CSV: {missing_cols}")

    # 3. Check for null/missing values
    null_counts = df[REQUIRED_COLUMNS].isnull().sum()
    if null_counts.any():
        cols_with_nulls = null_counts[null_counts > 0].to_dict()
        raise ValueError(f"Dataset contains missing values: {cols_with_nulls}")

    # 4. Check for duplicate Student_IDs
    if df["Student_ID"].duplicated().any():
        duplicate_ids = df[df["Student_ID"].duplicated()]["Student_ID"].tolist()
        raise ValueError(f"Duplicate Student_ID(s) found: {duplicate_ids}")

    # 5. Check numeric ranges (0 to 100 for subjects and attendance)
    numeric_cols = SUBJECT_COLUMNS + ["Attendance"]
    for col in numeric_cols:
        # Check for invalid values (< 0 or > 100)
        out_of_range = df[(df[col] < 0) | (df[col] > 100)]
        if not out_of_range.empty:
            invalid_ids = out_of_range["Student_ID"].tolist()
            raise ValueError(f"Column '{col}' has values outside [0, 100] for students: {invalid_ids}")

    return df


def calculate_total(marks: list) -> float:
    """
    Calculates total marks from a list of numerical marks using NumPy.

    Parameters:
        marks (list): List of subject scores.

    Returns:
        float: Sum of all marks.
    """
    marks_array = np.array(marks, dtype=float)
    return float(np.sum(marks_array))


def calculate_average(total: float, num_subjects: int) -> float:
    """
    Calculates average marks rounded to 2 decimal places.

    Parameters:
        total (float): Total marks scored.
        num_subjects (int): Total number of subjects.

    Returns:
        float: Average mark.
    """
    if num_subjects <= 0:
        return 0.0
    return round(float(total / num_subjects), 2)


def assign_grade(average_mark: float) -> str:
    """
    Assigns a letter grade based on documented academic thresholds:
    - 90.0 to 100.0 : A+ (Outstanding)
    - 80.0 to 89.99 : A  (Excellent)
    - 70.0 to 79.99 : B  (Good)
    - 60.0 to 69.99 : C  (Average)
    - 50.0 to 59.99 : D  (Below Average)
    - Below 50.0    : F  (Fail)

    Parameters:
        average_mark (float): Average mark percentage.

    Returns:
        str: Grade letter.
    """
    if average_mark >= 90.0:
        return "A+"
    elif average_mark >= 80.0:
        return "A"
    elif average_mark >= 70.0:
        return "B"
    elif average_mark >= 60.0:
        return "C"
    elif average_mark >= 50.0:
        return "D"
    else:
        return "F"


def determine_pass_fail(marks: list, passing_mark: float = PASSING_MARK) -> str:
    """
    Determines Pass or Fail status.
    Rule: A student must score at least `passing_mark` (default 35)
          in EVERY individual subject to Pass.

    Parameters:
        marks (list): List of subject marks.
        passing_mark (float): Minimum mark required per subject.

    Returns:
        str: 'Pass' or 'Fail'
    """
    for mark in marks:
        if mark < passing_mark:
            return "Fail"
    return "Pass"


def process_student_data(df: pd.DataFrame) -> pd.DataFrame:
    """
    Iterates through each student record using a loop, applies calculation
    functions, and appends new analytical columns:
    - Total_Marks
    - Average_Marks
    - Grade
    - Result (Pass / Fail)

    Parameters:
        df (pd.DataFrame): Validated raw student DataFrame.

    Returns:
        pd.DataFrame: Processed DataFrame with analytical columns.
    """
    # Create a copy so the original DataFrame remains unmodified
    processed_df = df.copy()

    totals = []
    averages = []
    grades = []
    results = []

    # Iterate through each row in the DataFrame using a loop
    for _, row in processed_df.iterrows():
        # Extract marks for the three subjects
        subject_marks = [row["Python"], row["Mathematics"], row["Statistics"]]

        # Reusable functions call
        total = calculate_total(subject_marks)
        average = calculate_average(total, len(subject_marks))
        grade = assign_grade(average)
        result = determine_pass_fail(subject_marks, PASSING_MARK)

        # Store calculated metrics
        totals.append(total)
        averages.append(average)
        grades.append(grade)
        results.append(result)

    # Assign calculated lists as new columns in the DataFrame
    processed_df["Total_Marks"] = totals
    processed_df["Average_Marks"] = averages
    processed_df["Grade"] = grades
    processed_df["Result"] = results

    return processed_df


def calculate_class_summary(df: pd.DataFrame) -> dict:
    """
    Computes overall class performance metrics using NumPy and Pandas:
    - Overall Class Average
    - Highest Average Mark
    - Lowest Average Mark
    - Total Students
    - Total Passed and Pass Percentage
    - Total Failed and Fail Percentage
    - Average Attendance

    Parameters:
        df (pd.DataFrame): Processed DataFrame.

    Returns:
        dict: Summary statistics.
    """
    avg_marks_array = np.array(df["Average_Marks"], dtype=float)
    attendance_array = np.array(df["Attendance"], dtype=float)

    total_students = len(df)
    pass_count = int(np.sum(df["Result"] == "Pass"))
    fail_count = int(np.sum(df["Result"] == "Fail"))

    pass_percentage = round((pass_count / total_students) * 100, 2) if total_students > 0 else 0.0
    fail_percentage = round((fail_count / total_students) * 100, 2) if total_students > 0 else 0.0

    return {
        "total_students": total_students,
        "class_average": round(float(np.mean(avg_marks_array)), 2),
        "highest_average": round(float(np.max(avg_marks_array)), 2),
        "lowest_average": round(float(np.min(avg_marks_array)), 2),
        "average_attendance": round(float(np.mean(attendance_array)), 2),
        "pass_count": pass_count,
        "fail_count": fail_count,
        "pass_percentage": pass_percentage,
        "fail_percentage": fail_percentage,
    }


def calculate_subject_analysis(df: pd.DataFrame, subjects: list = None) -> tuple:
    """
    Computes subject-wise metrics (average, highest, lowest) and identifies
    the strongest subject (subject with highest average mark).

    Parameters:
        df (pd.DataFrame): Processed DataFrame.
        subjects (list): List of subject column names.

    Returns:
        tuple: (subject_stats_dict, strongest_subject_name)
    """
    if subjects is None:
        subjects = SUBJECT_COLUMNS

    subject_stats = {}
    strongest_subject = ""
    highest_avg_found = -1.0

    for subject in subjects:
        marks_array = np.array(df[subject], dtype=float)
        subj_avg = round(float(np.mean(marks_array)), 2)
        subj_max = round(float(np.max(marks_array)), 2)
        subj_min = round(float(np.min(marks_array)), 2)

        subject_stats[subject] = {
            "average": subj_avg,
            "highest": subj_max,
            "lowest": subj_min,
        }

        # Track the subject with the highest average
        if subj_avg > highest_avg_found:
            highest_avg_found = subj_avg
            strongest_subject = subject

    return subject_stats, strongest_subject


def calculate_department_analysis(df: pd.DataFrame) -> pd.DataFrame:
    """
    Analyzes student performance by department:
    - Number of students in each department
    - Department-wise average marks
    - Department-wise average attendance

    Parameters:
        df (pd.DataFrame): Processed DataFrame.

    Returns:
        pd.DataFrame: Grouped department summary.
    """
    dept_summary = (
        df.groupby("Department")
        .agg(
            Student_Count=("Student_ID", "count"),
            Average_Marks=("Average_Marks", "mean"),
            Average_Attendance=("Attendance", "mean"),
        )
        .reset_index()
    )

    dept_summary["Average_Marks"] = dept_summary["Average_Marks"].round(2)
    dept_summary["Average_Attendance"] = dept_summary["Average_Attendance"].round(2)
    dept_summary = dept_summary.sort_values(by="Average_Marks", ascending=False)

    return dept_summary


def get_top_performers(df: pd.DataFrame, top_n: int = 3) -> pd.DataFrame:
    """
    Identifies the top N students based on Average_Marks.

    Parameters:
        df (pd.DataFrame): Processed DataFrame.
        top_n (int): Number of top students to return (default: 3).

    Returns:
        pd.DataFrame: Subset containing top rankers.
    """
    # Sort students by Average_Marks in descending order
    sorted_df = df.sort_values(by="Average_Marks", ascending=False)
    cols = ["Student_ID", "Name", "Department", "Average_Marks", "Grade", "Result"]
    return sorted_df.head(top_n)[cols].reset_index(drop=True)


def save_results_to_csv(df: pd.DataFrame, output_filepath: str = "student_results.csv") -> None:
    """
    Saves the analyzed DataFrame with all calculated metrics into a CSV file.

    Parameters:
        df (pd.DataFrame): Processed DataFrame.
        output_filepath (str): Destination file path.
    """
    df.to_csv(output_filepath, index=False)
