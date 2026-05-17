import pandas as pd

#==============================================================
# read csv file

# df_csv = pd.read_csv('raw_data\student_coffee_crisis.csv')
# # common params:
# df_csv1 =pd.read_csv('raw_data\student_coffee_crisis.csv',
# sep=';', # different delimiter
# encoding='utf-8',
# skiprows=1)
#print("\nCSV:")
#print(df_csv.head())
#print(df_csv)

#==========================================================
# read json file

df_json = pd.read_json('raw_data\student_coffee_crisis.json')
print("\nJSON:")
print(df_json) 

# flat JSON → DataFrame
df_json1 = pd.read_json('raw_data\student_coffee_crisis.json')
# nested JSON → use json + normalize
import json
data_json = json.load(open('raw_data\student_coffee_crisis.json'))
df_json2 = pd.json_normalize(data_json)
print("\nJSON:")
print(df_json1)
print("\nJSON normalized:")
print(df_json2)

#==========================================================
# read excel file

# df_excel = pd.read_excel('raw_data\student_coffee_crisis.xlsx')
# print("\nExcel:")
# print(df_excel)
# #specific sheet:
# df_excel1 = pd.read_excel('raw_data\student_coffee_crisis.xlsx', sheet_name='Coffee_Crisis')
# print(df_excel1)

#==========================================================
# read parquet file
df_parquet = pd.read_parquet('raw_data\student_coffee_crisis.parquet')
# print("\nParquet:")
# print(df_parquet)


