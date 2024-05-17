import pandas as pd
import matplotlib.pyplot as plt


# MAY NOT WORK, MANY REQUESTS LABELED OPEN AND ONTIME DONT HAVE A TARGET DATE (DATA SEEMS INCONSISTENT)

filename = '2011_2024.csv'



def count_open_cases_by_status_and_year(filename):
    df = pd.read_csv(filename)
    df['open_dt'] = pd.to_datetime(df['open_dt'])
    
    # Group by case_status and year of 'open_dt' and count the number of cases for each group
    open_cases_by_status_and_year = df[df['case_status'] == 'Open'].groupby([df['open_dt'].dt.year, 'case_status']).size()
    return open_cases_by_status_and_year


open_cases_by_status_and_year = count_open_cases_by_status_and_year(filename)
print("Open Cases by Status and Year:")
print(open_cases_by_status_and_year)




def plot_total_vs_open_cases_by_status_and_year(filename):
    df = pd.read_csv(filename)
    df['open_dt'] = pd.to_datetime(df['open_dt'])
    
    # Count total requests per year
    total_requests_by_year = df.groupby(df['open_dt'].dt.year).size()
    
    # Count open cases by status and year
    open_cases_by_status_and_year = df[df['case_status'] == 'Open'].groupby(df['open_dt'].dt.year).size()
    
    # Reindex open_cases_by_status_and_year to include all years
    open_cases_by_status_and_year = open_cases_by_status_and_year.reindex(total_requests_by_year.index, fill_value=0)
    
    # Calculate percentage of open cases relative to total requests
    percentage_open_cases = (open_cases_by_status_and_year / total_requests_by_year) * 100
    
    # Plot the counts
    plt.figure(figsize=(12, 6))
    index = total_requests_by_year.index
    bar_width = 0.4
    opacity = 0.8
    
    plt.bar(index, total_requests_by_year.values, bar_width, alpha=opacity, color='g', label='Total Requests')
    plt.bar(index, open_cases_by_status_and_year.values, bar_width, alpha=opacity, color='r', label='Open Cases')
    
    # Annotate bars with the percentage of open cases
    for i, year in enumerate(index):
        total_height = total_requests_by_year.values[i]
        open_cases_height = open_cases_by_status_and_year.values[i]
        percentage = percentage_open_cases.values[i]
        plt.text(year, total_height + 0.5, f'{percentage:.1f}%', ha='center', fontsize=9)
    
    plt.xlabel('Year')
    plt.ylabel('Count')
    plt.title('Total Requests vs Open Cases by Year')
    plt.xticks(index)
    plt.legend()
    plt.grid(axis='y', linestyle='--', alpha=0.5)
    plt.tight_layout()
    plt.show()


plot_total_vs_open_cases_by_status_and_year(filename)





def count_overdue_requests_still_open(filename):
    df = pd.read_csv(filename)
    
    # Filter out rows where on_time is labeled as "overdue" and case is still open
    overdue_open_requests = df[(df['on_time'] == 'OVERDUE') & (df['case_status'] == 'Open')]
    
    # Count the number of overdue requests still open
    count_overdue_still_open = len(overdue_open_requests)
    return count_overdue_still_open


count_overdue_still_open = count_overdue_requests_still_open(filename)
print("Number of overdue requests still open:", count_overdue_still_open)





def plot_requests_and_overdue_requests_by_year(filename):
    df = pd.read_csv(filename, low_memory=False)
    df['open_dt'] = pd.to_datetime(df['open_dt'])
    
    # Count total requests per year
    total_requests_by_year = df.groupby(df['open_dt'].dt.year).size()
    
    # Filter out rows where on_time is labeled as "OVERDUE" and case is still open
    overdue_open_requests = df[(df['on_time'] == 'OVERDUE') & (df['case_status'] == 'Open')]
    
    # Group by year of 'open_dt' and count the number of overdue requests still open for each year
    counts_overdue_still_open_by_year = overdue_open_requests.groupby(overdue_open_requests['open_dt'].dt.year).size()
    
    # Reindex the counts_overdue_still_open_by_year to include all years
    counts_overdue_still_open_by_year = counts_overdue_still_open_by_year.reindex(total_requests_by_year.index, fill_value=0)
    
    # Calculate percentages
    percentages = (counts_overdue_still_open_by_year / total_requests_by_year) * 100
    
    # Plot the counts
    plt.figure(figsize=(12, 6))
    bar_width = 0.35
    opacity = 0.8
    index = total_requests_by_year.index
    
    # Plot total requests and overdue requests on the same bar
    plt.bar(index, total_requests_by_year.values, bar_width, alpha=opacity, color='b', label='Total Requests')
    plt.bar(index, counts_overdue_still_open_by_year.values, bar_width, alpha=opacity, color='r', label='Overdue Requests Still Open')

    plt.xlabel('Year')
    plt.ylabel('Number of Requests')
    plt.title('Total Requests vs Overdue Requests Still Open by Year')
    plt.xticks(index)
    plt.legend()
    plt.grid(axis='y', linestyle='--', alpha=0.7)
    
    # Annotate bars with percentages
    for i, v in enumerate(index):
        plt.text(v - 0.1, total_requests_by_year.values[i] + 20, f'{percentages.values[i]:.1f}%', fontsize=9)

    plt.tight_layout()
    plt.show()


plot_requests_and_overdue_requests_by_year(filename)
