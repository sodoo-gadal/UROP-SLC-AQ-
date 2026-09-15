
# https://aqs.epa.gov/data/api/sampleData/bySite?email=test@aqs.api&key=test&param=44201&bdate=20170618&state=37&county=183&site=0014

import os
from dotenv import load_dotenv

load_dotenv()

#site number for hawthorne elementary school is 3006
#POC is 1
#begin date is 19980101 YYYYMMDD
#end date is 20260731 YYYYMMDD


def make_sample_data_key():
    state_code = 49 #utah's code
    county_code = "035" #salt lake county's code, having trouble including it as 035
    site_number = input("Please input the site number (4 digits) for the site you want to get data for: ")
    begin_date = input("Please input the beginning date (YYYYMMDD) for the data you want to get: ")
    end_date = input("Please input the ending date (YYYYMMDD) for the data you want to get: ")
    parameter_code = input("Please input the parameter code for the data you want to get: ")
    email = os.getenv("EMAIL")
    api_key = os.getenv("KEY")
    data_key = f"https://aqs.epa.gov/data/api/sampleData/bySite?email={email}&key={api_key}&param={parameter_code}&bdate={begin_date}&edate={end_date}&state={state_code}&county={county_code}&site={site_number}"
    return print(data_key)

make_sample_data_key()

