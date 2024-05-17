import pandas as pd
import datetime
import matplotlib.pyplot as plt
import numpy as np


# Current year
current_year = datetime.datetime.now().year

# Initialize sums for each category
sum_3_years = 0
sum_5_10_years = 0

# Lists to store data for the scatter plot
years = []
num_reports_list = []

# Loop through the years
for year in range(2013, 2024):  # Adjust the range as per your files
    # File name
    file_name = f"filtered_{year}.csv" # this is the format for our datasets
    
    try:
        # Load the CSV file
        df = pd.read_csv(file_name)
        
        # Count the number of reports (rows) in this file
        num_reports = len(df)
        print(year, ": ", num_reports)
        
        # Append data to lists for scatter plot
        years.append(year)
        num_reports_list.append(num_reports)
        
        # Check which category the year belongs to and add to the appropriate sum
        if current_year - year <= 3:
            sum_3_years += num_reports
        elif 5 <= current_year - year <= 10:
            sum_5_10_years += num_reports
            
    except FileNotFoundError:
        print(f"File {file_name} not found. Skipping...")
        continue

# Results
print(f"Number of reports in the last 2-3 years: {sum_3_years}")
print(f"Number of reports in the last 5-10 years: {sum_5_10_years}")

# Create a DataFrame for the scatter plot
scatter_data = pd.DataFrame({'Year': years, 'Number of Reports': num_reports_list})

# Scatter plot using pandas
ax = scatter_data.plot.scatter(x='Year', y='Number of Reports', title='Number of Reports Over Years')
plt.xlabel('Year')
plt.ylabel('Number of Reports')

# Add a trend line
z = np.polyfit(scatter_data['Year'], scatter_data['Number of Reports'], 1)
p = np.poly1d(z)
ax.plot(scatter_data['Year'], p(scatter_data['Year']), color='red', linestyle='--', label='Trend Line')

# Annotate each point with the number of reports
for i, txt in enumerate(scatter_data['Number of Reports']):
    ax.annotate(txt, (scatter_data['Year'][i], scatter_data['Number of Reports'][i]), ha='right', va='bottom')

plt.legend()
plt.show()

# Create a DataFrame for the bar graph
bar_data = pd.DataFrame({'Year': years, 'Number of Reports': num_reports_list})

# Bar graph using pandas
bar_data.plot.bar(x='Year', y='Number of Reports', color='skyblue', legend=False)
plt.title('Bar Graph of Number of Reports Over Years')
plt.xlabel('Year')
plt.ylabel('Number of Reports')
plt.show()

