import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from matplotlib.ticker import MaxNLocator

# Load the dataset, ensuring zip codes are read as strings to preserve leading zeros
df = pd.read_csv('animal_counts_by_zipcode.csv', dtype={'location_zipcode': str})

# Setting up visualization style
sns.set(style="whitegrid")

# Common settings for the top animals
top_animals = df.groupby('animal')['count'].sum().nlargest(5).index.tolist()


# 2. Year-by-Year Comparison for Each Top Animal
for animal in top_animals:
    plt.figure()
    yearly_data = df[df['animal'] == animal].groupby('year')['count'].sum()
    sns.barplot(x=yearly_data.index, y=yearly_data.values, palette="PuBuGn")
    plt.title(f'Reports per Year: {animal}')
    plt.xlabel('Year')
    plt.ylabel('Number of Reports')
    plt.gca().xaxis.set_major_locator(MaxNLocator(integer=True))
    plt.tight_layout()
    plt.savefig(f'reports_per_year_{animal}.png')
    plt.close()

# 3. Heatmap of Animal Reports by Zip Code and Year
year_zip_counts = df.groupby(['year', 'location_zipcode'])['count'].sum().unstack().fillna(0)
plt.figure(figsize=(12, 10))
sns.heatmap(year_zip_counts.T, cmap="YlGnBu", linewidths=.5)  # Transpose the DataFrame using .T
plt.title('Heatmap of Animal Reports by Zip Code and Year')
plt.xlabel('Year')  # Adjust x-axis label since the axis is flipped
plt.ylabel('Zip Code')  # Adjust y-axis label since the axis is flipped
plt.tight_layout()
plt.savefig('heatmap_animal_reports_by_zip_and_year.png')
plt.close()

# 4. Box Plot of Reports per Animal Type
plt.figure(figsize=(12, 8))
sns.boxplot(x='animal', y='count', data=df[df['animal'].isin(top_animals)], palette="Set3")
plt.title('Box Plot of Reports per Animal Type')
plt.xlabel('Animal Type')
plt.ylabel('Number of Reports')
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig('box_plot_reports_per_animal_type.png')
plt.close()
