import pandas as pd

# Read the CSV data (assuming you have your CSV file in the same directory)
df = pd.read_csv('data/FullAnimalReports.csv')

# Convert 'open_dt' to datetime and extract year and month
df['open_dt'] = pd.to_datetime(df['open_dt'])
df['open_year'] = df['open_dt'].dt.year
df['open_month'] = df['open_dt'].dt.month

# Group by year, month, and case status
grouped = df.groupby(['open_year', 'open_month', 'case_status']).size().reset_index(name='case_count')

print(grouped)

# Assuming 'grouped' is the DataFrame that has the grouped data
csv_path = 'MLModel/GroupedAnimalReports.csv'  # Change this to your desired file path
grouped.to_csv(csv_path, index=False)  # Save without row indices
