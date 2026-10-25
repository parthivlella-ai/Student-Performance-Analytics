# Student Performance Analytics System

A dual-interface academic data analytics system that loads student records from a CSV dataset, validates data integrity, and calculates key metrics including total marks, average marks, letter grades, pass/fail results, class summaries, subject-wise statistics, and department-level insights using **Python**, **NumPy**, **Pandas**, and **Streamlit**.

Developed as an individual project assignment for the **Python with AI** program at **EWB Courses**.

---

## Live Demo & Repository Links

- **GitHub Repository:** [https://github.com/parthivlella-ai/Student-Performance-Analytics](https://github.com/parthivlella-ai/Student-Performance-Analytics)
- **Live Streamlit Web App:** `[Insert Your Deployed Streamlit Cloud URL Here]`  
  *(Placeholder: Replace with your Streamlit Community Cloud URL after deployment, e.g., `https://student-performance-analytics.streamlit.app`)*

---

## Project Interfaces

This project provides two distinct interfaces sharing the same computational backend:

1. **Terminal Application (`main.py`)**: A command-line program that executes the entire analytical pipeline, prints formatted ASCII tables and statistical summaries to the console, and exports processed results to `student_results.csv`.
2. **Interactive Web Dashboard (`app.py`)**: A browser-based dashboard built with Streamlit featuring real-time KPI metrics, interactive multi-column filters, comparative charts, an academic support alert center, an honor roll showcase, and direct CSV download capabilities.

---

## Repository Structure

```text
student-performance-analytics/
|-- .gitignore                 # Excludes bytecode, environments, and cache files
|-- requirements.txt           # Project dependencies for local setup & Streamlit Cloud
|-- students.csv               # Input dataset (20 fictional student records, 7 columns)
|-- student_results.csv        # Generated output dataset with computed grades & results
|-- functions.py               # Reusable analytics, grading, and validation functions
|-- main.py                    # Terminal program runner & reporting interface
|-- app.py                     # Streamlit web dashboard application
|-- streamlit.cmd              # Windows CLI wrapper for streamlit execution
|-- Project_Documentation.md   # Complete 10-section project assessment report
`-- README.md                  # Project overview, installation, and deployment guide
```

---

## Dataset Description

The system processes student data from `students.csv`, containing **20 student records** across **7 required columns** with no missing values:

| Column Name | Data Type | Description | Range |
| :--- | :--- | :--- | :--- |
| `Student_ID` | String | Unique identifier (`STU101` to `STU120`) | Unique alphanumeric |
| `Name` | String | Student's full name | Text |
| `Department` | String | Academic department | Computer Science, AI, IT, Data Science |
| `Python` | Integer | Marks scored in Python | 0 to 100 |
| `Mathematics` | Integer | Marks scored in Mathematics | 0 to 100 |
| `Statistics` | Integer | Marks scored in Statistics | 0 to 100 |
| `Attendance` | Integer | Class attendance percentage | 0 to 100% |

> **Note:** The input dataset contains only raw scores. All metrics (`Total_Marks`, `Average_Marks`, `Grade`, `Result`) are calculated dynamically by the Python backend.

---

## Grading and Pass / Fail Rules

### 1. Letter Grading Scale
Letter grades are assigned based on the calculated **Average Marks**:

| Average Marks Range | Grade | Classification |
| :--- | :---: | :--- |
| $90.0\%$ to $100.0\%$ | **A+** | Outstanding |
| $80.0\%$ to $89.99\%$ | **A** | Excellent |
| $70.0\%$ to $79.99\%$ | **B** | Good |
| $60.0\%$ to $69.99\%$ | **C** | Average |
| $50.0\%$ to $59.99\%$ | **D** | Below Average |
| Below $50.0\%$ | **F** | Fail |

### 2. Pass / Fail Criteria
- **Individual Subject Passing Rule:** A student must score at least **35 marks in EVERY subject** (Python, Mathematics, and Statistics) to obtain a **Pass** result.
- **Single-Subject Failure Rule:** If a student scores below 35 in even one subject, their overall result is **Fail**, regardless of how high their average marks may be.
- **Attendance Guideline:** Minimum recommended attendance is 75%.

---

## Installation & Setup

### 1. Prerequisites
- Python 3.10 or higher installed.
- Git installed.

### 2. Clone the Repository
```bash
git clone https://github.com/parthivlella-ai/Student-Performance-Analytics.git
cd Student-Performance-Analytics
```

### 3. Install Dependencies
Install all required libraries using `requirements.txt`:
```bash
pip install -r requirements.txt
```

---

## How to Run

### Option A: Run the Terminal Application
To run the full analytical pipeline in your terminal:
```bash
python main.py
```
This will validate `students.csv`, compute all metrics, display the formatted report sections in your console, and save `student_results.csv`.

### Option B: Run the Web Dashboard Locally
To launch the interactive Streamlit dashboard:
```bash
streamlit run app.py
```
*(Or on Windows: `python -m streamlit run app.py`)*

After running the command, Streamlit will start its local web server and output:
```text
  You can now view your Streamlit app in your browser.

  Local URL: http://localhost:8501
  Network URL: http://192.168.x.x:8501
```
Open **`http://localhost:8501`** in your web browser to explore the dashboard. To stop the server, press `Ctrl + C` in your terminal.

---

## Web Dashboard Features

- **KPI Metric Summary Cards**: Displays real-time metrics for Total Students (20), Class Average (69.53%), Pass Percentage (85.0%), and Average Attendance (83.2%).
- **Interactive Multi-Factor Filters**: Filter student records by Department, Letter Grade, and Pass/Fail status.
- **Custom CSV Upload**: Option to analyze the default `students.csv` or upload a custom CSV file with automatic integrity validation.
- **Interactive Student Table**: Sortable and searchable table showing all calculated values.
- **Subject Analytics & Charts**: Bar charts comparing Python, Mathematics, and Statistics averages, highlighting the strongest subject (*Mathematics at 70.4%*).
- **Department Performance**: Departmental comparison table and average mark charts.
- **Academic Honor Roll**: Visual cards highlighting the top 3 academic performers (*Meera Kulkarni*, *Rohan Verma*, and *Neha Gupta*).
- **Academic Support Center**: Alerts identifying students who scored below 35 in any subject, clearly listing the specific deficit subjects.
- **One-Click CSV Export**: Download the complete processed dataset (`student_results.csv`) directly from the browser.

---

## Deployment on Streamlit Community Cloud

Follow these steps to deploy this repository live on the web for free:

1. **Push Changes to GitHub**: Ensure all project files (`app.py`, `requirements.txt`, `functions.py`, `students.csv`, `main.py`) are committed and pushed to your GitHub repository.
2. **Sign in to Streamlit Cloud**: Go to [share.streamlit.io](https://share.streamlit.io/) and sign in with your GitHub account.
3. **Create New App**:
   - Click **"Create app"** (or **"New app"**).
   - Select your repository: `parthivlella-ai/Student-Performance-Analytics`.
   - Set Branch: `main`.
   - Set Main file path: `app.py`.
4. **Deploy**: Click **"Deploy!"**.
5. Streamlit Community Cloud will read `requirements.txt`, install dependencies, and launch your live application at a public URL (e.g., `https://<your-app-name>.streamlit.app`).
6. **Update Links**: Copy your live app URL and paste it into the placeholder at the top of this `README.md` and in your EWB submission form.

---

## Testing & Verification Results

All calculations and pipeline functions were verified with automated tests:

| Component | Test Performed | Result |
| :--- | :--- | :---: |
| **Terminal Runner** | `python main.py` executed end-to-end | **PASS** (Exit code 0) |
| **Web Server** | `streamlit run app.py` launched & HTTP checked | **PASS** (HTTP 200 OK on port 8501) |
| **Data Integrity** | Checked 20 records, unique IDs, range bounds | **PASS** (0 errors) |
| **Calculations** | Verified Total, Average, Grade, Result against dataset | **PASS** (100% accurate) |
| **Subject Analytics** | Verified Python (68.10%), Math (70.40%), Stats (70.10%) | **PASS** (Math identified as strongest) |
| **Deficit Flagging** | Flagged STU107 (Python 28), STU111 (Math 32), STU116 (Python 30) | **PASS** (3 failed students identified) |
| **CSV Download** | Verified exported byte stream schema and values | **PASS** (Matches `student_results.csv`) |

---

## Student & Course Details
- **Student Name:** Parthiv Lella
- **Course:** Python with AI
- **Institution:** EWB Courses
- **GitHub Repository:** [https://github.com/parthivlella-ai/Student-Performance-Analytics](https://github.com/parthivlella-ai/Student-Performance-Analytics)
