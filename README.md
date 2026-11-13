# Samsung Innovation Campus (SIC) Portfolio

[![Python](https://img.shields.io/badge/Python-3.10%2B-blue.svg)](https://www.python.org/)
[![Streamlit](https://img.shields.io/badge/Streamlit-App-FF4B4B.svg)](https://streamlit.io/)
[![Jupyter](https://img.shields.io/badge/Jupyter-Notebook-F37626.svg)](https://jupyter.org/)
[![License](https://img.shields.io/badge/License-MIT-green.svg)](#)

A comprehensive portfolio showcasing projects, exercises, data analysis, and interactive dashboards developed as part of the **Samsung Innovation Campus (SIC) — Coding & Programming** program.

---

## 📁 Repository Structure

```text
samsung-innovation-campus-portfolio/
│
├── python-core/                                    # Core Python modules & data visualization
│   ├── arithmetic.py                               # Arithmetic operations & modular functions
│   ├── main.py - main5.py                          # Python programming exercises
│   ├── mat1.py - mat8.py                           # Matplotlib charts & visualizations
│   ├── create_excel.py                             # Automated Excel creation using openpyxl
│   ├── qs-world-rankings-2025.csv                  # Dataset: Global university rankings
│   ├── titanic.csv                                 # Dataset: Titanic passenger data
│   ├── students.xlsx                               # Generated sample spreadsheet
│   └── ...
│
├── jupyter-notebooks/                              # Jupyter Notebooks & Data Science Labs
│   ├── samsung_innovation_campus_dsa.ipynb        # Master SIC DSA & Python notebook
│   ├── python_lab_exercises.ipynb                  # Lab assignments: Calculator, Fibonacci, Lists, Sorting, File I/O
│   ├── student_performance_and_stock_eda.ipynb     # Comprehensive EDA on Student Performance & financial stock time-series
│   ├── data_structures_mastery.ipynb              # Deep-dive into Lists, Tuples, Dictionaries, Sets, 2D Matrices
│   ├── loops_patterns_and_number_algorithms.ipynb  # For/while loops, factorials, primes, Armstrong numbers
│   ├── conditionals_and_decision_making.ipynb      # Leap year, grades, boolean logic, conditionals
│   ├── groq_kannada_chatbot.ipynb                  # Groq LLM API + Gradio Chatbot with Kannada system prompt
│   ├── groq_llm_quickstart.ipynb                   # Groq API quickstart integration
│   ├── histogram_visualization.ipynb               # Histogram charting with Matplotlib
│   ├── file_word_counter.ipynb                     # File inspection & text processing
│   ├── string_typecasting_operations.ipynb         # String conversions & arithmetic
│   ├── triangle_area_math.ipynb                    # Equilateral triangle math calculations
│   ├── student-mat.csv                             # Accompanying dataset: Student performance metrics
│   └── book.json                                   # Accompanying dataset: JSON book records
│
├── streamlit-dashboards/                           # Interactive web applications & dashboards
│   ├── app.py                                      # Multi-feature Streamlit web application
│   ├── universe_app.py                             # Interactive data explorer application
│   ├── sic2.py - sic5.py                           # Streamlit UI & widget exercises
│   ├── SIC_CnP_Ch08_Unit39.py                     # Chapter 8 Streamlit lab implementation
│   ├── covid-vaccination-doses-per-capita.csv      # Vaccination metrics dataset
│   ├── cosmos-desktop.png                          # UI assets
│   ├── cosmos-mobile.png
│   └── ...
│
├── misc/                                           # Additional code snippets
│   └── hello_world.c                               # C language introductory program
│
├── .gitignore                                      # Clean Python, Jupyter, & Streamlit ignore rules
└── README.md                                       # Project documentation
```

---

## 📓 Jupyter Notebooks Breakdown

| Notebook | Program / Topic Description | Accompanying Dataset |
| :--- | :--- | :--- |
| **`samsung_innovation_campus_dsa.ipynb`** | Data Structures & Algorithms: Ciphers, Stack, Queue, Josephus sequence, Sorting (Bubble, Merge, Quick), Recursion (Tower of Hanoi, Tromino puzzle), Greedy & DP | — |
| **`python_lab_exercises.ipynb`** | Multi-problem lab set: Menu-driven Calculator, Age from DOB, Fibonacci series, Digit occurrences, File word counter, Marks descending bubble sort | — |
| **`student_performance_and_stock_eda.ipynb`** | Exploratory Data Analysis (EDA) on student demographics, absences, study time, boxplots, missing value imputation, and Yahoo Finance (`yfinance`) rolling averages | `student-mat.csv` |
| **`data_structures_mastery.ipynb`** | Comprehensive manipulation of Lists, Tuples, Dictionaries, Sets, Nested 2D Lists, deep copy vs shallow copy, and JSON loading | `book.json` |
| **`loops_patterns_and_number_algorithms.ipynb`** | Loop constructs, number summation, factorials, prime number filters, Armstrong number checks, and star/hash patterns | — |
| **`conditionals_and_decision_making.ipynb`** | Leap year evaluation, multi-condition grading system, discount rules, and logical operators | — |
| **`groq_kannada_chatbot.ipynb`** | AI Chatbot built using Groq API (`openai/gpt-oss-120b`) with Kannada persona and Gradio UI | — |
| **`groq_llm_quickstart.ipynb`** | Quickstart script for setting up Groq completions and Gradio interface | — |
| **`histogram_visualization.ipynb`** | Histogram generation and frequency distribution visualization with `matplotlib` | — |
| **`file_word_counter.ipynb`** | Text file inspection, line parsing, and word counting | — |
| **`string_typecasting_operations.ipynb`** | String typecasting, slicing, concatenation, and basic mathematical operations | — |
| **`triangle_area_math.ipynb`** | Geometric computation of equilateral triangle area using the `math` library | — |

---

## 🛠️ Getting Started

### 1. Clone the Repository
```bash
git clone https://github.com/jeevangowdahm/samsung-innovation-campus-portfolio.git
cd samsung-innovation-campus-portfolio
```

### 2. Set Up a Virtual Environment
```bash
python -m venv .venv
# Windows:
.venv\Scripts\activate
# macOS/Linux:
source .venv/bin/activate
```

### 3. Install Dependencies
```bash
pip install pandas matplotlib openpyxl streamlit jupyter seaborn yfinance gradio groq
```

---

## 💻 Running the Projects

### Running Core Python Scripts
```bash
cd python-core
python main.py
python mat1.py
python create_excel.py
```

### Launching Jupyter Notebooks
```bash
cd jupyter-notebooks
jupyter notebook
```

### Launching Streamlit Dashboards
```bash
cd streamlit-dashboards
streamlit run app.py
# or launch universe_app:
streamlit run universe_app.py
```

---

## 👤 Author
**Jeevan Gowda H M**
- GitHub: [@jeevangowdahm](https://github.com/jeevangowdahm)
- Program: Samsung Innovation Campus (SIC)
