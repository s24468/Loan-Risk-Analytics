# Credit Risk & Loan Default Analytics (End-to-End Data Pipeline)

An automated, production-ready End-to-End Data Pipeline built for a Junior Data Engineer application. It extracts loan default data, loads it into a containerized PostgreSQL database, runs analytical transformations via SQL, and feeds a Power BI dashboard.

## 🚀 Architecture & Tech Stack
* **Orchestration:** Python (`run_pipeline.py`)
* **Extraction:** Kaggle API (`yasserh/loan-default-dataset`)
* **Database & Containerization:** PostgreSQL running inside a **Docker** container
* **Data Transformation:** Pandas, SQLAlchemy, and PostgreSQL Views (`create_views.sql`)
* **Visualization:** Power BI Desktop (Live connection to PostgreSQL)

## 📊 Pipeline Workflow
1. **Extract:** Automatically downloads and extracts the latest loan dataset from Kaggle.
2. **Load:** Ingests ~149k rows into a containerized PostgreSQL database (`raw_loans` table).
3. **Transform:** Executes modular SQL scripts to create clean analytical views (`vw_loan_summary`) with risk bucketing, DTI categories, and default flags.
4. **Export / BI:** Exposes clean relational data directly to Power BI for risk reporting.

## ⚙️ How to Run Locally
1. Clone the repository:
   ```bash
   git clone [https://github.com/YourUsername/Loan_Risk_Analytics.git](https://github.com/s24468/Loan_Risk_Analytics.git)