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

def transform(df):
    # Data cleaning
    df['GDP_USD_billion'] = df['GDP_USD_billion'].replace('—',np.nan, regex=True)
    df['GDP_USD_billion'] = df['GDP_USD_billion'].replace(',','', regex=True).astype(float)
    df = df.sort_values(by='GDP_USD_billion', ascending=False)
    return df