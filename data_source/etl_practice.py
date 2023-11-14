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

def extract_xml(filename):
    df = pd.DataFrame(columns=['car_model','year_of_manufacture', 'price','fuel'])
    tree = ET.parse(filename)
    root = tree.getroot()
    for car in root:
        car_model = car.find('car_model').text
        year_of_manufacture = car.find('year_of_manufacture').text
        price = float(car.find('price').text)
        fuel = float(car.find('fuel').text)
    
    df = pd.concat([df, pd.DataFrame([{'car_model':car_model, 'year_of_manufacture':year_of_manufacture, 'price':price, 'fuel':fuel}])])
    
    return df

def extract():
    extracted_data = pd.DataFrame(columns=['car_model', 'year_of_manufacture','price','fuel'])
    
    # process all csv files
    for csvfile in glob.glob('*csv'):
        extracted_data = pd.concat([extracted_data, pd.DataFrame(extract_csv(csvfile))], ignore_index = True)
    
    for jsonfile in glob.glob('*.json'):
        extracted_data = pd.concat([extracted_data, pd.DataFrame(extract_json(jsonfile))], ignore_index = True)
    
    for xmlfile in glob.glob('*.xml'):
        extracted_data = pd.concat([extracted_data, pd.DataFrame(extract_xml(xmlfile))], ignore_index = True)
    
    return extracted_data

def transform():
    df = df
    return df
