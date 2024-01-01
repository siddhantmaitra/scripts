from openpyxl import load_workbook
import pandas as pd
import sqlite3

 
# Parsing expenses spreadsheet with python

# Get list of months tracked

# load the workbook
wb = load_workbook(filename ='fin.xlsx',data_only=True)

#initialize sheet
month_sheets = list()

# filter and create list of months with 2023 in it
for sheet in wb:
	if "2023" in sheet.title:
		month_sheets.append(sheet.title)
		

# choose xlsx, take list of sheets, choose columns to be used, create dataframe dict from excel
dfs = pd.read_excel(io="fin.xlsx",sheet_name=month_sheets,usecols="B:I")

# concat all dataframes, ignore index of each one, drop any NaT/NaN in Date column
final_df = pd.concat(dfs, ignore_index=True).dropna(subset=['Date'])

# Write dataframe to csv, remove index
final_df.to_csv('Txns_2023_Apr-Dec.csv', index=False)

# Write dataframe to sqlite
conn = sqlite3.connect('Txns_2023_Apr-Dec.sqlite')
final_df.to_sql('Transactions', conn, if_exists='replace', index=False)
conn.close()