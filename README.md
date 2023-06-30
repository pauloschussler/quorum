# Quorum

### This application reads and writes .csv files applying data filtering

The code is available in the following GitHub repository: https://github.com/pauloschussler/quorum.

#### Setting Up

To run this apllication, you will need Python installed on your system.

#### Project

This is a simple Python application that will generate two .csv files in the 'csv_results' folder.
To execute the code, you need to run the 'app.py' file. To do this, navigate to the folder where this project is located and execute the command 'python app.py'.
The command is illustrated in the following code snippet:

```
python folder/subfolder/quorum/app.py
```
#### OR

```
cd folder/subfolder/quorum/

python app.py
```


### Test answers

#### 1. Discuss your solution’s time complexity. What trade offs did you make?

The time complexity of the aplication is Linear Time: The execution time grows linearly with the input size.

Reading and Writing CSV Files:
Reading a CSV file: The time complexity for reading a CSV file using pandas read_csv() function is typically O(n), where n is the number of rows in the file. It reads each row and processes the data accordingly.
Writing a CSV file: The time complexity for writing a CSV file using pandas to_csv() function is also O(n), where n is the number of rows to be written. It iterates over the data and writes each row.

Data Filtering:
Time complexity for filtering operations can vary depending on the specific conditions and the size of the data being filtered.
Common filtering operations such as selecting rows based on a condition or applying logical operations on columns generally have a time complexity of O(n), where n is the number of rows being processed.

Trade-offs Made:

The trade-off made in this solution is that it prioritizes simplicity and ease of use by utilizing the pandas library for reading, writing, and filtering CSV files.

The focus was on providing a simple and readable solution rather than aiming for the most optimized performance.

#### 2. How would you change your solution to account for future columns that might be requested, such as “Bill Voted On Date” or “Co-Sponsors”?

The current code does not prevent the entry of different data, so it would be necessary to modify the functions responsible for filtering the data to handle such scenarios.

#### 3. How would you change your solution if instead of receiving CSVs of data, you were given a list of legislators or bills that you should generate a CSV for?

- Replace the step of reading CSV files with obtaining the list of legislators or bills directly as input.

- Perform any necessary data manipulations, filtering, or calculations on the list of legislators or bills as required.

- Write the data to a CSV file.

#### 4. How long did you spend working on the assignment?
3 hours.
