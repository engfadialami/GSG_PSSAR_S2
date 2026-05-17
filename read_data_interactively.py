# %%
import pandas as pd
import json

# %%
#==============================================================
# read csv file

df_csv = pd.read_csv('raw_data\student_coffee_crisis.csv')

#==========================================================
# read json file

# flat JSON → DataFrame
df_json1 = pd.read_json('raw_data\student_coffee_crisis.json')
# nested JSON → use json + normalize
data_json = json.load(open('raw_data\student_coffee_crisis.json'))
df_json_norm = pd.json_normalize(data_json)

#==========================================================
# read excel file

df_excel = pd.read_excel('raw_data\student_coffee_crisis.xlsx')

#==========================================================
# read parquet file

df_parquet = pd.read_parquet('raw_data\student_coffee_crisis.parquet')



