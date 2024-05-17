import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# Load data
animal_reports = pd.read_csv('MLModel/animal_reports_population.csv')

# Extract the 'Distance to Nearest Park (miles)' column from the dataset
distances = animal_reports['Distance to Nearest Park (miles)']

bin_edges = np.arange(0, 2.25, 0.25) 

# Plot the histogram with defined bin edges
plt.hist(distances, bins=bin_edges, edgecolor='black')
plt.title("Animal Reports by Distance to Nearest Park")
plt.xlabel("Distance to Nearest Park (miles)")
plt.ylabel("Number of Animal Reports")
file_path = "MLModel/animal_reports_nearest_park_histogram.png"
plt.savefig(file_path)  
plt.show()  

