from folium import plugins
from folium.plugins import HeatMap
import folium
import pandas as pd
import matplotlib as plt


def non_empty_animal_reports(filepath):
    df = pd.read_csv(filepath, dtype=object)
    # Assuming df is your DataFrame
    # Strip whitespace from the "Animal" column and drop rows with empty strings
    df['Animal'] = df['Animal'].str.strip()  # Remove leading and trailing whitespace
    df = df[df['Animal'] != '']  # Drop rows where the Animal column is an empty string
    df.to_csv(f'animal_only.csv', index=False)
    print(df)


def create_animal_frequency_to_hourly_csv(filepath):
    df = pd.read_csv(filepath, dtype=object)
    pass


# create_heat_map('dog_lat_long.csv' , 'dog_heatmap.html')