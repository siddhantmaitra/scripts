import os
import pandas as pd

# Get the path of the data file from the environment
data_path = os.environ['DATA_PATH']

# Load all sheets from the ODS file into a dictionary of DataFrames
data = pd.read_excel(data_path, sheet_name=None, engine='odf')

# Extract the HDFC_MF, ICICI_PRUD_MF, and CoalIndia sheets
data_hdfc = data['HDFC_MF']
data_icici = data['ICICI_PRUD_MF']
# data_coalindia = data['CoalIndia']

# Convert the date columns to datetime format
data_hdfc['Date'] = pd.to_datetime(data_hdfc['Date'], format='ISO8601')
data_icici['Date'] = pd.to_datetime(data_icici['Date'], format='ISO8601')
# data_coalindia['Date'] = pd.to_datetime(data_coalindia['Date'], format='%d/%m/%Y')

# Define the date ranges
date_ranges = [
    ('Up to 15-Jun-2024', '01-Jan-1900', '15-Jun-2024'),
    ('From 16-Jun-2024 to 15-Sep-2024', '16-Jun-2024', '15-Sep-2024'),
    ('From 16-Sep-2024 to 15-Dec-2024', '16-Sep-2024', '15-Dec-2024'),
    ('From 16-Dec-2024 to 15-Mar-2025', '16-Dec-2024', '15-Mar-2025'),
    ('From 16-Mar-2025 to 31-Mar-2025', '16-Mar-2025', '31-Mar-2025')
]

# Create a new DataFrame to store the results
results = pd.DataFrame(columns=['Constraint', 'HDFC_MF', 'ICICI_PRUD_MF', 'Total'])

# Iterate over the date ranges and compute the sums
for constraint, start_date, end_date in date_ranges:
    mask_hdfc = (data_hdfc['Date'] >= start_date) & (data_hdfc['Date'] <= end_date)
    mask_icici = (data_icici['Date'] >= start_date) & (data_icici['Date'] <= end_date)
    # mask_coalindia = (data_coalindia['Date'] >= start_date) & (data_coalindia['Date'] <= end_date)
    sum_hdfc = data_hdfc.loc[mask_hdfc, 'Credit'].sum()
    sum_icici = data_icici.loc[mask_icici, 'Credit'].sum()
    # sum_coalindia = data_coalindia.loc[mask_coalindia, 'Credit'].sum()
    total = sum_hdfc + sum_icici 
    # total = sum_hdfc + sum_icici + sum_coalindia
    new_row = pd.DataFrame({'Constraint': [constraint], 'HDFC_MF': [sum_hdfc], 'ICICI_PRUD_MF': [sum_icici], 'Total': [total]})
    # new_row = pd.DataFrame({'Constraint': [constraint], 'HDFC_MF': [sum_hdfc], 'ICICI_PRUD_MF': [sum_icici], 'CoalIndia': [sum_coalindia], 'Total': [total]})
    results = pd.concat([results, new_row], ignore_index=True)

# Add the results DataFrame to the dictionary of DataFrames
data['Results'] = results

# Write all DataFrames back to the ODS file
with pd.ExcelWriter(data_path, engine='odf') as writer:
    for sheet_name, df in data.items():
        df.to_excel(writer, sheet_name=sheet_name, index=False)
