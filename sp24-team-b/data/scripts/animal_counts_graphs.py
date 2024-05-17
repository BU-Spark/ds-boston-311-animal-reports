import pandas as pd
import matplotlib.pyplot as plt

# Load the data from the CSV file using pandas
df = pd.read_csv('animal_counts.csv') # the csv passed into this script is animal_counts.csv
                                          # this was compiled using the animal_count.py script

# Create a bar plot using the data
bar_plot = df.plot.bar(x='Animal', y='Count', legend=False, color='skyblue', figsize=(20, 10))
bar_plot.set_ylabel("Number of Reports", fontsize=14)
bar_plot.set_xlabel("Animal", fontsize=14)
bar_plot.set_title("Number of Reports by Each Animal 2013-2023", fontsize=18)

# Rotate the x-axis labels to prevent overlap
bar_plot.set_xticklabels(bar_plot.get_xticklabels(), rotation=45, ha="right")

# Adjust the plot to ensure everything fits without overlapping
plt.tight_layout()
plt.savefig('animal_count_bar_graph.png', dpi=300)
plt.show()
