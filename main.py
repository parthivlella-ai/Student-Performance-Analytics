"""
main.py
=======
Student Performance Analytics System - Main Application

This script coordinates the data analysis pipeline:
1. Loads and validates the student records from 'students.csv'.
2. Calculates totals, averages, letter grades, and pass/fail results.
3. Computes class-wide, subject-wise, and department-wise metrics.
4. Highlights the top 3 performers.
5. Saves the final processed report into 'student_results.csv'.
6. Catches and gracefully displays any validation or file errors.
"""

import sys
import os
import pandas as pd
from functions import (
    load_and_validate_data,
    process_student_data,
    calculate_class_summary,
    calculate_subject_analysis,
    calculate_department_analysis,
    get_top_performers,
    save_results_to_csv,
    SUBJECT_COLUMNS,
    PASSING_MARK,
)


def print_divider(character: str = "=", length: int = 78) -> None:
    """Prints a clean divider line."""
    print(character * length)


def print_section_header(title: str) -> None:
    """Prints a styled section header."""
    print()
    print_divider("-", 78)
    print(f"  {title.upper()}")
    print_divider("-", 78)


def main():
    """Main execution function."""
    print_divider("=")
    print("        STUDENT PERFORMANCE ANALYTICS SYSTEM")
    print("             EWB Courses - Python with AI")
    print_divider("=")

    # 1. File paths setup
    input_file = "students.csv"
    output_file = "student_results.csv"

    # Allow custom input file via command-line argument if provided
    if len(sys.argv) > 1:
        input_file = sys.argv[1]

    print(f"[+] Looking for input dataset: '{input_file}'")

    # 2. Load and Validate Data (with Error Handling)
    try:
        raw_df = load_and_validate_data(input_file)
        print(f"[OK] Data loaded successfully! Found {len(raw_df)} valid student records.")
        print(f"[OK] Dataset schema and values verified without errors.")
    except FileNotFoundError:
        print(f"\n[ERROR] File '{input_file}' was not found.")
        print("Please make sure 'students.csv' exists in the project directory.")
        sys.exit(1)
    except ValueError as ve:
        print(f"\n[DATA VALIDATION ERROR] {ve}")
        sys.exit(1)
    except Exception as e:
        print(f"\n[UNEXPECTED ERROR] Failed to load data: {e}")
        sys.exit(1)

    # 3. Process Student Records
    print("[+] Processing student records (totals, averages, grades, pass/fail)...")
    processed_df = process_student_data(raw_df)

    # 4. Display Complete Student Records Table
    print_section_header("1. Individual Student Performance Summary")
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
    # Set pandas display options for neat terminal output
    pd.set_option("display.max_columns", None)
    pd.set_option("display.width", 1000)
    print(processed_df[display_cols].to_string(index=False))

    # 5. Overall Class Performance Summary
    class_summary = calculate_class_summary(processed_df)
    print_section_header("2. Class Performance Summary")
    print(f"  * Total Students Evaluated : {class_summary['total_students']}")
    print(f"  * Overall Class Average    : {class_summary['class_average']}%")
    print(f"  * Highest Average Score    : {class_summary['highest_average']}%")
    print(f"  * Lowest Average Score     : {class_summary['lowest_average']}%")
    print(f"  * Overall Average Attendance: {class_summary['average_attendance']}%")

    # 6. Pass / Fail Statistics
    print_section_header(f"3. Pass / Fail Analysis (Passing Rule: >= {PASSING_MARK} in each subject)")
    print(f"  * Students Passed          : {class_summary['pass_count']} ({class_summary['pass_percentage']}%)")
    print(f"  * Students Failed          : {class_summary['fail_count']} ({class_summary['fail_percentage']}%)")

    # If there are failed students, list them and why
    failed_students = processed_df[processed_df["Result"] == "Fail"]
    if not failed_students.empty:
        print("\n  Students requiring academic support:")
        for _, row in failed_students.iterrows():
            low_subjects = [
                f"{sub} ({row[sub]})" for sub in SUBJECT_COLUMNS if row[sub] < PASSING_MARK
            ]
            print(f"    - {row['Student_ID']} | {row['Name']:<18} | Subject(s) < {PASSING_MARK}: {', '.join(low_subjects)}")

    # 7. Subject-wise Analysis
    subject_stats, strongest_subject = calculate_subject_analysis(processed_df)
    print_section_header("4. Subject-wise Performance Analysis")
    header_str = f"  {'Subject':<16} {'Average':<10} {'Highest':<10} {'Lowest':<10}"
    print(header_str)
    print("  " + "-" * 46)
    for subj, stats in subject_stats.items():
        print(f"  {subj:<16} {stats['average']:<10.2f} {stats['highest']:<10.2f} {stats['lowest']:<10.2f}")
    print(f"\n  [!] Strongest Subject: '{strongest_subject}' (Highest Average: {subject_stats[strongest_subject]['average']}%)")

    # 8. Department-wise Analysis
    dept_df = calculate_department_analysis(processed_df)
    print_section_header("5. Department-wise Performance Analysis")
    print(dept_df.to_string(index=False))

    # 9. Top 3 Performers (Honor Roll)
    top_3_df = get_top_performers(processed_df, top_n=3)
    print_section_header("6. Top 3 Academic Performers (Honor Roll)")
    for rank, (_, row) in enumerate(top_3_df.iterrows(), start=1):
        print(f"  [Rank {rank}] {row['Name']} ({row['Student_ID']})")
        print(f"         Department: {row['Department']}")
        print(f"         Average: {row['Average_Marks']}% | Grade: {row['Grade']} | Status: {row['Result']}")

    # 10. Save Results to CSV
    print_section_header("7. Exporting Processed Data")
    try:
        save_results_to_csv(processed_df, output_file)
        print(f"[OK] Successfully saved processed results to '{output_file}'!")
        print(f"     Full Path: {os.path.abspath(output_file)}")
    except Exception as e:
        print(f"[!] Error saving to '{output_file}': {e}")

    print()
    print_divider("=")
    print("      ANALYSIS COMPLETE - REPORT GENERATED SUCCESSFULLY")
    print_divider("=")


if __name__ == "__main__":
    main()
