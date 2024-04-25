from folium import plugins
from folium.plugins import HeatMap
import folium
import pandas as pd


# for creating a dataset with just the specified animal, 
def generate_datasets_for_animal_coordinates_time(filename):
    df = pd.read_csv(filename)
    df_cleaned = df[['Animal', 'latitude', 'longitude', 'open_dt']]

    df_cleaned['open_dt'] = pd.to_datetime(df_cleaned['open_dt'])
    print(df_cleaned.head())
    df_cleaned.to_csv('animal_coordinates_time_dataset.csv', index=False)


# filename = "data/animal_only.csv"
# generate_datasets_for_animal_coordinates_time(filename)


# generate a dataset for a given animal by year and the coordinates of their location 
def generate_coordinates_for_animal_report_by_year(filename, animal, year):
    df = pd.read_csv(filename)

    df['open_dt'] = pd.to_datetime(df['open_dt'])

    filtered_df = df[(df['Animal'] == animal) & (df['open_dt'].dt.year == year)]

    filtered_df.to_csv(f'Heatmaps/{animal}_reports_{year}.csv', index=False)


filename = "Heatmaps/animal_coordinates_time_dataset.csv"
year23 = 2023
year22 = 2022
year21 = 2021
year20 = 2020
year19 = 2019
# generate_coordinates_for_animal_report_by_year(filename, 'dog', year23)
# generate_coordinates_for_animal_report_by_year(filename, 'dog', year22)
# generate_coordinates_for_animal_report_by_year(filename, 'dog', year21)
# generate_coordinates_for_animal_report_by_year(filename, 'dog', year20)
# generate_coordinates_for_animal_report_by_year(filename, 'dog', year19)


def create_heat_map(filepath, output):
    map_hooray = folium.Map(location=[42.3601, -71.0589], zoom_start=13) 

    df_acc = pd.read_csv(filepath, dtype=object)
    df_acc['latitude'] = df_acc['latitude'].astype(float)
    df_acc['longitude'] = df_acc['longitude'].astype(float)

    heat_df = df_acc[df_acc['latitude']>0]
    heat_df = heat_df[['latitude', 'longitude']]
    heat_df = heat_df.dropna(axis=0, subset=['latitude','longitude'])

    heat_data = [[row['latitude'],row['longitude']] for index, row in heat_df.iterrows()]

    HeatMap(heat_data).add_to(map_hooray)

    map_hooray.save(output)

for i in range(2014, 2024):
    filepath = f'{i}_reports.csv'
    create_heat_map(filename, f'Heatmaps/{i}_heatmap.html')


# create_heat_map('Heatmaps/dog_reports_2023.csv' , 'Heatmaps/dog_2023_heatmap.html')
# create_heat_map('Heatmaps/dog_reports_2022.csv' , 'Heatmaps/dog_2022_heatmap.html')
# create_heat_map('Heatmaps/dog_reports_2021.csv' , 'Heatmaps/dog_2021_heatmap.html')
# create_heat_map('Heatmaps/dog_reports_2020.csv' , 'Heatmaps/dog_2020_heatmap.html')
# create_heat_map('Heatmaps/dog_reports_2019.csv' , 'Heatmaps/dog_2019_heatmap.html')

def generate_yearly_datasets(filename, year):
    df = pd.read_csv(filename)

    # Convert open_dt to datetime
    df['open_dt'] = pd.to_datetime(df['open_dt'])

    # Filter rows where the year of open_dt is 2014
    df_year = df[df['open_dt'].dt.year == year]

    # Display the filtered DataFrame

    df_year.to_csv(f'Heatmaps/{year}_reports.csv', index=False)


# for i in range(2014, 2024):
#     generate_yearly_datasets('data/FullAnimalReports.csv' , i)


