import requests
from bs4 import BeautifulSoup
import pandas as pd
import sqlite3
import numpy as np
import datetime

# Functions & preliminaries for project:
url = 'https://web.archive.org/web/20230908091635 /https://en.wikipedia.org/wiki/List_of_largest_banks'
table_attribs = ['Name','MC_USD_Billion']
exchange_rate_df = pd.read_csv(r'C:\Users\Manuel Elizaldi\Desktop\Learning-Testing\DataEngCourse\Week_2_PracticeProject\Graded_Project\exchange_rate.csv')
output_path = r'C:\Users\Manuel Elizaldi\Desktop\Learning-Testing\DataEngCourse\Week_2_PracticeProject\Graded_Project\Largest_banks_data.csv'

# This function keeps a log of activities/tasks done
def log_progress(message):
    timestamp_format = '%Y-%h-%d-%H:%M:%S' # Year-Monthname-Day-Hour-Minute-Second 
    now = datetime.datetime.now() # get current timestamp 
    timestamp = now.strftime(timestamp_format)  
    with open(r"C:\Users\Manuel Elizaldi\Desktop\Learning-Testing\DataEngCourse\Week_2_PracticeProject\Graded_Project\code_log.txt","a") as f: 
        f.write(timestamp + ' : ' + message + '\n')
        
# This function will use requests to get html, then using beautiful soup we parse the html, from that we extract the data that we want:
def extract(url, table_attribs):
    # Getting and parsing html for extraction
    r = requests.get(url).text
    soup = BeautifulSoup(r, 'html.parser')
    table = soup.find_all('tbody')
    table = table[0]
    rows = table.find_all('tr')
    count = 0
    
    # Creating dict and data frame that will hold data
    df = pd.DataFrame(columns = table_attribs)
    data_dict = dict()

    # For loop to parse table rows
    for row in rows:
        if count < 11:
            col = row.find_all('td')
            if len(col) != 0:
                data_dict = {'Name':col[1].contents[2].contents[0], 'MC_USD_Billion':col[2].contents[0].replace('\n','')}
                df1 = pd.DataFrame(data_dict, index = [0])
                df = pd.concat([df, df1])
        else:
            break
    
    # Converting market cap column to float so we can perform operations on it
    df['MC_USD_Billion'] = df['MC_USD_Billion'].astype(float)
    
    return df

# This function has 2 arguments, one is the dataframe and the other one is the exchange rate table, we use the exchange rate table to create the new column in the dataframe
def transform(df, exchange_rate_df):
    # USD -> GBP conversion 
    df['MC_GBP_Billion'] = round(exchange_rate_df['Rate'][1] * df['MC_USD_Billion'],2)

    # USD -> EUR conversion
    df['MC_EUR_Billion'] = round(exchange_rate_df['Rate'][0] * df['MC_USD_Billion'],2)

    # USD -> INR conversion
    df['MC_INR_Billion'] = round(exchange_rate_df['Rate'][2] * df['MC_USD_Billion'],2)
    
    return df

# Saving dataframe as csv
def load_to_csv(df, output_path):
    df.to_csv(output_path)

# Uploading to database
def load_to_db(df, database, table_name):
    conn = sqlite3.connect(database)
    df.to_sql(table_name, conn, index = False, if_exists='replace')
    conn.close()
    
# Function to query the table
def run_query(query_statement, database):
    conn = sqlite3.connect(database)
    cursor = conn.cursor()
    cursor.execute(query_statement)
    rows = cursor.fetchall()
    conn.close()
    return rows

# Project:
log_progress('Preliminaries complete. Initiating ETL process')
print('Preliminaries complete. Initiating ETL process')

# Extraction of data from url
df = extract(url, table_attribs)
log_progress('Data extraction complete. Initiating Transformation process')
print('Data extraction complete. Initiating Transformation process')
print(df)

# Transformation process
df = transform(df,exchange_rate_df)
log_progress('Data transformation complete. Initiating Loading process')
print('Data transformation complete. Initiating Loading process')
print(df)

# Loading process
load_to_csv(df,output_path)
log_progress('Data saved to CSV file')
print('Data saved to CSV file')

# SQL Connection
log_progress('SQL Connection initiated')
print('SQL Connection initiated')

# SQL Creds
sql_connection = 'Banks.db'
table_name = 'Largest_banks'

#Loading to sql database 
load_to_db(df,sql_connection,table_name)
log_progress('Data loaded to Database as a table, Executing queries')
print('Data loaded to Database as a table, Executing queries')

#Queries
# Extract of whole database
query_statement = 'SELECT * FROM Largest_banks'
print('Printing the contents of the entire table:')
print(run_query(query_statement, sql_connection))

# Average market capitalization of all the banks in Billion USD.
query_statement = 'SELECT AVG(MC_GBP_Billion) FROM Largest_banks'
print('Average market capitalization of all the banks in Billion USD')
print(run_query(query_statement, sql_connection))

# Print only the names of the top 5 banks
query_statement = 'SELECT Name from Largest_banks LIMIT 5'
print('Top 5 banks')
print(run_query(query_statement, sql_connection))

# Extract the information for the London office, that is Name and MC_GBP_Billion
query_statement = 'SELECT Name, MC_GBP_Billion FROM Largest_banks'
print('Information for the London Office:')
print(run_query(query_statement, sql_connection))

# Extract the information for the Berlin office, that is Name and MC_EUR_Billion
query_statement = 'SELECT Name, MC_EUR_Billion FROM Largest_banks'
print('Information for the Berlin Office:')
print(run_query(query_statement, sql_connection))

# Extract the information for New Delhi office, that is Name and MC_INR_Billion
query_statement = 'SELECT Name, MC_INR_Billion FROM Largest_banks'
print('Information for the Delhi Office:')
print(run_query(query_statement, sql_connection))

# End
log_progress('Process Complete')
print('Process Complete')

# Closing server connection
log_progress('Server Connection Closed')
print('Server Connection Closed')