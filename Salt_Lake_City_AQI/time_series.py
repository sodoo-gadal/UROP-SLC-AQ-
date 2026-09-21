import pandas as pd

import matplotlib.pyplot as plt

df = pd.read_csv("Salt_Lake_City_AQI/combined.csv")

df = df[['Parameter Code', 'POC', 'Parameter Name', 'Duration Description', 'Year', 'Units of Measure', 'Observation Count', 'Valid Day Count', 'Arithmetic Mean', ]]

#filter for local PM2.5 data only
df = df[df["Parameter Name"] == "PM2.5 - Local Conditions"]

#filter for PPM measurements only
df = df[df['Units of Measure'] == "Micrograms/cubic meter (LC)"]

#remove the header row that is being read in the data, most likely from hasty combining of the csv files through
#the command line interface
df = df[df["Year"] != "Year"]

#sort the dataframe by year in ascending order so that the time series plot will be correct
df = df.sort_values(["Year"], ascending=True)

#sorting so that my dataframe only includes what I need for the time series plot

df = df[['Year', 'Arithmetic Mean']]

#converting the Year and Arithmetic Mean columns to numeric values so that I can plot them
#why are they strings ;(

df['Year'] = pd.to_numeric(df['Year'], errors='coerce')
df['Arithmetic Mean'] = pd.to_numeric(df['Arithmetic Mean'], errors='coerce')

df = df[df['Arithmetic Mean'].apply(lambda x: isinstance(x, (int, float)))]

#print(df.head())

#print(df())

print(df.shape)

#i've got it printing a plot, but the plot looks super suspicious, I dont think the right units are coming out


plt.scatter(df["Year"], df["Arithmetic Mean"])
plt.title("Salt Lake City PM2.5 Time Series")
plt.xlabel("Year")
plt.ylabel("PM2.5 Concentration (µg/m³)")
plt.show()