import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Load data
park_data = pd.read_csv('ParkCoordinates.csv')
park_coordinates = park_data[['Latitude', 'Longitude']].values

animal_reports = pd.read_csv('data/animal_only.csv')
animal_reports.dropna(inplace=True)

x = animal_reports["latitude"]
y = animal_reports["longitude"]
data = np.array(list(zip(x, y)))

# Function to calculate distance between two points in miles
def distance_in_miles(point1, point2):
    lat_diff = (point1[0] - point2[0]) * 69  # Convert latitude difference to miles
    lon_diff = (point1[1] - point2[1]) * 69  # Convert longitude difference to miles (approximation)
    return np.sqrt(lat_diff**2 + lon_diff**2)

# Assign each data point to its nearest park cluster and calculate distance in miles
nearest_park_clusters = []
distances = []
for point in data:
    min_distance = float('inf')
    nearest_cluster = None
    for i, park in enumerate(park_coordinates):
        dist = distance_in_miles(point, park)
        if dist < min_distance:
            min_distance = dist
            nearest_cluster = i
    nearest_park_clusters.append(nearest_cluster)
    distances.append(min_distance)

# Colors for clusters
colors = [
    'olive', 'silver', 'rosybrown', 'olivedrab', 'darkcyan', 'navy', 'plum', 'lightcoral', 'coral', 'yellowgreen', 'red', 'blue', 'green', 'orange', 'purple', 'brown', 'pink', 'yellow', 'black', 'teal', 'skyblue', 'chocolate'
]

# Assign colors based on distance
cluster_colors = []
for dist, cluster in zip(distances, nearest_park_clusters):
    if dist > 0.25:  # More than 0.25 miles
        cluster_colors.append("gray")  # Color in gray
    else:
        cluster_colors.append(colors[cluster % len(colors)])  # Original colors

# Plotting
plt.figure(figsize=(22.5, 18))
plt.scatter(y, x, c=cluster_colors, s=30, alpha=0.8)  # Data points

# Plotting park coordinates with markers and unique colors
for i, park in enumerate(park_coordinates):
    plt.scatter(park[1], park[0], marker='x', color=colors[i % len(colors)], s=100, label=park_data.iloc[i]['Park Name'])

# Positioning the legend outside the plot
plt.legend(loc='center left', bbox_to_anchor=(1, 0.5), fontsize=10, frameon=False)  # Position the legend outside and remove frame

plt.title('Clustering of Animal Reports Relative to Nearest Park if Distance <= 0.25')
plt.xlabel('Longitude')
plt.ylabel('Latitude')
plt.show()
