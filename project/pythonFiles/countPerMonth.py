import pandas as pd
import matplotlib.pyplot as plt


#COUNT PER MONTH

# Read the CSV file into a pandas DataFrame
df = pd.read_csv('animal_related_complaints_2011_2024.csv')

# Convert the 'open_dt' column to datetime type
df['open_dt'] = pd.to_datetime(df['open_dt'])

# Extract the month from the 'open_dt' column
df['month'] = df['open_dt'].dt.month

# Bucket count of requests based on the month
monthly_counts = df['month'].value_counts().sort_index()

# Plot the monthly counts
plt.figure(figsize=(10, 6))
ax = monthly_counts.plot(kind='bar')
plt.title('Monthly Counts of Requests')
plt.xlabel('Month')
plt.ylabel('Number of Requests')
plt.xticks(rotation=0)

# Calculate and annotate percentages
total_requests_monthly = monthly_counts.sum()
for i, v in enumerate(monthly_counts):
    percentage = (v / total_requests_monthly) * 100
    ax.text(i, v + 5, f'{percentage:.2f}%', ha='center')

plt.tight_layout()
plt.savefig('countPerMonth.png')  # Save the graph as an image
plt.show()







# COUNT PER SEASON
# Convert the 'open_dt' column to datetime type
df['open_dt'] = pd.to_datetime(df['open_dt'])

# Define a function to map months to seasons
def get_season(month):
    if month in [3, 4, 5]:
        return 'Spring'
    elif month in [6, 7, 8]:
        return 'Summer'
    elif month in [9, 10, 11]:
        return 'Autumn'
    else:
        return 'Winter'

# Extract the month from the 'open_dt' column and map to seasons
df['month'] = df['open_dt'].dt.month
df['season'] = df['month'].apply(get_season)

# Bucket count of requests based on the season
season_counts = df['season'].value_counts()

# Reorder the index to match the desired order
season_counts = season_counts.reindex(['Winter', 'Spring', 'Summer', 'Autumn'])

# Plot the seasonal counts
plt.figure(figsize=(10, 6))
ax = season_counts.plot(kind='bar')
plt.title('Seasonal Counts of Requests')
plt.xlabel('Season')
plt.ylabel('Number of Requests')
plt.xticks(rotation=0)

# Calculate and annotate percentages
total_requests_seasonal = season_counts.sum()
for i, v in enumerate(season_counts):
    percentage = (v / total_requests_seasonal) * 100
    ax.text(i, v + 5, f'{percentage:.2f}%', ha='center')

plt.tight_layout()
plt.savefig('countPerSeason.png')  # Save the graph as an image
plt.show()
