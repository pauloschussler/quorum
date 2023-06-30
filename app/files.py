import csv
import pandas as pd

# Define a function to read csv files
def read_csv_file(file_path):
    data = pd.read_csv(file_path)
    return data

# Define a function to write csv files
def write_csv_file(file_path, data):
    with open(file_path, 'w', newline='') as csv_file:
        writer = csv.writer(csv_file)
        
        writer.writerow(data.columns)
       
        writer.writerows(data.values)
        
        print(f"Data successfully written to {file_path}")