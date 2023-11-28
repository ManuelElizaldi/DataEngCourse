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