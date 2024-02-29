import pandas as pd
import datetime

# Current year
current_year = datetime.datetime.now().year

# Initialize sums for each category
sum_3_years = 0
sum_5_10_years = 0

# Loop through the years
for year in range(2013, 2024):  # Adjust the range as per your files
    # File name
    file_name = f"filtered_{year}.csv" # the names of each of our files follows this format
    
    try:
        # Load the CSV file
        df = pd.read_csv(file_name)
        
        # Count the number of reports (rows) in this file
        num_reports = len(df)
        print(year, ": ", num_reports)
        
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