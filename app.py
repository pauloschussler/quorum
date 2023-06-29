import csv
import pandas as pd

def read_csv_file(file_path):
    data = pd.read_csv(file_path)
    return data

def print_csv_data(data):
    df = pd.DataFrame(data)
    print(df.to_string(index=False, header=False))

def legislators_support_oppose(legislators, vote_result):

    merged_data = legislators.merge(vote_result, left_on='id', right_on='legislator_id')
    grouped_data = merged_data.groupby(['legislator_id', 'name', 'vote_type']).size().reset_index(name='vote_count')
    grouped_data.rename(columns={'legislator_id': 'id'}, inplace=True)

    supported_bills = grouped_data[grouped_data['vote_type'] == 1].rename(columns={'vote_count': 'num_supported_bills'}).drop(columns=['vote_type'])
    opposed_bills = grouped_data[grouped_data['vote_type'] == 2].rename(columns={'vote_count': 'num_opposed_bills'}).drop(columns=['vote_type'])

    legislators_result = supported_bills.merge(opposed_bills, on=['id', 'name'])

    return legislators_result

# Define the CSV file paths
csv_file_paths = [
    'bills.csv',
    'legislators.csv',
    'vote_results.csv',
    'votes.csv'
]

# Read the CSV files and store the contents in variables
bills = read_csv_file(csv_file_paths[0])
legislators = read_csv_file(csv_file_paths[1])
vote_result = read_csv_file(csv_file_paths[2])
votes = read_csv_file(csv_file_paths[3])

legislators_support_oppose_count = legislators_support_oppose(legislators, vote_result)