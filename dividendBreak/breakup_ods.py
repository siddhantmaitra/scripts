import os
import pandas as pd

# Get the path of the data file from the environment
data_path = os.environ['DATA_PATH']

# Load all sheets from the ODS file into a dictionary of DataFrames
data = pd.read_excel(data_path, sheet_name=None, engine='odf')

# Extract the UCO and Baroda sheets
data_uco = data['UCO']
data_baroda = data['Baroda']

# Convert the date columns to datetime format
data_uco['Dates'] = pd.to_datetime(data_uco['Dates'], format='%d-%b-%Y')
data_baroda['Dates'] = pd.to_datetime(data_baroda['Dates'], format="%d/%m/%Y")

# Define the date ranges
date_ranges = [
    ('Up to 15-Jun-2022', '01-Jan-1900', '15-Jun-2022'),
    ('From 16-Jun-2022 to 15-Sep-2022', '16-Jun-2022', '15-Sep-2022'),
    ('From 16-Sep-2022 to 15-Dec-2022', '16-Sep-2022', '15-Dec-2022'),
    ('From 16-Dec-2022 to 15-Mar-2023', '16-Dec-2022', '15-Mar-2023'),
    ('From 16-Mar-2023 to 31-Mar-2023', '16-Mar-2023', '31-Mar-2023')
]

# Define the keywords for filtering the description column
keywords = ['hdfc balanced', 'icici prudential', 'aditya birla']

# Create a new DataFrame to store the results
results = pd.DataFrame(columns=['Constraint', 'UCO', 'Baroda', 'Total'])

# Iterate over the date ranges and compute the sums
for constraint, start_date, end_date in date_ranges:
    mask_uco = (data_uco['Dates'] >= start_date) & (data_uco['Dates'] <= end_date) & (data_uco['Description'].str.lower().str.contains('|'.join(keywords)))
    mask_baroda = (data_baroda['Dates'] >= start_date) & (data_baroda['Dates'] <= end_date) & (data_baroda['Description'].str.lower().str.contains('|'.join(keywords)))
    sum_uco = data_uco.loc[mask_uco, 'Deposit'].sum()
    sum_baroda = data_baroda.loc[mask_baroda, 'Deposit'].sum()
    total = sum_uco + sum_baroda
    new_row = pd.DataFrame({'Constraint': [constraint], 'UCO': [sum_uco], 'Baroda': [sum_baroda], 'Total': [total]})
    results = pd.concat([results, new_row], ignore_index=True)

# Add the results DataFrame to the dictionary of DataFrames
data['Results'] = results

# Write all DataFrames back to the ODS file
with pd.ExcelWriter(data_path, engine='odf') as writer:
    for sheet_name, df in data.items():
        df.to_excel(writer, sheet_name=sheet_name, index=False)
