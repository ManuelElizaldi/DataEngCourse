import requests
import sqlite3
import pandas as pd
from bs4 import BeautifulSoup

# Information required Average Rank, Film, and Year
url = 'https://web.archive.org/web/20230902185655/https://en.everybodywiki.com/100_Most_Highly-Ranked_Films'

# I have to create this in my machine:
db_name = 'Movies.db'
table_name = 'Top_50'

# Path to csv that will hold the data
csv_path = r'C:\Users\Manuel Elizaldi\Desktop\Learning-Testing\DataEngCourseProject\Web_Scraping_Lesson'

# creating dataframe to hold requiered info
df = pd.DataFrame(columns=["Average Rank","Film","Year"])

# We set counter to 0 because we only need top 50, there might be mroe in the website
count = 0

# Getting the html from the website that we will parse
r = requests.get(url).text

# Creating the beautiful soup object
soup = BeautifulSoup(r, 'html.parser')

# Using the inspect feature in the browser we can analyze the html
# When doing that, we can notice that the table is inside the <tbody> tag
# Each row is inside the <tr> row and each element inside the row is in the <th> tag
# So we need a for loop inside another loop to get this data

# To get all the rows inside the table we need to use the method find_all 
tables = soup.find_all('tbody')
rows = tables[0].find_all('tr')

print(rows)