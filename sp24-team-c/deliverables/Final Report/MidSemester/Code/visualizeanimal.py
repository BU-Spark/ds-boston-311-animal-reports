import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load the dataset, ensuring zip codes are read as strings to preserve leading zeros
df = pd.read_csv('animal_counts_by_zipcode.csv', dtype={'location_zipcode': str})

# Setting up visualization style
sns.set(style="whitegrid")

# 1. Total count of each animal type
plt.figure(figsize=(12, 8))
total_counts = df.groupby('animal')['count'].sum().sort_values(ascending=False)
ax = sns.barplot(x=total_counts.values, y=total_counts.index, palette="viridis")
plt.title('Total Count of Each Animal Type (2011-2023)')
plt.xlabel('Total Counts')
plt.ylabel('Animal Types')

# Adding count labels to the end of each bar
for i, count in enumerate(total_counts.values):
    ax.text(count + 0.1, i, f'{count}', va='center')


plt.savefig('total_counts_by_animal.png')  # Save the figure to your directory
plt.close()  # Close the figure context

# 2. Distribution of animal reports per year
plt.figure(figsize=(12, 8))
yearly_counts = df.groupby('year')['count'].sum()
sns.lineplot(x=yearly_counts.index, y=yearly_counts.values, marker='o', color='b')
plt.title('Distribution of Animal Reports Per Year')
plt.xlabel('Year')
plt.ylabel('Number of Reports')
plt.grid(True)
plt.savefig('animal_reports_per_year.png')  # Save the figure to your directory
plt.close()  # Close the figure context

# 3. Distribution of animal reports per zip code (Top 20)
plt.figure(figsize=(12, 8))
zipcode_counts = df.groupby('location_zipcode')['count'].sum().sort_values(ascending=False).head(20)
sns.barplot(x=zipcode_counts.values, y=zipcode_counts.index, palette="rocket")
plt.title('Top 20 Zip Codes by Number of Animal Reports')
plt.xlabel('Number of Reports')
plt.ylabel('Zip Codes')
plt.savefig('top_20_zip_codes.png')  # Save the figure to your directory
plt.close()  # Close the figure context



# 5. Number of different animal reports in each zip code
plt.figure(figsize=(12, 8))
unique_animal_reports = df.groupby('location_zipcode')['animal'].nunique().sort_values(ascending=False).head(20)
sns.barplot(x=unique_animal_reports.index, y=unique_animal_reports.values, palette="pastel")
plt.title('Number of Different Animal Types Reported in Each Zip Code (Top 20)')
plt.xlabel('Zip Code')
plt.ylabel('Number of Different Animal Types')
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig('unique_animal_reports_per_zipcode.png')
plt.close()

