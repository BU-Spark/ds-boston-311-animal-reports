import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("data/animal_only.csv")

top_10_neighborhoods = df['neighborhood'].value_counts().head(10).index

df_top_10 = df[df['neighborhood'].isin(top_10_neighborhoods)]

top_5_animals = df_top_10['Animal'].value_counts().head(5).index

neighborhood_animal_counts = pd.DataFrame(index=top_10_neighborhoods, columns=top_5_animals)

for neighborhood in top_10_neighborhoods:
    df_neighborhood = df_top_10[df_top_10['neighborhood'] == neighborhood]
    animal_counts = df_neighborhood['Animal'].value_counts().head(5) 
    neighborhood_animal_counts.loc[neighborhood] = animal_counts

plt.figure(figsize=(12, 8))
neighborhood_animal_counts.plot(kind='bar')
plt.title('Top 5 Most Commonly Reported Animals in Top 10 Neighborhoods')
plt.xlabel('Neighborhood')
plt.ylabel('Number of Reports')
plt.xticks(rotation=45, ha='right')


plt.legend(title='Animal', labels=[animal.capitalize() for animal in top_5_animals])
plt.tight_layout()
plt.show()
