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

non_empty_animal_reports("data/reports_with_date_and_animal.csv")

def create_animal_frequency_to_hourly_csv(filepath):
    df = pd.read_csv(filepath, dtype=object)
    time_and_animal_df = df[['a', 'e']]
    time_and_animal_df.to_csv(f'time_and_animal_df.csv', index=False)


#create_animal_frequency_to_hourly_csv("data/animal_only.csv")