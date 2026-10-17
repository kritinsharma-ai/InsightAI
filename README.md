# InsightAI — End-to-End Data Science & AI Project

**InsightAI** is a hands-on business intelligence project that transforms raw business data into actionable insights through data cleaning, validation, analysis, visualization, and automated reporting.

The project uses a fictional e-commerce business, **NovaMart**, to demonstrate how Python-based data workflows can support better business decisions.

## 🎯 Project Goals

* Build a reusable data analysis pipeline.
* Clean and validate business datasets.
* Perform exploratory data analysis (EDA).
* Analyze product and category performance.
* Generate meaningful visualizations and business insights.
* Automate report generation.
* Expand the platform with SQL, machine learning, Generative AI, RAG, and AI agents.

## ✅ Implemented Features

* Data quality validation.
* Product revenue analysis.
* Category revenue analysis.
* Automated product and category visualizations.
* CSV report generation.
* Business insights and recommendations.
* Consolidated executive report generation.
* Pipeline logging and execution monitoring.

## 🛠️ Technologies

### Currently used

* Python
* Pandas
* NumPy
* Matplotlib
* Git and GitHub

### Planned extensions

* SQL
* Seaborn
* Machine Learning
* Large Language Model (LLM) APIs
* Retrieval-Augmented Generation (RAG)
* LangChain
* CrewAI
* AutoGen
* Workflow automation
* Interactive dashboards

*Planned technologies will be marked as implemented when their features are built and tested.*

## 🏗️ Project Workflow

```text
Cleaned Business Dataset
          |
          v
   Data Validation
          |
          v
 Product & Category Analysis
          |
          v
    Visualizations
          |
          v
     CSV Reports
          |
          v
  Business Insights
          |
          v
 Executive Business Report
```

## 📊 Example Business Scenario

InsightAI analyzes NovaMart's sample product dataset to identify revenue performance and category-level trends.

Example findings from the current dataset:

* **Total revenue:** ₹305,500
* **Total units sold:** 16
* **Top-revenue product:** Laptop
* **Top-revenue category:** Electronics

These figures describe the current sample dataset, not real-world sales.

## 📁 Project Structure

```text
InsightAI/
├── 01_python/
│   ├── main.py
│   ├── data_quality.py
│   ├── business_analysis.py
│   ├── reporting.py
│   ├── pipeline_logging.py
│   ├── Visualization.py
│   └── executive_report.py
├── 02_Data/
├── 03_Visualizations/
├── logs/
├── 02_sql/
├── 03_numpy/
├── 04_pandas/
├── 05_eda/
├── 06_visualization/
├── 07_machine_learning/
├── 08_genai/
├── 09_langchain/
├── 10_ai_agents/
├── 11_automation/
├── notebooks/
└── README.md
```

## 🚀 Getting Started

### Prerequisites

* Python installed
* Git installed
* Visual Studio Code (recommended)

### 1. Clone the repository

```bash
git clone https://github.com/kritinsharma-ai/InsightAI.git
cd InsightAI
```

### 2. Create and activate a virtual environment

**Windows PowerShell:**

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
```

If your virtual environment is named `.venv` at the project root, activate it using the command above.

### 3. Install dependencies

Install the packages used by the current project:

```powershell
python -m pip install pandas numpy matplotlib
```

### 4. Run the pipeline

From the repository root:

```powershell
python 01_python\main.py
```

The pipeline reads the cleaned dataset and generates analysis outputs, visualizations, and business reports.

## 📄 Outputs

Depending on the pipeline configuration, generated files include:

* `novamart_product_analysis.csv`
* `novamart_category_analysis.csv`
* `novamart_business_insights.txt`
* `novamart_executive_report.txt`
* `product_revenue.png`
* `category_revenue.png`
* `insightai.log`

Data reports are saved in `02_Data/`, charts in `03_Visualizations/`, and logs in `logs/`.

## 🗺️ Roadmap

* [x] Data quality checks
* [x] Product and category analysis
* [x] Revenue visualizations
* [x] Automated CSV and text reports
* [x] Executive business report
* [x] Pipeline logging
* [ ] SQL-based analysis
* [ ] Expanded exploratory data analysis
* [ ] Statistical analysis
* [ ] Machine learning models
* [ ] LLM-powered business analysis
* [ ] RAG-based knowledge retrieval
* [ ] AI agents and workflow automation
* [ ] Interactive business dashboard

## 📌 Project Status

**Status:** Core Python analysis and reporting pipeline implemented; additional data science and AI capabilities planned.

InsightAI is a learning and portfolio project focused on practical data science, business analytics, software organization, and progressive AI integration.

## 👨‍💻 Author

**Kritin Sharma**

GitHub: [kritinsharma-ai](https://github.com/kritinsharma-ai)

