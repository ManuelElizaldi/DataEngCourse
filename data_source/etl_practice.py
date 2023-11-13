# Lesson: Hands-on Lab: Extract, Transform, Load (ETL)

# Headers: 'car_model', 'year_of_manufacture', 'price', 'fuel'
# File types: CSV, Json, XML
import glob 
import pandas as pd 
# This package helps us extract XML data
import xml.etree.ElementTree as ET 
from datetime import datetime 


def extract_csv(filename):
    df = pd.read_csv(filename, low_memory = False)
    return df

def extract_json(filename):
    df = pd.read_json(filename, lines = True)
    return df

df extract_xml(filename):
    df = pd.DataFrame(columns=['car_model','year_of_manufacture', 'price','fuel'])
    tree = ET.parse(filename)
    root = tree.getroot()
    for car in root:
        car_model = 
        year_of_manufacture = 
        price = 
        fuel = 