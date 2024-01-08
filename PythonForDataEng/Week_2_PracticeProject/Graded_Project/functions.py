import requests
from bs4 import BeautifulSoup
import pandas as pd
import sqlite3
import numpy as np
import datetime

# This function keeps a log of activities/tasks done
def log_progress(message):
    timestamp_format = '%Y-%h-%d-%H:%M:%S' # Year-Monthname-Day-Hour-Minute-Second 
    now = datetime.datetime.now() # get current timestamp 
    timestamp = now.strftime(timestamp_format)  
    with open("./code_log.txt","a") as f: 
        f.write(timestamp + ' : ' + message + '\n')
        
        
# This function will use requests to get html, then using beautiful soup we parse the html, from that we extract the data that we want:
def extract(url, table_attribs):
    r = requests.get(url).text
    soup = BeautifulSoup(r, 'html.parser')
    table = soup.find_all('tbody')
    table = table[0]
    rows = table.find_all('tr')
    count = 0
    
    df = pd.DataFrame(columns = table_attribs)
    data_dict = dict()

    for row in rows:
        if count < 11:
            col = row.find_all('td')
            if len(col) != 0:
                data_dict = {'Name':col[1].contents[2].contents[0], 'MC_USD_Billion':col[2].contents[0].replace('\n','')}
                df1 = pd.DataFrame(data_dict, index = [0])
                df = pd.concat([df, df1])
        else:
            break

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
    
def load_to_db(df, sql_connection, table_name):
    df.to_sql(table_name, sql_connection, if_exists='replace')
    
# Function to query the table
def run_query(query_statement, database):
    conn = sqlite3.connect(database)
    cursor = conn.cursor()
    cursor.execute(query_statement)
    rows = cursor.fetchall()
    conn.close()
    return rows