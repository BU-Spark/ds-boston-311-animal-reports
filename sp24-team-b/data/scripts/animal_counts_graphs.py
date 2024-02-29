import pandas as pd
import matplotlib.pyplot as plt

# Load the data from the CSV file using pandas
df = pd.read_csv('Path/to/csv/file.csv') # the csv passed into this script is animal_counts.csv
                                          # this was compiled using the animal_count.py script

# Create a bar plot using the data
plt.figure(figsize=(20, 10))  # Increase the figure size for better readability
bar_plot = df.plot.bar(x='Animal', y='Count', legend=False, color='skyblue', figsize=(20, 10))
bar_plot.set_ylabel("Number of Reports")
bar_plot.set_xlabel("Animal")
bar_plot.set_title("Number of Reports by Each Animal 2013-Present")

# Rotate the x-axis labels to prevent overlap
bar_plot.set_xticklabels(bar_plot.get_xticklabels(), rotation=45, ha="right")

# Adjust the plot to ensure everything fits without overlapping
plt.tight_layout()
plt.show()


# Define a color palette
colors = plt.cm.Paired(range(len(df)))

# Create the pie chart with the defined colors
top_animals = df.nlargest(10, 'Count')  # Select the top 10 animals

explode_values = [0.0] * len(top_animals)
pie_chart = top_animals.plot.pie(
    y='Count',
    labels=top_animals['Animal'],
    autopct='%1.1f%%',  # Show the percentage on the chart
    colors=colors,  # Use the color palette
    startangle=90,  # Start the chart at 90 degrees to align the first section vertically
    shadow=False, 
    explode=explode_values, 
    figsize= (15,10)
)

# Hide the 'Count' label on the y-axis
pie_chart.set_ylabel("")
pie_chart.set_title('Top 10 Animals Reported')

# Adjust the plot to ensure everything fits without overlapping
plt.tight_layout()

# Display the plot
plt.show()
