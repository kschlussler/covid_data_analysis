# COVID-19 Data Analysis

COVID-19 death data using Pandas and SQLite to perform data analysis on a publicly available dataset.

## Steps Followed

1. **Loaded the dataset**:
   - I downloaded the dataset and used Pandas to read the CSV file into a DataFrame.
 

2. **Set up an SQLite database**:
   - After loading the dataset, I connected to an SQLite database using `sqlite3`.
   - I used Pandas’ `to_sql()` function to store the dataset into the SQLite database as a table called `covid_deaths`.

3. **Performed SQL queries**:
   - I wrote several SQL queries to analyze the data:
     - Query 1: Selected records for a specific age group.
     - Query 2: Counted the number of records for New York.
     - Query 3: Grouped data by age group and calculated total deaths.
     - Query 4: Retrieved the top 5 records with the most deaths.

## Errors and Troubleshooting

- **Error**: `NameError: name 'pd' is not defined` occurred when I forgot to import Pandas at the top of the script.
  - **Solution**: I added `import pandas as pd` at the beginning of the script, and the error was resolved.

- **Error**: SQL queries were not working because I was referencing the wrong column names.
  - **Solution**: I used the correct column name `"COVID-19 Deaths"` instead of `"Deaths"` in the SQL queries.

## Dataset

The dataset used is from the following link: [Conditions Contributing to COVID-19 Deaths](https://catalog.data.gov/dataset/conditions-contributing-to-deaths-involving-coronavirus-disease-2019-covid-19-by-age-group).

## SQL Queries Summary

- Query 1: Selected records where Age Group is '45-54 years'.
- Query 2: Counted the number of records for New York.
- Query 3: Grouped by Age Group and calculated total deaths.
- Query 4: Retrieved the top 5 records with the most deaths.

