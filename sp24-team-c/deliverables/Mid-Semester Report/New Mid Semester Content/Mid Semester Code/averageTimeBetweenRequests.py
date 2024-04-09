import pandas as pd

# Read the CSV file into a pandas DataFrame
df = pd.read_csv('2011_2024.csv', low_memory=False)

# Convert 'open_dt' column to datetime objects
df['open_dt'] = pd.to_datetime(df['open_dt'])

# Extract year from 'open_dt'
df['year'] = df['open_dt'].dt.year

# Group the DataFrame by year
grouped = df.groupby('year')

# Initialize an empty list to store DataFrames for each year
dfs = []

# Iterate over each group (year)
for year, group in grouped:
    # Sort the data within the group by 'open_dt'
    group_sorted = group.sort_values(by='open_dt')
    
    # Calculate time differences between consecutive 'open_dt' values
    group_sorted['time_difference'] = group_sorted['open_dt'].diff()
    
    
    # Calculate the average time difference for the year
    average_time_between_requests = group_sorted['time_difference'].mean()
    
    # Create a DataFrame with the year and average time difference
    result_df = pd.DataFrame({'Year': [year], 'Average Time Between Requests': [average_time_between_requests]})
    
    # Append the result DataFrame to the list
    dfs.append(result_df)

# Concatenate all DataFrames in the list into a single DataFrame
result_df = pd.concat(dfs, ignore_index=True)
print(result_df)



# Results

#    Year Average Time Between Requests
# 0   2011     0 days 04:42:44.495689655
# 1   2012     0 days 04:01:56.712967235
# 2   2013     0 days 03:23:52.550893550
# 3   2014     0 days 01:53:09.258453586
# 4   2015     0 days 01:36:52.626893239
# 5   2016     0 days 01:22:05.946620883
# 6   2017     0 days 01:18:29.045271178
# 7   2018     0 days 01:16:05.155987242
# 8   2019     0 days 01:06:37.910371969
# 9   2020     0 days 01:03:17.418369800
# 10  2021     0 days 00:55:27.302694136
# 11  2022     0 days 00:50:20.088156381
# 12  2023     0 days 00:47:29.256716417
# 13  2024        0 days 01:09:07.500000


import pandas as pd
import matplotlib.pyplot as plt

# Data
data = {
    'Year': ['2011', '2012', '2013', '2014', '2015', '2016', '2017', '2018', '2019', '2020', '2021', '2022', '2023', '2024'],
    'Average Time Between Requests': ['0 days 04:42:44.495689655', '0 days 04:01:56.712967235', '0 days 03:23:52.550893550', '0 days 01:53:09.258453586', '0 days 01:36:52.626893239', '0 days 01:22:05.946620883', '0 days 01:18:29.045271178', '0 days 01:16:05.155987242', '0 days 01:06:37.910371969', '0 days 01:03:17.418369800', '0 days 00:55:27.302694136', '0 days 00:50:20.088156381', '0 days 00:47:29.256716417', '0 days 01:09:07.500000']
}

# Convert to DataFrame
df = pd.DataFrame(data)

# Convert 'Average Time Between Requests' to timedelta
df['Average Time Between Requests'] = pd.to_timedelta(df['Average Time Between Requests'])

# Plot
plt.figure(figsize=(10, 6))
plt.plot(df['Year'], df['Average Time Between Requests'].dt.total_seconds() / 3600, marker='o')
plt.title('Average Time Between Requests by Year')
plt.xlabel('Year')
plt.ylabel('Average Time Between Requests (hours)')
plt.xticks(rotation=45)
plt.grid(True, linestyle='--', alpha=0.7)
plt.tight_layout()
plt.show()
