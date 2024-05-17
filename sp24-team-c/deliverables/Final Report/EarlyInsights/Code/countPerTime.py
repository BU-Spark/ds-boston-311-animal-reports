import pandas as pd
import matplotlib.pyplot as plt



# COUNT PER TIME OF DAY
# Read the CSV file into a pandas DataFrame
df = pd.read_csv('2011_2024.csv')

# Convert the 'open_dt' column to datetime type
df['open_dt'] = pd.to_datetime(df['open_dt'])

# Define a function to map hours to time of day
def get_time_of_day(hour):
    if 6 <= hour < 12:
        return 'Morning (6 AM to 12 PM)'
    elif 12 <= hour < 18:
        return 'Noon (12 PM to 6 PM)'
    elif 18 <= hour < 24:
        return 'Night (6 PM to 12 AM)'
    else:
        return 'Late Night (12 AM to 6 AM)'

# Extract the hour from the 'open_dt' column and map to time of day
df['hour'] = df['open_dt'].dt.hour
df['time_of_day'] = df['hour'].apply(get_time_of_day)

# Bucket count of requests based on the time of day
time_of_day_counts = df['time_of_day'].value_counts()

# Reorder the index to match the desired order
time_of_day_counts = time_of_day_counts.reindex(['Morning (6 AM to 12 PM)', 'Noon (12 PM to 6 PM)', 'Night (6 PM to 12 AM)', 'Late Night (12 AM to 6 AM)'])

# Calculate percentages
total_requests = time_of_day_counts.sum()
percentages = (time_of_day_counts / total_requests) * 100

# Plot the time of day counts
ax = time_of_day_counts.plot(kind='bar', figsize=(10, 6))
plt.title('Time of Day Counts of Requests')
plt.xlabel('Time of Day')
plt.ylabel('Number of Requests')
plt.xticks(rotation=45)
plt.grid(False)  # Remove grid lines
plt.tight_layout()

# Annotate bars with percentages
for i, v in enumerate(time_of_day_counts):
    ax.text(i, v + 0.5, f'{percentages[i]:.1f}%', ha='center')

plt.savefig('countPerTimeOfDay.png')  # Save the graph as an image
plt.show()
