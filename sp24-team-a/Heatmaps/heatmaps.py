from folium import plugins
from folium.plugins import HeatMap
import folium
import pandas as pd

def create_heat_map(filepath, output):
    map_hooray = folium.Map(location=[42.3601, -71.0589], zoom_start=13) 

    df_acc = pd.read_csv(filepath, dtype=object)
    # Ensure you're handing it floats
    df_acc['latitude'] = df_acc['latitude'].astype(float)
    df_acc['longitude'] = df_acc['longitude'].astype(float)

    # Filter the DF for rows, then columns, then remove NaNs
    heat_df = df_acc[df_acc['latitude']>0] # Reducing data size so it runs faster
    heat_df = heat_df[['latitude', 'longitude']]
    heat_df = heat_df.dropna(axis=0, subset=['latitude','longitude'])

    # List comprehension to make out list of lists
    heat_data = [[row['latitude'],row['longitude']] for index, row in heat_df.iterrows()]

    # Plot it on the map
    HeatMap(heat_data).add_to(map_hooray)

    # Display the map
    map_hooray.save(output)

create_heat_map('dog_lat_long.csv' , 'dog_heatmap.html')
create_heat_map('cat_lat_long.csv' , 'cat_heatmap.html')
create_heat_map('bird_lat_long.csv' , 'bird_heatmap.html')
create_heat_map('bat_lat_long.csv' , 'bat_heatmap.html')
create_heat_map('raccoon_lat_long.csv' , 'raccoon_heatmap.html')