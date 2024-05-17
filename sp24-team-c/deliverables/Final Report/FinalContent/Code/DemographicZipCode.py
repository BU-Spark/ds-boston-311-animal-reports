import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from scipy.stats import linregress
 
zipcodes = [
    '02026',
    '02108',
    '02109',
    '02110',
    '02111',
    '02113',
    '02114',
    '02115',
    '02116',
    '02118',
    '02119',
    '02120',
    '02121',
    '02122',
    '02124',
    '02125',
    '02126',
    '02127',
    '02128',
    '02129',
    '02130',
    '02131',
    '02132',
    '02133',
    '02134',
    '02135',
    '02136',
    '02146',
    '02163',
    '02167',
    '02199',
    '02210',
    '02215',
    '02467'
]

PopulationDensityPeoplePerSquareMile = [
    2412,
    27919,
    21721,
    9355,
    28542,
    68665,
    26694,
    40159, 
    32724,
    24075,
    15871,
    24456,
    14884, 
    11554,
    15913,
    15611,
    12277,
    15744,
    8352,
    12192,
    10618,
    11505,
    5670,
    0, # NA 02133
    16212,
    16236,
    6207,
    0, # NA 02146
    26048,
    0, # NA 02167
    19927,
    2256,
    34190,
    4616
]




## EDITED


zipcodes = [
    '02026',
    '02108',
    '02109',
    '02110',
    '02111',
    '02113',
    '02114',
    '02115',
    '02116',
    '02118',
    '02119',
    '02120',
    '02121',
    '02122',
    '02124',
    '02125',
    '02126',
    '02127',
    '02128',
    '02129',
    '02130',
    '02131',
    '02132',
    '02134',
    '02135',
    '02136',
    '02163',
    '02199',
    '02210',
    '02215',
    '02467'
]


## MORE EDITED

zipcodes = [
    '2026.0',
    '2108.0',
    '2109.0',
    '2110.0',
    '2111.0',
    '2113.0',
    '2114.0',
    '2115.0',
    '2116.0',
    '2118.0',
    '2119.0',
    '2120.0',
    '2121.0',
    '2122.0',
    '2124.0',
    '2125.0',
    '2126.0',
    '2127.0',
    '2128.0',
    '2129.0',
    '2130.0',
    '2131.0',
    '2132.0',
    '2134.0',
    '2135.0',
    '2136.0',
    '2163.0',
    '2199.0',
    '2210.0',
    '2215.0',
    '2467.0'
]

PopulationDensityPeoplePerSquareMile = [
    2412,
    27919,
    21721,
    9355,
    28542,
    68665,
    26694,
    40159, 
    32724,
    24075,
    15871,
    24456,
    14884, 
    11554,
    15913,
    15611,
    12277,
    15744,
    8352,
    12192,
    10618,
    11505,
    5670,
    16212,
    16236,
    6207,
    26048,
    19927,
    2256,
    34190,
    4616
]


zip_pop_dict = dict(zip(zipcodes, PopulationDensityPeoplePerSquareMile))

print(zip_pop_dict)



# Read the CSV file into a pandas DataFrame
df = pd.read_csv("/Users/ericgaudreau/Desktop/Mid-Semester Report/csv/2011_2024.csv")

# Group by zipcode and count the number of requests
requests_per_zipcode = df.groupby('location_zipcode').size().reset_index(name='num_requests')

num_requests_dict = dict(zip(requests_per_zipcode['location_zipcode'].astype(str), requests_per_zipcode['num_requests']))

print(num_requests_dict)














# GRAPH

# Convert string keys to float for zipcodes
num_requests_dict = {float(k): v for k, v in num_requests_dict.items()}

# Create lists to store population density and number of requests
pop_density = []
num_requests = []

# Populate the lists with data from the dictionaries
for zipcode in zipcodes:
    pop_density.append(zip_pop_dict.get(zipcode, 0))
    num_requests.append(num_requests_dict.get(float(zipcode), 0))

# Calculate correlation coefficient
correlation_coefficient = np.corrcoef(pop_density, num_requests)[0, 1]

# Perform linear regression
slope, intercept, r_value, p_value, std_err = linregress(pop_density, num_requests)
line = slope * np.array(pop_density) + intercept

# Plot the data
plt.scatter(pop_density, num_requests)
plt.plot(pop_density, line, color='red', label='Line of Best Fit')
plt.title('Correlation between Population Density and Number of Requests')
plt.xlabel('Population Density (people per square mile)')
plt.ylabel('Number of Requests')
plt.grid(True)

# Add correlation coefficient to the plot
plt.text(10000, 30000, f'Correlation coefficient: {correlation_coefficient:.2f}', fontsize=10, bbox=dict(facecolor='white', alpha=0.5))

plt.show()
