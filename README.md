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
├── python-core/                  # Core Python modules & data visualization
│   ├── arithmetic.py             # Arithmetic operations & modular functions
│   ├── main.py - main5.py        # Python programming exercises
│   ├── mat1.py - mat8.py         # Matplotlib charts & visualizations
│   ├── create_excel.py           # Automated Excel creation using openpyxl
│   ├── qs-world-rankings-2025.csv# Dataset: Global university rankings
│   ├── titanic.csv               # Dataset: Titanic passenger data
│   ├── students.xlsx             # Generated sample spreadsheet
│   └── ...
│
├── jupyter-notebooks/            # Interactive data analysis & lab experiments
│   └── sic.ipynb                 # Comprehensive SIC data exploration notebook
│
├── streamlit-dashboards/         # Interactive web applications & dashboards
│   ├── app.py                    # Multi-feature Streamlit web application
│   ├── universe_app.py           # Interactive data explorer application
│   ├── sic2.py - sic5.py         # Streamlit UI & widget exercises
│   ├── SIC_CnP_Ch08_Unit39.py   # Chapter 8 Streamlit lab implementation
│   ├── covid-vaccination-doses-per-capita.csv # Vaccination metrics dataset
│   ├── cosmos-desktop.png        # UI assets
│   ├── cosmos-mobile.png
│   └── ...
│
├── .gitignore                    # Clean Python, Jupyter, & Streamlit ignore rules
└── README.md                     # Project documentation
```

---

## 🚀 Key Modules & Highlights

### 1. 🐍 Core Python & Data Visualization (`/python-core`)
- **Foundations**: Modular Python architecture, functional programming, dynamic input parsing, and control structures.
- **Excel Automation**: Generating and formatting `.xlsx` workbooks programmatically with `openpyxl`.
- **Data Visualization**: Advanced charts using `matplotlib` and `pandas`:
  - Demographic breakdowns and survival distributions on the **Titanic dataset**.
  - Comparative institutional ranking plots on the **QS World Rankings (2025)**.

### 2. 📓 Jupyter Notebooks (`/jupyter-notebooks`)
- **Interactive Labs**: End-to-end data manipulation workflows, step-by-step algorithms, visual plots, and inline exploratory data analysis (EDA).
- **Notebook**: `sic.ipynb` consolidates coding exercises and statistical analysis into documented, reproducible cells.

### 3. 📊 Streamlit Dashboards (`/streamlit-dashboards`)
- **Interactive Web Apps**: Rapid web application development with real-time UI components, filters, and dynamic charting.
- **Data Dashboards**: Visualizing COVID-19 vaccination per capita metrics, custom analytics views, and responsive layout styling.

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
pip install pandas matplotlib openpyxl streamlit jupyter
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
jupyter notebook sic.ipynb
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
