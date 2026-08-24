<div align="center">

<img src="assets/header.svg" width="900" alt="Pandas Analyzer Header"/>

</div>

---

<div align="center">

![Python](https://img.shields.io/badge/Python-3.8%2B-00FF41?style=for-the-badge&logo=python&logoColor=00FF41&labelColor=0D0D0D&color=003B00)
![Pandas](https://img.shields.io/badge/Pandas-2.x-00E5FF?style=for-the-badge&logo=pandas&logoColor=00E5FF&labelColor=0D0D0D&color=001A2E)
![NumPy](https://img.shields.io/badge/NumPy-1.x-BD00FF?style=for-the-badge&logo=numpy&logoColor=BD00FF&labelColor=0D0D0D&color=1A0030)
![Matplotlib](https://img.shields.io/badge/Matplotlib-3.x-FFD700?style=for-the-badge&logo=python&logoColor=FFD700&labelColor=0D0D0D&color=2A2000)
![Seaborn](https://img.shields.io/badge/Seaborn-0.x-FF4500?style=for-the-badge&logo=python&logoColor=FF4500&labelColor=0D0D0D&color=2A0A00)
![Jupyter](https://img.shields.io/badge/Jupyter-Notebook-FF6B35?style=for-the-badge&logo=jupyter&logoColor=FF6B35&labelColor=0D0D0D&color=2A1500)

</div>

---

<div align="center">

<img src="assets/metrics.svg" width="900" alt="Project Metrics"/>

</div>

---

## `// 01` · OVERVIEW

<div align="center">

<img src="assets/pipeline.svg" width="900" alt="Data Pipeline"/>

</div>

> A comprehensive **Sales Data Analysis & Visualization** tool built in Python.
> Encapsulates all data science operations inside a single `SalesDataFrame` class —
> from raw CSV ingestion to advanced statistical analysis, multi-library visualization,
> and interactive menu-driven user interface. Built for academic excellence and real-world applicability.

---

## `// 02` · FEATURES

<div align="center">

<img src="assets/features.svg" width="900" alt="Features Grid"/>

</div>

---

## `// 03` · VISUALIZATION GALLERY

<div align="center">

<img src="assets/charts_row1.svg" width="900" alt="Bar Chart · Line Chart · Heatmap"/>

<img src="assets/charts_row2.svg" width="900" alt="Scatter Plot · Pie Chart"/>

</div>

---

## `// 04` · CLASS ARCHITECTURE

<div align="center">

<img src="assets/architecture.svg" width="900" alt="SalesDataFrame Class Architecture"/>

</div>

---

## `// 05` · TECH STACK

<div align="center">

<img src="assets/techstack.svg" width="900" alt="Tech Stack"/>

</div>

---

## `// 06` · DATASET SCHEMA

<div align="center">

<img src="assets/schema.svg" width="900" alt="Dataset Schema"/>

</div>

---

## `// 07` · INSTALLATION

```bash
# Navigate to project directory
cd visualizer/

# Install dependencies
pip install pandas numpy matplotlib seaborn jupyter

# Run the CLI program
python sales_data_analyzer.py

# Launch Jupyter Notebook
jupyter notebook sales_data_analyzer.ipynb
```

---

## `// 08` · CONSOLE INTERACTION

<div align="center">

<img src="assets/terminal.svg" width="900" alt="Console Interaction"/>

</div>

---

## `// 09` · PROJECT STRUCTURE

```
visualizer/
│
├── 📓 sales_data_analyzer.ipynb    ← Jupyter Notebook (cell-by-cell execution)
├── 🐍 sales_data_analyzer.py       ← CLI Python program (menu-driven)
│
├── 📁 assets/                      ← SVG graphic assets for README
│   ├── header.svg
│   ├── metrics.svg
│   ├── pipeline.svg
│   ├── features.svg
│   ├── charts_row1.svg
│   ├── charts_row2.svg
│   ├── architecture.svg
│   ├── techstack.svg
│   ├── schema.svg
│   ├── terminal.svg
│   ├── flow.svg
│   ├── oop.svg
│   └── footer.svg
│
└── 📁 data/
    └── 📄 sales_data.csv           ← Synthetic dataset (200 rows × 5 cols)
```

---

## `// 10` · PROGRAM FLOW

<div align="center">

<img src="assets/flow.svg" width="900" alt="Program Flow"/>

</div>

---

## `// 11` · OOP PRINCIPLES APPLIED

<div align="center">

<img src="assets/oop.svg" width="900" alt="OOP Principles"/>

</div>

---

## `// 12` · ASSUMPTIONS

- Dataset must be in **CSV format** with headers in the first row.
- When no dataset file is found, a **200-row synthetic dataset** is auto-generated at `data/sales_data.csv`.
- Mathematical and statistical operations apply to **numeric columns only**; non-numeric columns are skipped automatically.
- All visualizations default to `plt.show()` in CLI mode; in Jupyter, `%matplotlib inline` is active.
- Missing value handling is **non-destructive** by default — the user selects the strategy interactively.

---

<div align="center">

<img src="assets/footer.svg" width="900" alt="Footer"/>

</div>
