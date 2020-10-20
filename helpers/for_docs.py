import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

url_template = "http://climate.weather.gc.ca/climate_data/bulk_data_e.html?format=csv&stationID=5415&Year={year}&Month={month}&timeframe=1&submit=Download+Data"


def download_wether(year, month):
    url = url_template.format(year=year, month=month)
    weather_date = pd.read_csv(url, index_col="Date/Time", parse_dates=True, encoding="latin1")
    weather_date = weather_date.dropna(axis=1, how="any")
    weather_date.columns = [col.replace('\xb0', '') for col in weather_date.columns]
    weather_date = weather_date.drop(["Latitude (y)", "Station Name", "Climate ID", "Year", "Month"], axis=1)
    return weather_date
