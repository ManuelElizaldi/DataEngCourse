import glob 
import pandas as pd 
import xml.etree.ElementTree as ET 
from datetime import datetime 

# This file will store the log
log_file = "log_file.txt" 

# This file will store the data
target_file = "transformed_data.csv" 


# This function will extract a csv 
def extract_from_csv(file_to_process): 
    dataframe = pd.read_csv(file_to_process, low_memory=False) 
    return dataframe 

# This function will extract a json file 
# lines = True so that each file is treated like its own json
def extract_from_json(file_to_process): 
    dataframe = pd.read_json(file_to_process, lines=True) 
    return dataframe 


# This function will extract a xml file 
def extract_from_xml(file_to_process):
    dataframe = pd.DataFrame(columns=['name','height','weight'])
    tree = ET.parse(file_to_process)
    root = tree.getroot()
    for person in root:
        name = person.find('name').text
        height = float(person.find('height').text)
        weight = float(person.find('weight').text)
        
        dataframe = pd.concat([dataframe, pd.DataFrame([{'name':name,'height':height,'weight':weight}])])
    
    return dataframe


# Putting them all together
# By using the wild card * you extract everything from the local folder
# This function would need changes if you want it to extract files from another folder
def extract():
    # This empty dataframe will hold the extracted data
    extracted_data = pd.DataFrame(columns=['name','height','weight'])
    
    # Process all csv files
    for csvfile in glob.glob('*csv'):
        extracted_data = pd.concat([extracted_data, pd.DataFrame(extract_from_csv(csvfile))], ignore_index = True)
        
    # Process all json files
    for jsonfile in glob.glob('*.json'):
        extracted_data = pd.concat([extracted_data, pd.DataFrame(extract_from_json(jsonfile))], ignore_index = True)
        
    for xmlfile in glob.glob('*.xml'):
        extracted_data = pd.concat([extracted_data, pd.DataFrame(extract_from_xml(xmlfile))], ignore_index= True)
        
    return extracted_data


# Function to transform from pounds -> kilograms and inch -> meters
def transform(data): 
    '''Convert inches to meters and round off to two decimals 
    1 inch is 0.0254 meters '''
    data['height'] = round(data.height * 0.0254,2) 
 
    '''Convert pounds to kilograms and round off to two decimals 
    1 pound is 0.45359237 kilograms '''
    data['weight'] = round(data.weight * 0.45359237,2) 
    
    return data 

# This function will load the extracted and cleaned data to a csv file that can be used in a database later 
def load_data(target_file, transformed_data):
    transformed_data.to_csv(target_file)

# It is good practice to also keep a log of changes that have happend, this function will take care of that
def log_progress(message):
    timestamp_format = '%Y-%h-%d-%H:%M:%S' # Year-Monthname-Day-Hour-Minute-Second 
    now = datetime.now()
    timestamp = now.strftime(timestamp_format)
    with open(log_file, 'a') as f:
        f.write(timestamp + ',' + message + '\n')