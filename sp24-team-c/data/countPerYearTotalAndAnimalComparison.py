import pandas as pd
import matplotlib.pyplot as plt


# GET TOTAL NUMBER
# # Read the CSV file into a pandas DataFrame
# df = pd.read_csv('animal_related_complaints_2011_2024.csv')

# # Convert the 'open_dt' column to datetime type
# df['open_dt'] = pd.to_datetime(df['open_dt'])

# # Extract the year from the 'open_dt' column
# df['year'] = df['open_dt'].dt.year

# # Bucket count of requests based on the year
# yearly_counts = df['year'].value_counts().sort_index()






# Data TAKEN FROM ORIGINAL CSV FILE TOTAL NUMBER
data_total = {
    'Year': [2011, 2012, 2013, 2014, 2015, 2016, 2017, 2018, 2019, 2020, 2021, 2022, 2023],
    'Value': [58262, 118092, 142610, 147820, 210083, 216535, 251269, 262748, 259022, 251222, 273784, 276599, 313226]
}

# DATA BELOW COMES FROM ABOVE SCRIPTS
data_animal = {
    'Year': [2011, 2012, 2013, 2014, 2015, 2016, 2017, 2018, 2019, 2020, 2021, 2022, 2023],
    'Animal_Reports': [929, 2168, 2575, 4644, 5415, 6408, 6694, 6899, 7878, 8319, 9466, 10437, 11056]
}

# Creating DataFrames
df_total = pd.DataFrame(data_total)
df_animal = pd.DataFrame(data_animal)

# Plotting
plt.figure(figsize=(10, 6))

plt.plot(df_total['Year'], df_total['Value'], marker='o', color='b', label='Total Reports')
plt.plot(df_animal['Year'], df_animal['Animal_Reports'], marker='o', color='r', label='Animal Reports')

plt.title('Number of 311 Reports Over the Years')
plt.xlabel('Year')
plt.ylabel('Value')
plt.grid(True)
plt.xticks(df_total['Year'], rotation=45)
plt.tight_layout()
plt.legend()
plt.savefig('NumberReportsOverYears.png')  # Save the graph as an image
plt.show()








# Calculate the percentage of animal reports out of total reports for each year
df_total['Animal_Percentage'] = (df_animal['Animal_Reports'] / df_total['Value']) * 100

# Plotting
plt.figure(figsize=(10, 6))

plt.plot(df_total['Year'], df_total['Animal_Percentage'], marker='o', color='g', label='Animal Reports Percentage')

plt.title('Percentage of Animal Reports Over Total Reports')
plt.xlabel('Year')
plt.ylabel('Percentage')
plt.grid(True)
plt.xticks(df_total['Year'], rotation=45)
plt.tight_layout()
plt.legend()
plt.savefig('percentageAnimalLine.png')  # Save the graph as an image
plt.show()









# PIE CHART 
# Calculate the total number of animal reports
total_animal_reports = df_animal['Animal_Reports'].sum()

# Plotting
plt.figure(figsize=(10, 6))

# Pie chart
colors = ['#ff9999', '#66b3ff']
explode = (0.1, 0)  # explode the 1st slice
plt.pie([total_animal_reports, df_total['Value'].sum() - total_animal_reports],
        labels=['Animal Reports', 'Other Reports'], autopct='%1.1f%%',
        colors=colors, startangle=140, explode=explode, shadow=True)
plt.title('Percentage of Animal Reports Out of Total Reports')
plt.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle
plt.tight_layout()
plt.savefig('percentageAnimalPie.png')  # Save the graph as an image
plt.show()
