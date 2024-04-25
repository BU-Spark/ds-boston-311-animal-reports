from cmath import cos, sin
from math import sqrt
import pandas as pd
import math 
import matplotlib.pyplot as plt

# parks_data = pd.read_csv('ParkCoordinates.csv')
# animal_reports = pd.read_csv('data/animal_only.csv')
# animal_reports.dropna(inplace=True)


# Function to calculate distance using the Haversine formula, from Stack Overflow
def haversine(lat1, long1, lat2, long2):
    lat1_rad = math.radians(lat1)
    long1_rad = math.radians(long1)
    lat2_rad = math.radians(lat2)
    long2_rad = math.radians(long2)

    delta_lat = lat2_rad - lat1_rad
    delta_long = long2_rad - long1_rad

    a = sin(delta_lat / 2) ** 2 + cos(lat1_rad) * cos(lat2_rad) * sin(delta_long / 2) ** 2
    a = max(0, min(1, a.real))

    c = 2 * math.atan2(sqrt(a), sqrt(1 - a))

    R = 3959 # radius of the Earth in miles
    distance = R * c
    
    return distance


def generate_nearest_park_to_report(animal_data, parks_data):
    animal_reports_data = pd.read_csv(animal_data)
    animal_reports_data.dropna(inplace=True)
    parks_data = pd.read_csv(parks_data)
    nearest_parks = []

    for _, row in animal_reports_data.iterrows():
        lat_report = row['latitude']
        long_report = row['longitude']
        
        distances = parks_data.apply(lambda park: haversine(lat_report, long_report, park['Latitude'], park['Longitude']), axis=1)
        
        nearest_park_index = distances.idxmin()
        nearest_park = parks_data.loc[nearest_park_index, 'Park Name']
        
        nearest_parks.append(nearest_park)

    animal_reports_data['Nearest Park'] = nearest_parks

    animal_reports_data.to_csv('animal_reports_nearest_park.csv', index=False)

animal_data = 'data/animal_only.csv'
park_data = 'ParkCoordinates.csv'
generate_nearest_park_to_report(animal_data, park_data)


def calculate_distance_between_report_to_nearest_park(animal_data, park_data):
    animal_reports_data = pd.read_csv(animal_data)
    animal_reports_data.dropna(inplace=True)
    parks_data = pd.read_csv(park_data)
    distances_to_parks = []

    for _, row in animal_reports_data.iterrows():
        lat_report = row['latitude']
        long_report = row['longitude']

        nearest_park_name = row['Nearest Park']

        nearest_park_coords = parks_data[parks_data['Park Name'] == nearest_park_name].iloc[0]
        lat_park = nearest_park_coords['Latitude']
        long_park = nearest_park_coords['Longitude']

        distance = haversine(lat_report, long_report, lat_park, long_park)

        distances_to_parks.append(distance)

    animal_reports_data['Distance to Nearest Park (miles)'] = distances_to_parks

    animal_reports_data.to_csv('animal_reports_nearest_park_and_distance.csv', index=False)

animal_data = 'animal_reports_nearest_park.csv'
park_data = 'ParkCoordinates.csv'
calculate_distance_between_report_to_nearest_park(animal_data, park_data)


def population(filename, population_map):
    pop_data = pd.read_csv(population_map)
  
    animal_reports_data = pd.read_csv(filename)

    animal_reports_data.columns = [
        "Animal", "Case Status", "Date", "Issue", "Address", "Neighborhood",
        "District", "Ward", "Precinct", "Full Address", "Zip Code",
        "Latitude", "Longitude","Nearest Park", "Distance to Nearest Park (miles)"
    ]

    animal_reports_data["Year"] = pd.to_datetime(animal_reports_data["Date"]).dt.year

    merged_df = pd.merge(animal_reports_data, pop_data, on="Year", how="left")
    merged_df.to_csv('animal_reports_population.csv', index=False)
    return merged_df.head()

filename = ('animal_reports_nearest_park_and_distance.csv')
population_map = ('BostonPopulationData.csv.csv')
population(filename, population_map)


# Function to create a bar chart showing the count of total reprots reported near park when the distance to the nearest park is less or equal to 0.25 miles
def number_of_animal_reports_by_park(filename):
    
    animal_reports_data = pd.read_csv(filename)

    filtered_df = animal_reports_data[animal_reports_data['Distance to Nearest Park (miles)'] <= 0.25]

    report_counts = filtered_df['Nearest Park'].value_counts()

    plt.figure(figsize=(8, 6))
    report_counts.plot(kind='bar', color='skyblue', title='Number of Animal Reports by Nearest Park')
    plt.xlabel('Nearest Park')
    plt.ylabel('Number of Reports')
    plt.show() 

#filename = "animal_reports_population.csv"
#number_of_animal_reports_by_park(filename)

# Function to create a stacked bar chart showing the count of different animals reported near park when the distance to the nearest park is less or equal to 0.25 miles
import pandas as pd
import matplotlib.pyplot as plt

def animal_report_count_by_park(filename):
    # Read data from CSV
    animal_reports_data = pd.read_csv(filename)

    # Filter data for parks within 0.25 miles
    filtered_df = animal_reports_data[animal_reports_data['Distance to Nearest Park (miles)'] <= 0.25]

    # Group by park and animal type
    grouped = filtered_df.groupby(['Nearest Park', 'Animal']).size().unstack(fill_value=0)

    # Get top N animals
    N = 5
    top_animals = grouped.sum().nlargest(N).index
    grouped_top = grouped[top_animals]

    # Sum the other animals into a single "Other" column
    other_animals = grouped.columns.difference(top_animals)
    grouped_other = grouped[other_animals].sum(axis=1)

    # Combine the top animals with the "Other" column
    grouped_combined = pd.concat([grouped_top, grouped_other.rename('Other')], axis=1)

    # Add a "Total" column to sort by
    grouped_combined['Total'] = grouped_combined.sum(axis=1)

    # Sort by the total number of reports in ascending order
    grouped_sorted = grouped_combined.sort_values(by='Total', ascending=False)

    # Plot the data
    grouped_sorted.drop(columns='Total').plot(
        kind='bar',
        stacked=True,
        figsize=(10, 6),
        title='Number of Reports by Nearest Park by Animal'
    )

    plt.xlabel('Nearest Park')
    plt.ylabel('Number of Reports')

    # Show the plot
    plt.show()


# Generate code for animal report count by park
filename = "animal_reports_population.csv"
animal_report_count_by_park(filename)  # This should refer to the provided CSV file with the relevant data
