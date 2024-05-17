import pandas as pd
import matplotlib.pyplot as plt

# Assuming you have your data in a CSV file named 'data.csv'
data = pd.read_csv("/Users/ericgaudreau/Desktop/Mid-Semester Report/csv/2011_2024.csv")

# Convert 'open_dt' column to datetime type
data['open_dt'] = pd.to_datetime(data['open_dt'])

# Extract year from 'open_dt' column
data['year'] = data['open_dt'].dt.year

# Filter out data for the years 2011, 2012, and 2024
data = data[~data['year'].isin([2011, 2012, 2024])]

# Group by year and case title, then count the number of requests
requests_per_year = data.groupby(['year', 'type']).size().unstack(fill_value=0)

# Calculate the total requests per year
total_requests_per_year = requests_per_year.sum(axis=1)

# Calculate the percentage of each case type for each year
percentages = requests_per_year.div(total_requests_per_year, axis=0) * 100

# Plotting
ax = requests_per_year.plot(kind='bar', figsize=(12, 6), width=0.8)
plt.title('Number of Requests per Year Based on Request Type', fontsize=16)
plt.xlabel('Year', fontsize=14)
plt.ylabel('Number of Requests', fontsize=14)
plt.xticks(rotation=45)
plt.legend(title='Request Type', bbox_to_anchor=(1.05, 1), loc='upper left')

# Annotate bars with percentages for 'Pick Up Dead Animal' request type
for i, year in enumerate(percentages.index):
    for j, case_type in enumerate(percentages.columns):
        if case_type == 'Pick up Dead Animal':
            plt.text(i + j * 0.10, requests_per_year.iloc[i, j] + 5, f'{percentages.iloc[i, j]:.2f}%', ha='center', va='bottom', rotation=0, fontsize=8)

plt.tight_layout()
plt.show()
