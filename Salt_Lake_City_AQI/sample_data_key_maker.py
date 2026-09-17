
# https://aqs.epa.gov/data/api/sampleData/bySite?email=test@aqs.api&key=test&param=44201&bdate=20170618&state=37&county=183&site=0014

import os
from dotenv import load_dotenv
import pandas as pd
import requests


load_dotenv()

#site number for hawthorne elementary school is 3006
#POC is 1
#begin date is 19980101 YYYYMMDD
#end date is 20260731 YYYYMMDD


def make_sample_data_key(site_number, parameter_code, begin_date, end_date):
    state_code = "49" #utah's code
    county_code = "035" #salt lake county's code, having trouble including it as 035
    email = os.getenv("EMAIL")
    api_key = os.getenv("KEY")
    site_number = str(site_number).zfill(4)   # this ensures 4-digit site string
    parameter_code = str(parameter_code)   # this ensures parameter code is a string
    url = "https://aqs.epa.gov/data/api/sampleData/bySite"
    params = {
        "email": email,
        "key": api_key,
        "param": parameter_code,
        "bdate": begin_date,
        "edate": end_date,
        "state": state_code,
        "county": county_code,
        "site": site_number
    }
    
    response = requests.get(url, params=params)
    return response

site_number = "3006"
parameter_code = "88101"

all_data = []

for i in range(29): # changed to 29 to include the last date range
    year = 1998 + i
    print(f"Fetching data for year: {year}")
    if year == 2026:
        response = make_sample_data_key(site_number, parameter_code, "20260101", "20260731")
    else:
        new_start_date = f"{year}0101"
        new_end_date = f"{year}1231"
        response = make_sample_data_key(site_number, parameter_code, new_start_date, new_end_date)

    if response.status_code == 200:
        json_resp = response.json()
        if json_resp.get("Data"):
            all_data.extend(json_resp["Data"])
        else:
            print(f"No data / error for {year}: {json_resp.get('Header')}")

df = pd.DataFrame(all_data)
print(df)
