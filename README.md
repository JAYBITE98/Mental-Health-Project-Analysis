# Mental Health in Tech: Data Analysis & Dashboard Project

## Project Overview
This project analyzes a survey dataset on mental health in the technology workplace. The goal is to uncover patterns in treatment-seeking behavior, identify key demographic factors, and present these insights in an interactive Power BI dashboard.

The workflow covers the entire data analysis lifecycle, from data cleaning and exploratory analysis (EDA) to building visualizations and a publishable dashboard.

## Key Features & Insights
*   **Data Cleaning**: Handled missing values, corrected typos (e.g., "Y" to "Yes"), and standardized columns for analysis.
*   **Exploratory Analysis**: Investigated relationships between treatment seeking and factors like gender and work interference.
*   **Key Finding**: Individuals who reported work "sometimes" interfering with their mental health were the most likely to seek treatment (45.5%), while those who reported it "often" interfered were the least likely (30.2%).
*   **Interactive Dashboard**: Built a dynamic Power BI dashboard with slicers for gender and work interference to allow for real-time data filtering.

## Tools & Technologies
*   **Python**: Primary language for data processing and analysis.
*   **Pandas**: Used for data manipulation, cleaning, and transformation.
*   **Matplotlib**: Created static visualizations for exploratory analysis.
*   **Power BI**: Designed and published the final interactive dashboard.

## Repository Contents
*   `generate_data.py`: Script to generate the sample survey dataset.
*   `analysis.py`, `cleaned_analysis.py`, `gender_analysis.py`, `work_analysis.py`: Python scripts for step-by-step analysis.
*   `mental_health_survey.csv`: Raw, unprocessed survey data.
*   `cleaned_mental_health_data.csv`: Data after cleaning and preprocessing.
*   `Mental_Health_Dashboard.pbix`: The final Power BI dashboard file.
*   `*.png`: Image exports of the key visualizations.

## How to Use This Project
1.  **Clone the repository**:
    ```bash
    git clone https://github.com/JAYBITE98/Mental-Health-Project-Analysis.git
