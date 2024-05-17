import pandas as pd
import matplotlib.pyplot as plt
import calendar  # For getting month names


# # Read the dataset
# df = pd.read_csv("data/FullAnimalReports.csv")

# # Extract year from 'open_dt' column
# df['open_year'] = pd.to_datetime(df['open_dt']).dt.year

# # Group by year and count the number of reports
# animal_reports_per_year = df.groupby("open_year").size()

# # Create bar chart
# plt.figure(figsize=(12, 6))
# animal_reports_per_year.plot(kind="bar", color="skyblue")
# plt.title("Number of Animal Reports per Year")
# plt.xlabel("Year")
# plt.ylabel("Number of Reports")
# plt.savefig("Plots/Count per year.png")
# # plt.show()  # Display the plot


# Read the dataset
# df = pd.read_csv("data/FullAnimalReports.csv")

# # Extract month from 'open_dt' column
# df['open_month'] = pd.to_datetime(df['open_dt']).dt.month

# # Group by month and count the number of reports
# animal_reports_per_month = df.groupby("open_month").size()

# # Map month numbers to month names
# animal_reports_per_month.index = animal_reports_per_month.index.map(lambda x: calendar.month_name[x])

# # Create bar chart
# plt.figure(figsize=(12, 6))
# animal_reports_per_month.plot(kind="bar", color="skyblue")
# plt.title("Number of Animal Reports by Month")
# plt.xlabel("Month")
# plt.ylabel("Number of Reports")
# plt.xticks(rotation=45, ha='right')
# # Save the bar chart to a file
# plt.savefig("Plots/Count_per_month.png")


# import pandas as pd
# import matplotlib.pyplot as plt

# # Read the dataset
# df = pd.read_csv("data/FullAnimalReports.csv")

# # Extract the hour from 'open_dt' column
# df['open_hour'] = pd.to_datetime(df['open_dt']).dt.hour

# # Group by hour and count the number of reports
# animal_reports_per_hour = df.groupby("open_hour").size()

# # Create bar chart
# plt.figure(figsize=(12, 6))
# animal_reports_per_hour.plot(kind="bar", color="skyblue")
# plt.title("Number of Animal Reports by Hour of the Day")
# plt.xlabel("Hour")
# plt.ylabel("Number of Reports")

# # Save the bar chart to a file
# plt.savefig("Plots/Hours of the day.png")



import pandas as pd
import matplotlib.pyplot as plt

# Read the CSV file
df = pd.read_csv("data/animal_only.csv")

# Count occurrences of each animal in the 'Animal' column
animal_counts = df['Animal'].value_counts()

# Separate top 10 animals and the rest
top_10_animals = animal_counts[:10]
rest_of_animals = animal_counts[10:]

# Combine the rest into "Other"
other_count = rest_of_animals.sum()
other_series = pd.Series({"Other": other_count})

# Concatenate the top 10 animals with the "Other" category
animal_counts_modified = pd.concat([top_10_animals, other_series])

# Create a bar plot with the top 10 animals and the "Other" category
plt.figure(figsize=(10, 6))
animal_counts_modified.plot(kind='bar', color='skyblue', alpha=0.7)
plt.title("Number of Reports by Animal Type (Top 10 + Other)")
plt.xlabel("Animal")
plt.ylabel("Number of Reports")
plt.xticks(rotation=45, ha='right')
plt.savefig("Plots/animal_frequency_top10_other.png")  # Save the plot
plt.show()  # Display the plot


