# job-market-analyzer
A Python-based job market intelligence tool that analyzes job listings to identify in-demand technical skills, popular job titles, and hiring trends.

# 📊 Job Market Analyzer

A Python-based job market intelligence tool that analyzes job listings to identify **in-demand technical skills, popular job titles, and hiring trends**.

## 🚀 Overview

The Job Market Analyzer collects job listing data from configurable public JSON sources and transforms it into useful insights about the technology job market.

The project automatically:

* Collects job listing data
* Cleans and normalizes job information
* Extracts technical skills from job titles and descriptions
* Identifies the most in-demand skills
* Analyzes popular job titles
* Analyzes job locations
* Generates CSV reports
* Creates visualizations automatically

## 🏗️ How It Works

```text
Job Data Source
       ↓
Data Collection
       ↓
Data Cleaning & Normalization
       ↓
Technical Skill Extraction
       ↓
Job Market Analysis
       ↓
CSV Reports + Charts
```

## ✨ Features

* 🔎 Configurable public JSON job data source
* 🧹 Automatic data cleaning and normalization
* 🧠 Technical skill extraction
* 📊 In-demand skill analysis
* 💼 Job title analysis
* 📍 Location analysis
* 📈 Automatic chart generation
* 💾 CSV report exports
* ⚙️ Command-line interface
* 🧪 Built-in sample data for testing

## 🛠️ Technologies

* Python
* Requests
* Pandas
* Matplotlib

## 📁 Project Structure

```text
job-market-analyzer/
│
├── main.py
├── config.py
├── requirements.txt
├── README.md
├── .gitignore
│
├── collectors/
│   └── jobs_api.py
│
├── analysis/
│   ├── skills.py
│   └── statistics.py
│
├── data/
│   └── .gitkeep
│
└── results/
    └── .gitkeep
```

## ⚙️ Installation

Clone the repository:

```bash
git clone https://github.com/YOUR-USERNAME/job-market-analyzer.git
cd job-market-analyzer
```

Install the required dependencies:

```bash
pip install -r requirements.txt
```

## ▶️ Usage

### Run with sample data

The project includes sample job listings for testing:

```bash
python main.py --sample-data
```

### Run with a public JSON job source

Provide a compatible public JSON endpoint:

```bash
python main.py --source-url "https://example.com/jobs.json"
```

The JSON response should contain either:

* A list of job objects

or an object containing one of the following:

* `jobs`
* `data`
* `results`
* `items`

## 📊 Analysis

The analyzer searches job titles and descriptions for technical skills such as:

* Python
* Java
* JavaScript
* TypeScript
* SQL
* Docker
* Kubernetes
* AWS
* Azure
* Linux
* Git
* Networking
* Cybersecurity
* Machine Learning
* PowerShell
* Windows Server

## 📈 Output

After running the analysis, the project generates:

### Data

```text
data/raw_jobs.json
data/cleaned_jobs.csv
```

### Reports

```text
results/skill_demand.csv
results/top_locations.csv
results/top_job_titles.csv
```

### Visualizations

```text
results/top_skills.png
results/top_locations.png
results/top_job_titles.png
```

## 💡 Example Results

The analyzer can produce insights such as:

```text
Top Technical Skills

1. Python
2. SQL
3. Docker
4. AWS
5. Linux
```

These results can help identify which technologies and skills appear most frequently across analyzed job listings.

## 🧠 Technical Approach

The project is divided into separate components:

### Data Collection

The `collectors` module retrieves job data from configurable public JSON sources.

### Skill Extraction

The analyzer searches job titles and descriptions for predefined technical skills using keyword matching.

### Data Analysis

Pandas is used to clean, normalize, and analyze job market data.

### Visualization

Matplotlib automatically generates charts showing:

* Most requested technical skills
* Most common job locations
* Most common job titles

## 🔮 Future Improvements

* [ ] Add additional job data source adapters
* [ ] Add salary analysis
* [ ] Analyze remote and hybrid positions
* [ ] Add skill trend analysis over time
* [ ] Create an interactive Streamlit dashboard
* [ ] Add automated tests
* [ ] Add scheduled data collection
* [ ] Add database storage
* [ ] Add GitHub Actions CI/CD

## ⚠️ Responsible Data Collection

This project is designed to work with public APIs and job-data sources that permit automated access.

When adding data sources, always respect:

* Terms of Service
* API documentation
* Rate limits
* Access restrictions

## 👤 Author

Developed as a portfolio project exploring **Python, data analysis, automation, and job market intelligence**.
