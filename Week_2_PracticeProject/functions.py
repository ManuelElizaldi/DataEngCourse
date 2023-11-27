import requests
from bs4 import BeautifulSoup
import pandas as pd
import sqlite3
import numpy as np
import datetime

# Data extraction function
def extract(url):
    r = requests.get(url).text
    # Using BeautifulSoup to parse html
    soup = BeautifulSoup(r, 'html.parser')
    table = soup.find_all('tbody')
    rows = table[2].find_all('tr')
    
    count = 0 
    df = pd.DataFrame(columns=['Country', 'GDP_USD_billion'])
    data_dict = dict()

    # For loop to parse the rows and get every value 
    for row in rows[3:]:
        if count < 214:
            col = row.find_all('td')
            data_dict = {'Country':col[0].contents[2],
                        'GDP_USD_billion':col[2].contents[0]}
            df1 = pd.DataFrame(data_dict, index = [0])
            df = pd.concat([df,df1])
            count+=1
        else:
            break
    return df

# Cleaning data function
def transform(df):
    # Data cleaning
    df['GDP_USD_billion'] = df['GDP_USD_billion'].replace('—',np.nan, regex=True)
    df['GDP_USD_billion'] = df['GDP_USD_billion'].replace(',','', regex=True).astype(float)
    df['GDP_USD_billion'] = round(df['GDP_USD_billion']/1000,2)
    df = df.sort_values(by='GDP_USD_billion', ascending=False)
    return df

# Saving as CSV
def load_to_csv(df, file_name, csv_path):
    file_name = 'Countries_by_GDP.csv'
    csv_path = fr'C:\Users\Manuel Elizaldi\Desktop\Learning-Testing\DataEngCourse\Week_2_PracticeProject\{file_name}'
    df.to_csv(csv_path, index = False)

# Saving data inside database
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
    return rows

# This function keeps a log of activities/tasks done
def log_progress(message):
    timestamp_format = '%Y-%h-%d-%H:%M:%S' # Year-Monthname-Day-Hour-Minute-Second 
    now = datetime.now() # get current timestamp 
    timestamp = now.strftime(timestamp_format) 
    with open("./etl_project_log.txt","a") as f: 
        f.write(timestamp + ' : ' + message + '\n')