# Student Performance Analytics System
## Project Documentation & Academic Report

---

### 1. Project Title and Student Details
- **Project Title:** Student Performance Analytics System
- **Student Name:** Parthiv Lella
- **Course:** Python with AI
- **Institution / Academy:** EWB Courses
- **Submission Date:** October 2026
- **GitHub Repository:** [https://github.com/parthivlella-ai/Student-Performance-Analytics.git](https://github.com/parthivlella-ai/Student-Performance-Analytics.git)

---

### 2. Objective
Educational institutions often handle large volumes of student grade sheets, subject scores, and attendance registers manually. Manual analysis is prone to human error, time-consuming, and does not provide fast insights into student strengths, weaknesses, or at-risk individuals.

The **Student Performance Analytics System** was developed to:
1. Automate the ingestion, validation, and processing of student academic records from CSV format.
2. Programmatically calculate key academic indicators including Total Marks, Average Marks, Letter Grades, and Pass/Fail status.
3. Deliver comprehensive descriptive statistics across subjects, departments, and class-wide distributions.
4. Detect students at risk (marks below the passing threshold of 35) to provide targeted academic support.
5. Provide top-performing students recognition through an automated honor roll.

---

### 3. Technologies Used
- **Programming Language:** Python 3.10+
- **Data Manipulation & Analysis:**
  - **Pandas:** For loading tabular CSV data into DataFrames, validating columns, grouping by department, and exporting analytical reports.
  - **NumPy:** For high-performance vectorized numerical operations (`np.sum`, `np.mean`, `np.max`, `np.min`, array boolean indexing).
- **Core Python Built-ins:**
  - Functions, loops (`for`, `iterrows`), conditional branching (`if-elif-else`), exception handling (`try-except-raise`), file I/O, string formatting.
- **Version Control & Collaboration:** Git and GitHub.

---

### 4. Dataset Description
The input dataset is stored in `students.csv`. It contains 20 individual student records with zero missing values and unique student identifiers.

#### Column Dictionary
| Column Name | Data Type | Description | Valid Range |
| :--- | :--- | :--- | :--- |
| `Student_ID` | String | Unique identifier for each student (STU101 - STU120) | Unique Alphanumeric |
| `Name` | String | Full name of the student | Alphabetic text |
| `Department` | String | Academic department (Computer Science, AI, IT, Data Science) | Categorical |
| `Python` | Integer / Float | Marks scored in Python programming | 0 to 100 |
| `Mathematics` | Integer / Float | Marks scored in Mathematics | 0 to 100 |
| `Statistics` | Integer / Float | Marks scored in Statistics | 0 to 100 |
| `Attendance` | Integer / Float | Class attendance percentage | 0 to 100% |

> **Note:** The input CSV strictly contains raw data. All derived metrics (`Total_Marks`, `Average_Marks`, `Grade`, `Result`) are computed dynamically by the Python application and exported to `student_results.csv`.

---

### 5. Implementation
The project follows a clean modular architecture separating reusable logic from application orchestration:

```text
student-performance-analytics/
|-- .gitignore                 # Excludes bytecode and cache files
|-- students.csv               # Input dataset (20 student records)
|-- student_results.csv        # Processed output dataset with grades & results
|-- functions.py               # Reusable business logic & statistical functions
|-- main.py                    # Program runner & terminal reporting interface
|-- README.md                  # Quickstart guide & repository overview
`-- Project_Documentation.md   # Comprehensive EWB Course project report
```

#### Step-by-Step Execution Workflow:
1. **Data Ingestion & Integrity Validation (`load_and_validate_data`):**
   - Validates existence of all 7 required columns.
   - Verifies there are no missing or `NaN` values.
   - Ensures all `Student_ID` entries are strictly unique.
   - Validates numeric boundaries ($0 \le \text{Marks, Attendance} \le 100$).
2. **Student Metrics Calculation (`process_student_data`):**
   - Iterates through the DataFrame using loops.
   - Calculates Total Marks via NumPy array sum.
   - Calculates Average Marks rounded to 2 decimal places.
   - Assigns letter grades using a documented grading scale.
   - Evaluates Pass/Fail status based on the individual subject passing mark ($\ge 35$).
3. **Class-wide & Subject-wise Aggregation (`calculate_class_summary`, `calculate_subject_analysis`):**
   - Evaluates overall class mean, highest average, lowest average, and attendance mean.
   - Calculates pass/fail headcounts and percentage ratios.
   - Computes subject-specific averages, min, and max, identifying the strongest academic subject.
4. **Departmental Comparison (`calculate_department_analysis`):**
   - Uses Pandas `.groupby("Department")` to compute average scores and headcounts per department.
5. **Honor Roll Extraction (`get_top_performers`):**
   - Ranks students by average marks in descending order and extracts the top 3.
6. **Data Export (`save_results_to_csv`):**
   - Exports the enriched DataFrame with all computed columns to `student_results.csv`.

---

### 6. Key Features
- **Strict Data Validation:** Prevents garbage-in, garbage-out errors by validating schema, duplicates, and range boundaries before processing.
- **Documented Grading Scale:**
  - $\ge 90\%$: **A+** (Outstanding)
  - $80\% - 89.99\%$: **A** (Excellent)
  - $70\% - 79.99\%$: **B** (Good)
  - $60\% - 69.99\%$: **C** (Average)
  - $50\% - 59.99\%$: **D** (Below Average)
  - $< 50\%$: **F** (Fail)
- **Strict Subject-wise Pass Criteria:** To pass, a student must secure $\ge 35$ in **every individual subject**.
- **At-Risk Identification:** Automatically identifies and lists students failing in any subject along with their specific deficit subjects.
- **Subject-wise & Department-wise Insights:** Highlights strongest/weakest subjects and compares department performance.
- **Automated CSV Export:** Generates an official report spreadsheet (`student_results.csv`) automatically.

---

### 7. Output / Terminal Execution Results

Running `python main.py` produces the following structured output:

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
  1. INDIVIDUAL STUDENT PERFORMANCE SUMMARY
------------------------------------------------------------------------------
Student_ID            Name              Department  Python  Mathematics  Statistics  Attendance  Total_Marks  Average_Marks Grade Result
    STU101    Aarav Sharma        Computer Science      88           92          85          92        265.0          88.33     A   Pass
    STU102      Diya Patel        Computer Science      75           80          78          88        233.0          77.67     B   Pass
    STU103     Rohan Verma            Data Science      94           89          96          95        279.0          93.00    A+   Pass
    STU104     Ananya Iyer Artificial Intelligence      62           58          65          82        185.0          61.67     C   Pass
    STU105     Kabir Singh  Information Technology      45           52          48          74        145.0          48.33     F   Pass
    STU106      Neha Gupta        Computer Science      91           95          90          96        276.0          92.00    A+   Pass
    STU107 Vikram Malhotra            Data Science      28           42          39          70        109.0          36.33     F   Fail
    STU108      Pooja Nair Artificial Intelligence      82           78          84          90        244.0          81.33     A   Pass
    STU109    Aditya Joshi  Information Technology      56           60          54          78        170.0          56.67     D   Pass
    STU110  Meera Kulkarni        Computer Science      98           96          99          98        293.0          97.67    A+   Pass
    STU111   Siddharth Rao            Data Science      38           32          45          65        115.0          38.33     F   Fail
    STU112  Tanvi Deshmukh Artificial Intelligence      72           76          70          86        218.0          72.67     B   Pass
    STU113     Karan Mehta  Information Technology      68           70          64          80        202.0          67.33     C   Pass
    STU114        Riya Sen        Computer Science      85           88          82          91        255.0          85.00     A   Pass
    STU115   Harsh Vardhan            Data Science      52           49          55          72        156.0          52.00     D   Pass
    STU116      Ishita Roy Artificial Intelligence      30           55          50          60        135.0          45.00     F   Fail
    STU117    Varun Chopra  Information Technology      79           84          81          89        244.0          81.33     A   Pass
    STU118    Sneha Pillai        Computer Science      87           83          88          94        258.0          86.00     A   Pass
    STU119    Manish Yadav            Data Science      42           38          40          71        120.0          40.00     F   Pass
    STU120    Priyanka Das Artificial Intelligence      90           91          89          93        270.0          90.00    A+   Pass

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

  Students requiring academic support:
    - STU107 | Vikram Malhotra    | Subject(s) < 35: Python (28)
    - STU111 | Siddharth Rao      | Subject(s) < 35: Mathematics (32)
    - STU116 | Ishita Roy         | Subject(s) < 35: Python (30)

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
  5. DEPARTMENT-WISE PERFORMANCE ANALYSIS
------------------------------------------------------------------------------
             Department  Student_Count  Average_Marks  Average_Attendance
       Computer Science              6          87.78               93.17
Artificial Intelligence              5          70.13               82.20
 Information Technology              4          63.42               80.25
           Data Science              5          51.93               74.60

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
     Full Path: c:\Users\parth\OneDrive\Desktop\student-performance-analytics\student_results.csv

==============================================================================
      ANALYSIS COMPLETE - REPORT GENERATED SUCCESSFULLY
==============================================================================
```

---

### 8. Final Outcome
- The project successfully met 100% of the assignment objectives outlined in the EWB Courses assignment specification.
- Clean separation of concerns between computational logic (`functions.py`) and presentation (`main.py`).
- Correct numerical calculations verified with NumPy and Pandas.
- Robust error handling protecting the program against invalid or corrupt input data.
- The output CSV file `student_results.csv` is correctly populated with all required columns.

---

### 9. Challenges & Learning
1. **Terminal Character Encoding on Windows:**
   - *Problem:* Initial use of UTF-8 checkmarks (`✓`) and medal emojis triggered a `UnicodeEncodeError` under Windows console's standard CP1252 codepage.
   - *Solution:* Replaced non-ASCII characters with clean, cross-platform ASCII indicators (`[OK]`, `[Rank 1]`, `[*]`) to guarantee universal portability.
2. **Strict Pass/Fail Logic Across All Subjects:**
   - *Problem:* A simple average threshold (e.g. average $\ge 40$) could pass a student who scored poorly in one critical subject.
   - *Solution:* Implemented subject-wise validation checking that every individual score satisfies $\ge 35$, correctly categorizing students with isolated low scores into the academic support list.
3. **NumPy Vectorization vs. Beginner Readability:**
   - *Learning:* Balanced performance and educational clarity by using NumPy arrays for numerical calculations while employing readable Python loops and functions to make the logic accessible to beginners.

---

### 10. GitHub Repository
- **Repository URL:** [https://github.com/parthivlella-ai/Student-Performance-Analytics.git](https://github.com/parthivlella-ai/Student-Performance-Analytics.git)
- **Branch:** `main`
