import pandas as pd

df = pd.read_csv("Salt_Lake_City_AQI/combined.csv")

df_proper_POC = df[df["POC"] == 1]


df_correct_columns = df[["Parameter Code", "POC", "Year"]]

print(df_correct_columns.head())