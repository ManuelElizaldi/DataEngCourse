# Lesson: Hands-on Lab: Extract, Transform, Load (ETL)
# Headers: 'car_model', 'year_of_manufacture', 'price', 'fuel'
# File types: CSV, Json, XML
import glob 
import pandas as pd 
# This package helps us extract XML data
import xml.etree.ElementTree as ET 
from datetime import datetime 

# This file will store the log
log_file = "log_file.txt" 

# This file will store the data
target_file = "transformed_data.csv" 


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
        price = car.find('price').text
        fuel = car.find('fuel').text
        df = pd.concat([df, pd.DataFrame([{'car_model':car_model, 'year_of_manufacture':year_of_manufacture, 'price':price, 'fuel':fuel}])])
    
    # Convert 'price' column to numeric
    # Got this piece of code from chatgpt and now the script works:
    df['price'] = pd.to_numeric(df['price'], errors='coerce')
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

def transform(data):
    data['price'] = round(data.price ,2)
    return data

def load_data(target_file, clean_data):
    clean_data.to_csv(target_file)
    
def log_progress(message):
    timestamp_format = '%Y-%h-%d-%H:%M:%S'
    now = datetime.now()
    timestamp = now.strftime(timestamp_format)
    with open(log_file, 'a') as f:
        f.write(timestamp + ',' + message + '\n')

# Log the initialization of the ETL process 
log_progress("ETL Job Started") 
print("ETL Job Started")

# Log the beginning of the Extraction process 
log_progress("Extract phase Started") 
print("Extract phase Started")
extracted_data = extract() 

# Log the completion of the Extraction process 
log_progress("Extract phase Ended") 
print("Extract phase Ended")

# Log the beginning of the Transformation process 
log_progress("Transform phase Started") 
print("Transform phase Started")

# Testing
print(extracted_data['price'].dtype)

transformed_data = transform(extracted_data) 
print("Transformed Data") 
print(transformed_data) 
 
# Log the completion of the Transformation process 
log_progress("Transform phase Ended") 
print("Transform phase Ended")

# Log the beginning of the Loading process 
log_progress("Load phase Started") 
load_data(target_file,transformed_data) 
print("Load phase Started")

# Log the completion of the Loading process 
log_progress("Load phase Ended") 
print("Load phase Ended")

# Log the completion of the ETL process 
log_progress("ETL Job Ended") 
print("ETL Job Ended")