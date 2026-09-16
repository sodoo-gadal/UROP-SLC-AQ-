
# https://aqs.epa.gov/data/api/sampleData/bySite?email=test@aqs.api&key=test&param=44201&bdate=20170618&state=37&county=183&site=0014

import os
from dotenv import load_dotenv
import pandas as pd


load_dotenv()

#site number for hawthorne elementary school is 3006
#POC is 1
#begin date is 19980101 YYYYMMDD
#end date is 20260731 YYYYMMDD


def make_sample_data_key(begin_date, end_date):
    state_code = 49 #utah's code
    county_code = "035" #salt lake county's code, having trouble including it as 035
    email = os.getenv("EMAIL")
    api_key = os.getenv("KEY")
    data_key = f"https://aqs.epa.gov/data/api/sampleData/bySite?email={email}&key={api_key}&param={parameter_code}&bdate={begin_date}&edate={end_date}&state={state_code}&county={county_code}&site={site_number}"
    return data_key

site_number = input("Please input the site number (4 digits) for the site you want to get data for: ")
parameter_code = input("Please input the parameter code for the data you want to get: ")

key_list = []

for i in range(28):
    if i == 0:
        new_key = make_sample_data_key(19980101, 19981231)
    elif i == 28:
        new_key = make_sample_data_key(20260101, 20260731)
    else:
        new_start_date = 19980101 + (i * 10000)
        new_end_date = 19980101 + ((i + 1) * 10000) - 1
        new_key = make_sample_data_key(new_start_date, new_end_date)
    key_list.append(new_key)

df = pd.DataFrame(key_list, columns=["Data Key"])
print(df)
