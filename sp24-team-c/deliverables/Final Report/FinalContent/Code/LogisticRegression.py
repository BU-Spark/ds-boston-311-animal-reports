import pandas as pd
import numpy as np
import statsmodels.api as sm
import matplotlib.pyplot as plt

# Your data
zipcodes = [
    '2026.0', '2108.0', '2109.0', '2110.0', '2111.0', '2113.0', '2114.0', '2115.0', '2116.0', '2118.0',
    '2119.0', '2120.0', '2121.0', '2122.0', '2124.0', '2125.0', '2126.0', '2127.0', '2128.0', '2129.0',
    '2130.0', '2131.0', '2132.0', '2134.0', '2135.0', '2136.0', '2163.0', '2199.0', '2210.0', '2215.0', '2467.0'
]

PopulationDensityPeoplePerSquareMile = [
    2412, 27919, 21721, 9355, 28542, 68665, 26694, 40159, 32724, 24075, 15871, 24456, 14884, 11554, 15913,
    15611, 12277, 15744, 8352, 12192, 10618, 11505, 5670, 16212, 16236, 6207, 26048, 19927, 2256, 34190, 4616
]

zip_pop_dict = dict(zip(zipcodes, PopulationDensityPeoplePerSquareMile))

# Read the CSV file into a pandas DataFrame
df = pd.read_csv("/Users/ericgaudreau/Desktop/Mid-Semester Report/csv/2011_2024.csv")

# Group by zipcode and count the number of requests
requests_per_zipcode = df.groupby('location_zipcode').size().reset_index(name='num_requests')
num_requests_dict = dict(zip(requests_per_zipcode['location_zipcode'].astype(str), requests_per_zipcode['num_requests']))

# Convert string keys to float for zipcodes
num_requests_dict = {float(k): v for k, v in num_requests_dict.items()}

# Create lists to store population density and number of requests
pop_density = []
num_requests = []

# Populate the lists with data from the dictionaries
for zipcode in zipcodes:
    pop_density.append(zip_pop_dict.get(zipcode, 0))
    num_requests.append(num_requests_dict.get(float(zipcode), 0))

# Calculate the average number of requests for all zip codes
average_requests = np.mean(num_requests)
print("Average number of requests for all zip codes:", average_requests)

# Define a threshold for the number of requests
threshold = average_requests  # You can adjust this threshold based on your specific problem

# Create a binary outcome variable based on the threshold
binary_outcome = [1 if num > threshold else 0 for num in num_requests]

# Perform logistic regression
logit_model = sm.Logit(binary_outcome, sm.add_constant(np.array(pop_density)))
result = logit_model.fit()

# Print the summary of the logistic regression model
print(result.summary())


# Scatter plot of the data
plt.scatter(pop_density, binary_outcome, color='blue', label='Observed Data')

# Plot the logistic curve
x_values = np.linspace(min(pop_density), max(pop_density), 100)
y_values = result.predict(sm.add_constant(x_values))
plt.plot(x_values, y_values, color='red', label='Logistic Curve')

plt.title('Logistic Regression')
plt.xlabel('Population Density (people per square mile)')
plt.ylabel('Probability of Exceeding Average Number of Requests per Zip Code')
plt.legend()
plt.grid(True)
plt.show()