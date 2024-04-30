import pandas as pd
import matplotlib.pyplot as plt


filename = '2011_2024.csv'


def count_rows_with_closed_dt_larger_than_target(filename):
    df = pd.read_csv(filename)
    df['closed_dt'] = pd.to_datetime(df['closed_dt'])
    df['sla_target_dt'] = pd.to_datetime(df['sla_target_dt'])
    count = len(df[df['closed_dt'] > df['sla_target_dt']])
    return count


def average_time_difference(filename):
    df = pd.read_csv(filename)
    df['closed_dt'] = pd.to_datetime(df['closed_dt'])
    df['sla_target_dt'] = pd.to_datetime(df['sla_target_dt'])
    df['time_difference'] = df['closed_dt'] - df['sla_target_dt']
    average_difference = df['time_difference'].mean()
    return average_difference


def average_time_difference_for_late_requests(filename):
    df = pd.read_csv(filename)
    df['closed_dt'] = pd.to_datetime(df['closed_dt'])
    df['sla_target_dt'] = pd.to_datetime(df['sla_target_dt'])
    df['time_difference'] = df['closed_dt'] - df['sla_target_dt']
    
    # Filter out rows where closed_dt is not greater than sla_target_dt
    late_requests = df[df['closed_dt'] > df['sla_target_dt']]
    
    # Calculate the average time difference for late requests
    average_difference = late_requests['time_difference'].mean()
    return average_difference


def plot_counts_of_late_requests_by_year(filename):
    df = pd.read_csv(filename)
    df['closed_dt'] = pd.to_datetime(df['closed_dt'])
    df['sla_target_dt'] = pd.to_datetime(df['sla_target_dt'])
    
    # Filter out rows where closed_dt is greater than sla_target_dt
    late_requests = df[df['closed_dt'] > df['sla_target_dt']]
    
    # Group by year of 'closed_dt' and count the number of rows for each year
    counts_by_year = late_requests.groupby(late_requests['closed_dt'].dt.year).size()
    
    # Plot the counts
    plt.figure(figsize=(10, 6))
    counts_by_year.plot(kind='bar', color='skyblue')
    plt.title('Counts of Late Requests by Year')
    plt.xlabel('Year')
    plt.ylabel('Number of Late Requests')
    plt.xticks(rotation=45)
    plt.grid(axis='y', linestyle='--', alpha=0.7)
    plt.tight_layout()
    plt.show()

import pandas as pd
import matplotlib.pyplot as plt

def plot_total_vs_late_requests_by_year(filename):
    df = pd.read_csv(filename)
    df['closed_dt'] = pd.to_datetime(df['closed_dt'])
    df['sla_target_dt'] = pd.to_datetime(df['sla_target_dt'])
    
    # Group by year of 'closed_dt' and count the total number of requests and late requests for each year
    total_requests_by_year = df.groupby(df['closed_dt'].dt.year).size()
    late_requests_by_year = df[df['closed_dt'] > df['sla_target_dt']].groupby(df['closed_dt'].dt.year).size()
    
    # Calculate the percentage of late requests relative to the total requests
    percentage_late_requests = (late_requests_by_year / total_requests_by_year) * 100
    
    # Plot the counts
    plt.figure(figsize=(12, 6))
    bar_width = 0.35
    index = total_requests_by_year.index
    
    # Plot total requests
    plt.bar(index, total_requests_by_year.values, label='Total Requests', color='skyblue', width=bar_width)
    
    # Overlay late requests on top of total requests
    plt.bar(index, late_requests_by_year.values, label='Late Requests', color='salmon', width=bar_width)
    
    plt.title('Total Requests vs Late Requests by Year')
    plt.xlabel('Year')
    plt.ylabel('Number of Requests')
    plt.xticks(index)
    plt.legend()
    
    # Annotate bars with the percentage of late requests
    for i, late_count in enumerate(late_requests_by_year.values):
        total_count = total_requests_by_year.values[i]
        percentage = percentage_late_requests.values[i]
        plt.text(index[i], max(total_count, late_count) + 10, f'{percentage:.2f}%', ha='center', fontsize=9)
    
    plt.grid(axis='y', linestyle='--', alpha=0.7)
    plt.tight_layout()
    plt.show()




count = count_rows_with_closed_dt_larger_than_target(filename)
print("Number of rows with 'closed_dt' larger than 'sla_target_dt':", count)


# NOT THAT HELPFUL BECAUSE SOME CASES ARE OPEN FOR YEARS AFTER AND MESS WITH THE AVERAGE
average_difference = average_time_difference(filename)
print("Average time difference between 'closed_dt' and 'sla_target_dt':", average_difference)


average_difference_late = average_time_difference_for_late_requests(filename)
print("Average time difference for late requests between 'closed_dt' and 'sla_target_dt':", average_difference_late)


plot_counts_of_late_requests_by_year(filename)


plot_total_vs_late_requests_by_year(filename)


