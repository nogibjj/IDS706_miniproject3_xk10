[![CI/CD Workflow](https://github.com/cassiekang/IDS706-template/actions/workflows/cicd.yml/badge.svg)](https://github.com/cassiekang/IDS706-template/actions/workflows/cicd.yml)


# Polars Descriptive Statistics Script

## Purpose
This project aims to perform EDA on the 'bmi.csv' dataset from Kaggle (https://www.kaggle.com/datasets/rukenmissonnier/age-weight-height-bmi-analysis), which comprises 741 individual records. Here are the concise goals:

1. Dataset loading: create a codespaces environment to automatically load the 'bmi.csv' dataset using Polars.
2. Descriptive statistics: generate basic descriptive statistics, including mean, median, standard deviation for the columns (age, height, weight, bmi).
3. data visualization: create one example visualization for age distribution.

## Preparation
1. This project was generated from the previous miniproject IDS706-template, which includes a 'Makefile', 'requirements.txt', '.devcontainer', '.gitignore', 'GithubActions' and 'README'.
2. The project incorporates an automated workflow managed through a Makefile, which efficiently handles various tasks. These tasks encompass installation (via "make install"), testing (via "make test"), code formatting (via "make format"), and code quality checks (via "make lint").
3. main.py:
* Reads dataset from a CSV file using polars.
* Generates summary statistics and a histogram for the 'Age' column.
* Saves summary statistics and a histogram as Markdown and image files.
4. test_main.py:
* Tests the generate_summary_and_visualization function.
* Loads a test dataset using polars.
* Calls the function to create a test summary report and histogram.

## Summary Statistics
The dataset contains 741 records with the following key statistics: Age: Average age is 31.6 years, ranging from 15 to 61 years. Height: Average height is 1.709 meters, ranging from 1.46 to 2.07 meters. Weight: Average weight is 78.4 kilograms, ranging from 25.9 to 270 kilograms. BMI: Average BMI is 26.4, ranging from 12.15 to 66.30. These statistics summarize the dataset's age, height, weight, and BMI attributes.

## Data Visualization
For this project, I created a histogram for age distribution

## Summary report: please see 'summary_rerport.md'
I used data.describe() to compute the summary statistics for numeric columns using polars. Then, convert them to a pandas DataFrame for compatibility with the 'to_markdown()' function, and save the summary statistics in Markdown format using 'summary_stats.to_pandas.to_markdown()'.

