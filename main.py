import pandas as pd  # Ensure this line is included at the top
import sqlite3

# Load the dataset
df = pd.read_csv('C:/Users/kschluss/Desktop/covid_data_analysis/Conditions_Contributing_to_COVID-19_Deaths__by_State_and_Age__Provisional_2020-2023.csv')

# Display the first few rows of the dataset
print(df.head())
# Create a connection to SQLite database
conn = sqlite3.connect('covid_data.db')  # This will create a new SQLite database file named 'covid_data.db'

# Load DataFrame into SQLite as a table
df.to_sql('covid_deaths', conn, if_exists='replace', index=False)  # This creates a table called 'covid_deaths'

# Verify the table was created by selecting the first few rows
query = pd.read_sql('SELECT * FROM covid_deaths LIMIT 5;', conn)
print("First 5 rows from the database:")
print(query)

# Query 1: Records where Age Group is '45-54 years'
query1 = pd.read_sql('SELECT * FROM covid_deaths WHERE "Age Group" = "45-54 years";', conn)
print("Query 1 Results (45-54 years):")
print(query1)

# Query 2: Count the number of records for New York
query2 = pd.read_sql('SELECT COUNT(*) AS death_count FROM covid_deaths WHERE State = "New York";', conn)
print("Query 2 Results (Count of deaths in New York):")
print(query2)

# Query 3: Group by Age Group and show total COVID-19 deaths
query3 = pd.read_sql('SELECT "Age Group", SUM("COVID-19 Deaths") AS total_deaths FROM covid_deaths GROUP BY "Age Group";', conn)
print("Query 3 Results (Total COVID-19 deaths by age group):")
print(query3)

# Query 4: Get the top 5 records with the most deaths
query4 = pd.read_sql('SELECT * FROM covid_deaths ORDER BY "COVID-19 Deaths" DESC LIMIT 5;', conn)
print("Query 4 Results (Top 5 records by COVID-19 deaths):")
print(query4)


