import pandas as pd

# import csv file as dataframe

city_weather_df = pd.read_csv("assets/cities.csv")
    
# convert dataframe as html
city_weather_table = city_weather_df.to_html()
print(city_weather_table)