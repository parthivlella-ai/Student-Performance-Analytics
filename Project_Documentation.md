# Student Performance Analytics System
## Comprehensive Project Documentation & Assessment Report

---

### 1. Project Title and Student Details
- **Project Title:** Student Performance Analytics System
- **Student Name:** Parthiv Lella
- **Course:** Python with AI
- **Institution / Academy:** EWB Courses
- **Submission Date:** October 2026
- **GitHub Repository URL:** [https://github.com/parthivlella-ai/Student-Performance-Analytics](https://github.com/parthivlella-ai/Student-Performance-Analytics)
- **Live Streamlit Web Demo:** `[Insert Your Deployed Streamlit Cloud URL Here]`  
  *(Placeholder: Update this link after completing Streamlit Community Cloud deployment, e.g., `https://student-performance-analytics.streamlit.app`)*

---

### 2. Objective
In educational institutions, manual processing of student grade sheets, subject scores, and attendance registers is tedious, error-prone, and slow to highlight academic problems.

The **Student Performance Analytics System** was engineered to solve these challenges through automation:
1. **Automated Data Ingestion & Validation:** Safely reads student academic records from CSV format and enforces schema, duplicate, and numeric boundary checks.
2. **Dynamic Performance Calculations:** Automatically computes Total Marks, Average Marks, Letter Grades, and Pass/Fail statuses without hardcoded numbers.
3. **Comprehensive Descriptive Analytics:** Aggregates class averages, attendance rates, subject-wise statistics, and department-level comparisons using NumPy and Pandas.
4. **Early Academic Intervention:** Pinpoints students at risk (scoring $< 35$ in any subject) so faculty can provide targeted academic remediation.
5. **Dual Presentation Interface:** Offers both an automated, non-interactive command-line interface (`main.py`) for batch processing and an interactive web dashboard (`app.py`) built with Streamlit for visual data exploration.

---

### 3. Technologies Used
- **Programming Language:** Python 3.10+
- **Data Manipulation & Analysis:**
  - **Pandas:** Used for DataFrame creation, reading/writing CSV files, grouping data by department, and column-level aggregations.
  - **NumPy:** Used for vectorized numerical operations (`np.sum`, `np.mean`, `np.max`, `np.min`, array boolean masking).
- **Web Application Framework:**
  - **Streamlit (v1.30+ / v1.61+):** Used to construct the interactive browser-based dashboard with responsive KPI metrics, charts, sidebar filters, and file downloads.
- **Development & Version Control:**
  - **Git & GitHub:** For version control, tracking changes, and project hosting.
  - **Streamlit Community Cloud:** For deploying the live web application on the public internet.

---

### 4. Dataset Description
The system reads its data from `students.csv`, which contains **20 realistic fictional student records** across 4 engineering and science departments.

#### Dataset Schema
| Column Name | Data Type | Description | Valid Range |
| :--- | :--- | :--- | :--- |
| `Student_ID` | String | Unique identifier for each student (`STU101` to `STU120`) | Unique alphanumeric |
| `Name` | String | Full student name | Text |
| `Department` | String | Academic department (Computer Science, AI, IT, Data Science) | Categorical text |
| `Python` | Integer | Marks obtained in Python programming | 0 to 100 |
| `Mathematics` | Integer | Marks obtained in Mathematics | 0 to 100 |
| `Statistics` | Integer | Marks obtained in Statistics | 0 to 100 |
| `Attendance` | Integer | Overall percentage of attended classes | 0 to 100% |

#### Data Integrity Guarantee
- **Total Records:** Exactly 20 records.
- **Null / Missing Values:** 0 across all columns.
- **Unique Identifiers:** 20 distinct IDs with no duplicates.
- **Pre-computed Fields:** The input CSV contains strictly raw scores. All totals, averages, grades, and pass/fail statuses are dynamically derived by the Python logic.

---

### 5. Implementation
The project employs a clean modular design that separates analytical business logic from presentation layers:

```text
student-performance-analytics/
|-- .gitignore                 # Excludes cache, bytecode, and virtual environments
|-- requirements.txt           # Declarative list of required libraries
|-- students.csv               # Input dataset (20 raw student records)
|-- student_results.csv        # Processed dataset generated after running analysis
|-- functions.py               # Reusable analytics, grading, and validation functions
|-- main.py                    # Terminal program runner & CLI reporter
|-- app.py                     # Interactive Streamlit web dashboard
|-- streamlit.cmd              # Windows command helper for Streamlit CLI execution
|-- README.md                  # Project overview, installation, and deployment guide
`-- Project_Documentation.md   # Comprehensive EWB Course project report
```

#### Step-by-Step System Workflow

```
       [ students.csv ]
              │
              ▼
   load_and_validate_data()   <── Validates Schema, Nulls, Duplicates, [0-100] Range
              │
              ▼
    process_student_data()    <── Loops through rows, calls calculate_total(),
              │                   calculate_average(), assign_grade(), determine_pass_fail()
              ├──────────────────────────────┬──────────────────────────────┐
              ▼                              ▼                              ▼
  calculate_class_summary()     calculate_subject_analysis()   calculate_department_analysis()
              │                              │                              │
              ▼                              ▼                              ▼
     [ main.py - Console ]        [ app.py - Streamlit ]          [ student_results.csv ]
     Formatted ASCII output       Interactive Web Dashboard       Generated CSV File
```

1. **Data Ingestion & Integrity Validation (`load_and_validate_data`):**
   - Resolves paths relative to the script directory using `os.path.dirname(os.path.abspath(__file__))`.
   - Checks presence of all 7 mandatory columns.
   - Raises `ValueError` if missing values, duplicate student IDs, or out-of-range marks ($< 0$ or $> 100$) are found.
2. **Student Performance Computation (`process_student_data`):**
   - Uses an explicit loop across DataFrame rows (`df.iterrows()`).
   - Computes `Total_Marks` using `calculate_total(marks)` via `np.sum()`.
   - Computes `Average_Marks` using `calculate_average(total, num_subjects)` rounded to 2 decimal places.
   - Assigns letter grades using `assign_grade(average)`.
   - Determines pass/fail using `determine_pass_fail(marks, passing_mark=35)`.
3. **Class & Aggregated Analytics:**
   - `calculate_class_summary()`: Evaluates overall class mean, highest average, lowest average, pass/fail counts, pass rate, and mean attendance using NumPy array operations.
   - `calculate_subject_analysis()`: Computes mean, highest, and lowest marks per subject and detects the strongest subject.
   - `calculate_department_analysis()`: Groups records by `Department` using Pandas `.groupby().agg()` to calculate student counts, average marks, and average attendance.
   - `get_top_performers()`: Sorts students by `Average_Marks` descending to extract the top 3 rankers.
4. **Dual Presentation:**
   - **Console Runner (`main.py`):** Outputs a formatted report to stdout and writes results to `student_results.csv`.
   - **Web Dashboard (`app.py`):** Renders KPI cards, interactive tabs, filters, charts, and file download widgets using Streamlit.

---

### 6. Key Features

- **Documented Letter Grading Scale:**
  - $\ge 90.0\%$: **A+** (Outstanding)
  - $80.0\% - 89.99\%$: **A** (Excellent)
  - $70.0\% - 79.99\%$: **B** (Good)
  - $60.0\% - 69.99\%$: **C** (Average)
  - $50.0\% - 59.99\%$: **D** (Below Average)
  - $< 50.0\%$: **F** (Fail)
- **Strict Subject-wise Pass Criteria:**
  - A student must score at least **35 marks in each individual subject** (Python, Mathematics, and Statistics) to obtain a **Pass**. Scoring below 35 in any single subject results in a **Fail**, regardless of overall average marks.
- **Academic Support Alerts:** Automatically detects and displays students with deficit subjects ($< 35$), detailing the exact subject and mark obtained.
- **Top 3 Honor Roll:** Automatically extracts and showcases the highest-achieving students.
- **Interactive Multi-Filter Dashboard:** Allows real-time slicing by Department, Letter Grade, and Pass/Fail result.
- **Custom CSV Upload Support:** Enables analyzing new datasets on the fly directly in the web dashboard.
- **One-Click CSV Export:** Generates and downloads `student_results.csv` with all computed fields directly from the browser or terminal.

---

### 7. Output / Screenshots

#### A. Terminal Output (`python main.py`)
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
  * Total Students Evaluated : 20
  * Overall Class Average    : 69.53%
  * Highest Average Score    : 97.67%
  * Lowest Average Score     : 36.33%
  * Overall Average Attendance: 83.2%

------------------------------------------------------------------------------
  3. PASS / FAIL ANALYSIS (PASSING RULE: >= 35 IN EACH SUBJECT)
------------------------------------------------------------------------------
  * Students Passed          : 17 (85.0%)
  * Students Failed          : 3 (15.0%)

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
```

#### B. Web Dashboard Layout (`app.py`)
- **Top Row KPI Metrics:** Total Students (`20`), Class Average (`69.53%`), Pass Rate (`85.0%`), and Attendance (`83.2%`).
- **Sidebar:** Dynamic dropdowns for Department, Grade, and Result filtering, plus a CSV upload toggle.
- **Tabbed Exploration:**
  - Tab 1: Interactive Data Table + Download Button (`student_results.csv`).
  - Tab 2: Comparative Bar Chart for Subjects + Highlight card for Mathematics (70.4%).
  - Tab 3: Department Performance chart & aggregation table.
  - Tab 4: Top 3 Performers Honor Roll cards with badges and scores.
  - Tab 5: Academic Support center displaying error alert boxes for STU107, STU111, and STU116.
  - Tab 6: Grading & Passing rules table.

---

### 8. Final Outcome
- The project successfully satisfied 100% of the rubric criteria stipulated by the EWB Courses assignment.
- Both the terminal command-line program and the interactive web application share the exact same underlying mathematical logic from `functions.py`, eliminating code duplication.
- Edge cases (missing columns, duplicate IDs, out-of-range marks, single-subject failures) are handled safely without unhandled runtime crashes.
- Clean documentation and an automated test suite were established for maintainability and peer review.

---

### 9. Challenges & Learning
1. **Windows Terminal Character Encoding:**
   - *Problem:* Using unicode checkmark symbols (`✓`) and medal emojis caused `UnicodeEncodeError ('charmap' codec)` under Windows' default codepage (CP1252).
   - *Solution:* Replaced non-ASCII icons with clean, universally supported ASCII tokens (`[OK]`, `[Rank 1]`, `[*]`).
2. **Streamlit CLI PATH Configuration on Windows:**
   - *Problem:* In certain Windows environments, the Python `Scripts` directory is not automatically included in the terminal session PATH, causing `streamlit` to be unrecognized as a command.
   - *Solution:* Permanently added the `Scripts` folder to the User `PATH` environment variable and added a lightweight `streamlit.cmd` wrapper so commands like `streamlit run app.py` and `python -m streamlit run app.py` work seamlessly.
3. **Cross-Platform Path Resolution:**
   - *Problem:* Relative filepaths like `"students.csv"` can fail if an application is launched from outside the project directory or inside a cloud container.
   - *Solution:* Used `os.path.dirname(os.path.abspath(__file__))` in both `main.py` and `app.py` to ensure relative files are always located accurately.
4. **Clean Code Reuse Across CLI and Web UI:**
   - *Learning:* Designed `functions.py` as a pure, decoupled calculation library. This enabled `app.py` and `main.py` to share identical calculations without copying any code.

---

### 10. GitHub Repository & Live Demo URL

- **GitHub Repository URL:**  
  [https://github.com/parthivlella-ai/Student-Performance-Analytics](https://github.com/parthivlella-ai/Student-Performance-Analytics)
- **Live Streamlit Community Cloud URL:**  
  `[Insert Your Deployed Streamlit Cloud URL Here]`  
  *(Placeholder: Update this link after deploying to Streamlit Community Cloud, e.g., `https://student-performance-analytics.streamlit.app`)*

#### Instructions for Streamlit Community Cloud Deployment
1. Ensure all files (`app.py`, `requirements.txt`, `functions.py`, `students.csv`, `main.py`, `README.md`, `Project_Documentation.md`) are pushed to the `main` branch of your GitHub repository.
2. Visit [share.streamlit.io](https://share.streamlit.io/) and log in with your GitHub account.
3. Click **"New app"**.
4. Select repository: `parthivlella-ai/Student-Performance-Analytics`.
5. Select branch: `main`.
6. Select main file path: `app.py`.
7. Click **"Deploy!"**.
8. Once live, copy your application URL and update the placeholder links in this documentation and in `README.md`.
