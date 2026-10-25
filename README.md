# Student Performance Analytics System

A Python-based academic data analytics system that loads student records from a CSV dataset, validates data integrity, and calculates key metrics including total marks, average marks, letter grades, pass/fail results, class summaries, subject-wise statistics, and department-level insights using **Python**, **NumPy**, and **Pandas**.

Developed as an individual project assignment for the **Python with AI** program at **EWB Courses**.

---

## Repository Contents

```text
student-performance-analytics/
|-- .gitignore                 # Standard Python gitignore
|-- students.csv               # Input dataset (20 fictional student records)
|-- student_results.csv        # Generated output with computed grades & results
|-- functions.py               # Reusable analytics, grading, and validation functions
|-- main.py                    # Main program runner and terminal reporting script
|-- Project_Documentation.md   # Complete 10-section project documentation report
`-- README.md                  # Project overview and setup instructions
```

---

## Key Features

1. **Robust Data Validation**: Checks for missing columns, null values, duplicate Student IDs, and validates that scores and attendance fall within the 0–100 range.
2. **Student Performance Metrics**: Calculates total marks and average marks for every student using NumPy numerical functions.
3. **Documented Grading System**:
   - **A+ (Outstanding)**: $\ge 90\%$
   - **A (Excellent)**: $80\% - 89.99\%$
   - **B (Good)**: $70\% - 79.99\%$
   - **C (Average)**: $60\% - 69.99\%$
   - **D (Below Average)**: $50\% - 59.99\%$
   - **F (Fail)**: $< 50\%$
4. **Subject-wise Pass/Fail Rule**: A student must score at least **35 marks in each individual subject** (Python, Mathematics, Statistics) to pass.
5. **Class Performance Analytics**: Computes overall class average, highest/lowest scores, and average attendance.
6. **Subject Analysis**: Evaluates each subject's average, highest, and lowest mark, identifying the strongest subject.
7. **Department Analysis**: Groups performance metrics across academic departments.
8. **Honor Roll**: Identifies and highlights the top 3 academic performers.
9. **Automatic CSV Export**: Automatically exports full calculated results to `student_results.csv`.

---

## Quickstart & Installation

### 1. Prerequisites
Make sure you have Python 3.10+ installed along with `pandas` and `numpy`:

```bash
pip install pandas numpy
```

### 2. Clone the Repository
```bash
git clone https://github.com/parthivlella-ai/Student-Performance-Analytics.git
cd Student-Performance-Analytics
```

### 3. Run the Analytics System
```bash
python main.py
```

---

## Sample Output

```text
==============================================================================
        STUDENT PERFORMANCE ANALYTICS SYSTEM
             EWB Courses - Python with AI
==============================================================================
[+] Looking for input dataset: 'students.csv'
[OK] Data loaded successfully! Found 20 valid student records.
[OK] Dataset schema and values verified without errors.
[+] Processing student records (totals, averages, grades, pass/fail)...

------------------------------------------------------------------------------
  2. CLASS PERFORMANCE SUMMARY
------------------------------------------------------------------------------
  * Total Students Evaluated  : 20
  * Overall Class Average     : 69.53%
  * Highest Average Score     : 97.67%
  * Lowest Average Score      : 36.33%
  * Overall Average Attendance: 83.2%

------------------------------------------------------------------------------
  3. PASS / FAIL ANALYSIS (PASSING RULE: >= 35 IN EACH SUBJECT)
------------------------------------------------------------------------------
  * Students Passed           : 17 (85.0%)
  * Students Failed           : 3 (15.0%)

------------------------------------------------------------------------------
  4. SUBJECT-WISE PERFORMANCE ANALYSIS
------------------------------------------------------------------------------
  Subject          Average    Highest    Lowest    
  ----------------------------------------------
  Python           68.10      98.00      28.00     
  Mathematics      70.40      96.00      32.00     
  Statistics       70.10      99.00      39.00     

  [!] Strongest Subject: 'Mathematics' (Highest Average: 70.4%)

------------------------------------------------------------------------------
  6. TOP 3 ACADEMIC PERFORMERS (HONOR ROLL)
------------------------------------------------------------------------------
  [Rank 1] Meera Kulkarni (STU110)
         Department: Computer Science
         Average: 97.67% | Grade: A+ | Status: Pass
  [Rank 2] Rohan Verma (STU103)
         Department: Data Science
         Average: 93.0% | Grade: A+ | Status: Pass
  [Rank 3] Neha Gupta (STU106)
         Department: Computer Science
         Average: 92.0% | Grade: A+ | Status: Pass

------------------------------------------------------------------------------
  7. EXPORTING PROCESSED DATA
------------------------------------------------------------------------------
[OK] Successfully saved processed results to 'student_results.csv'!
```

---

## Project Documentation

For the complete 10-section assessment submission report, refer to [Project_Documentation.md](Project_Documentation.md).

---

## Student Details
- **Student Name:** Parthiv Lella
- **Course:** Python with AI
- **Academy:** EWB Courses
- **GitHub:** [parthivlella-ai](https://github.com/parthivlella-ai)
