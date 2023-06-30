import pandas as pd


from app.files import *
from app.data import *

# Define the CSV file paths
csv_file_paths = [
    'bills.csv',
    'legislators.csv',
    'vote_results.csv',
    'votes.csv'
]

# Read the CSV files and store the contents in variables
bills_csv = read_csv_file(csv_file_paths[0])
legislators_csv = read_csv_file(csv_file_paths[1])
vote_result_csv = read_csv_file(csv_file_paths[2])
votes_csv = read_csv_file(csv_file_paths[3])

legislators_support_oppose_count = legislators_support_oppose(legislators_csv, vote_result_csv)
bills_support_oppose_count = bills_support_oppose(bills_csv, legislators_csv, vote_result_csv, votes_csv)

write_csv_file('./csv_results/legislators-support-oppose-count.csv', legislators_support_oppose_count)
write_csv_file('./csv_results/bills.csv', bills_support_oppose_count)