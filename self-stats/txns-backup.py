from openpyxl import load_workbook
import pandas as pd
import sqlite3

# Parsing expenses spreadsheet with python

# Get list of months tracked
print("Txns to csv,sqlite converter.")
print("Ensure:\n 1. File is in .xlsx format. \n 2. File is present in /data folder and has no spaces in its name")
year = input("\nPlease enter the year: ")
file_name = input("Please enter the file name: ")

file = f'data/{file_name}.xlsx'
# load the workbook
wb = load_workbook(filename=file, data_only=True)

#initialize sheet
month_sheets = list()

# filter and create list of months with 2023 in it
for sheet in wb:
    if year in sheet.title:
        month_sheets.append(sheet.title)

# choose xlsx, take list of sheets, choose columns to be used, create dataframe dict from excel
dfs = pd.read_excel(io=file, sheet_name=month_sheets, usecols="B:I")

# concat all dataframes, ignore index of each one, drop any NaT/NaN in Date column
final_df = pd.concat(dfs, ignore_index=True).dropna(subset=['Date'])

def clean_amount(amount):
    if pd.isna(amount):
        return 0.0
    try:
        # Convert to string first to handle any numeric types
        amount_str = str(amount)
        # Remove ₹, spaces, and commas
        cleaned = amount_str.replace('₹', '').replace(',', '').replace(' ', '').strip()
        return float(cleaned) if cleaned else 0.0
    except Exception as e:
        print(f"[ERROR]: Could not convert value: {amount}")
        return 0.0

final_df['Amount'] = final_df['Amount'].apply(clean_amount)


final_df.to_csv(f'output/txns-{year}.csv', index=False)

# Write dataframe to sqlite
conn = sqlite3.connect(f'output/txns-{year}.sqlite')
final_df.to_sql('Transactions', conn, if_exists='replace', index=False)
conn.close()