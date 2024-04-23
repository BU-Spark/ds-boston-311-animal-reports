import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load the dataset into a Pandas DataFrame
df = pd.read_csv('animal_related_animal_counts_by_zipcode.csv')

# Aggregate the data to find the total sightings for each animal across all years
animal_counts = df.groupby('animal')['count'].sum().reset_index(name='count')

# Sort the aggregated data to identify the top 5 animals
top_5_animals = animal_counts.nlargest(5, 'count')

# Filter the original DataFrame to include only data for the top 5 animals
top_5_data = df[df['animal'].isin(top_5_animals['animal'])]

# Assuming your dataset has columns 'Year' and 'Animal' representing the year and the animal seen
# Group the filtered data by year and animal, and then unstack to have one row per animal
top_5_data = top_5_data.groupby(['year', 'animal'])['count'].sum().unstack(fill_value=0)

# Plot a line graph for each of the top 5 animals
plt.figure(figsize=(10, 6))
for animal in top_5_data.columns:
    plt.plot(top_5_data.index, top_5_data[animal], label=animal)

plt.title('Top 5 Animals Seen Over Time')
plt.xlabel('Year')
plt.ylabel('Number of Sightings')
plt.legend()
plt.grid(True)
#plt.show()

plt.savefig('annual_reports_for_overall_top_5_animals.png')
plt.close()
