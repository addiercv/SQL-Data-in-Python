# This section of code is inspired from Exploratory Data Analysis Lab offered by IBM Machine Learning Foundation.
# Import required libraries
import sqlite3 as sq3   # SQL database library
import pandas.io.sql as pdsql   # Pandas

# SQL database is read by sqlite3 python package
db_path = 'data/classic_rock.db'
# Create a SQL database connection
sql_connection = sq3.Connection(db_path)
# Read the data in Pandas dataframe by writing a SQL query
query = '''SELECT * FROM rock_songs'''  # This query will select entire dataset
# Execute the query to read data (selected data based on query) into dataframe
data = pdsql.read_sql(query, sql_connection)
# Display head of data
print(data.head())

# Read another set of data from the same database based on new query
query2 = '''SELECT Artist, Release_Year, COUNT(*) AS num_songs, AVG(PlayCount) as avg_plays 
            FROM rock_songs
            GROUP BY Artist, Release_Year 
            ORDER BY num_songs desc'''
# Execute the query to read data
data2 = pdsql.read_sql(query2, sql_connection)
# Display head of selected data
print(data2.head())
