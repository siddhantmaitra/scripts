import pandas as pd

# Load the data
data_uco = pd.read_excel('data.xlsx', sheet_name='UCO')
data_baroda = pd.read_excel('data.xlsx', sheet_name='Baroda')

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

# Write the results to a new sheet in the same Excel file
with pd.ExcelWriter('data.xlsx', mode='a') as writer:
    results.to_excel(writer, sheet_name='Results', index=False)
