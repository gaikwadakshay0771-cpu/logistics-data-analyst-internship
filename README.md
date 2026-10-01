# Logistics Data Analyst Internship

Week 1 project for the **Logistics Data Analyst Intern** internship.

## Project
Strategic planning and data exploration for an e-commerce logistics scenario.

### Business focus
- Delivery reliability and late-delivery risk
- Shipping duration
- Operational segmentation
- Data quality
- Route-optimization planning

### Analytical methods
- Exploratory Data Analysis (EDA)
- Regression
- Classification
- Clustering
- Vehicle Routing / Optimization

## Repository structure

```text
logistics-data-analyst-internship/
├── README.md
├── PROJECT_STATUS.md
├── requirements.txt
├── .gitignore
├── src/
│   └── logistics_analysis.py
├── notebooks/
│   └── week1_logistics_analysis.ipynb
├── data/
│   └── README.md
├── reports/
│   └── Week_1_Logistics_Strategic_Planning_Report.docx
└── docs/
    └── project_notes.md
```

## Dataset

Primary public dataset:

**DataCo SMART Supply Chain for Big Data Analysis**

Dataset page:
https://data.mendeley.com/datasets/8gx2fvg2k6/5

DOI:
https://doi.org/10.17632/8gx2fvg2k6.5

The raw dataset is intentionally not included in this repository. Download it from the source and place the main CSV at:

```text
data/DataCoSupplyChainDataset.csv
```

## Setup

```bash
python -m venv .venv
```

Windows:

```bash
.venv\Scripts\activate
```

Install:

```bash
pip install -r requirements.txt
```

Run:

```bash
python src/logistics_analysis.py
```

Open the notebook:

```bash
jupyter notebook
```

## Important

The code contains a baseline workflow and illustrative models. Verify the exact downloaded-dataset column names before execution.

The route-optimization section is a prototype. A real VRP needs operational inputs such as coordinates, travel time/distance, vehicle capacity and delivery time windows.

Do not upload private company data, credentials, API keys, tokens, customer personal information, `.env` files or other secrets.

## Deliverable

The main Week 1 report is in:

`reports/Week_1_Logistics_Strategic_Planning_Report.docx`

## Author

**Akshay**
