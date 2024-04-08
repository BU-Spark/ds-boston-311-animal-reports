import pandas as pd
import matplotlib.pyplot as plt


def non_empty_animal_reports(filepath):
    df = pd.read_csv(filepath, dtype=object)
    df['Animal'] = df['Animal'].str.strip()
    df = df[df['Animal'] != '']
    df.to_csv(f'animal_only.csv', index=False)
    print(df)


def create_animal_frequency_to_hourly_csv(filepath):
    df = pd.read_csv(filepath, dtype=object)
    time_and_animal_df = df[['Animal', 'open_dt']]
    time_and_animal_df.to_csv(f'animal_and_time_df.csv', index=False)

def generate_bar_chart_for_hour():
    df = pd.read_csv("animal_and_time_df.csv", dtype=object)
    animal_list = list(df['Animal'])
    date_list = list(df['open_dt'])

    data = {
        "Animal": animal_list,
        "open_dt": date_list
    }

    df['open_dt'] = pd.to_datetime(df['open_dt'])

    df['hour'] = df['open_dt'].dt.hour

    grouped = df.groupby(['hour', 'Animal']).size().unstack(fill_value=0)

    N = 9
    top_animals = grouped.sum().nlargest(N).index
    grouped_top = grouped[top_animals]

    other_animals = grouped.columns.difference(top_animals)
    grouped_other = grouped[other_animals].sum(axis=1)

    grouped_combined = pd.concat([grouped_top, grouped_other.rename('Other')], axis=1)

    grouped_combined.plot(kind='bar', stacked=True, figsize=(10, 6))
    plt.title('Animal Reports by Hour')
    plt.xlabel('Hour of the Day')
    plt.ylabel('Number of Reports')
    plt.xticks(rotation=0)
    plt.legend(title='Animal')
    plt.show()


def generate_stacked_bar_chart_by_hour_by_season(season, df):
    season = season.lower()
    
    df['open_dt'] = pd.to_datetime(df['open_dt'])
    if season == 'winter':
        df_season = df[(df['open_dt'].dt.month == 1) | (df['open_dt'].dt.month == 2) | (df['open_dt'].dt.month == 12)]
    elif season == 'spring':
        df_season = df[(df['open_dt'].dt.month == 3) | (df['open_dt'].dt.month == 4) | (df['open_dt'].dt.month == 5)]
    elif season == 'summer':
        df_season = df[(df['open_dt'].dt.month == 6) | (df['open_dt'].dt.month == 7) | (df['open_dt'].dt.month == 8)]
    else:
        df_season = df[(df['open_dt'].dt.month == 9) | (df['open_dt'].dt.month == 10) | (df['open_dt'].dt.month == 11)]

    df_season['hour'] = df_season['open_dt'].dt.hour

    grouped = df_season.groupby(['hour', 'Animal']).size().unstack(fill_value=0)

    N = 5 
    top_animals = grouped.sum().nlargest(N).index
    grouped_top = grouped[top_animals]

    other_animals = grouped.columns.difference(top_animals)
    grouped_other = grouped[other_animals].sum(axis=1)

    grouped_combined = pd.concat([grouped_top, grouped_other.rename('Other')], axis=1)

    grouped_combined.plot(kind='bar', stacked=True, figsize=(10, 6))

    plt.title(f'Animal Reports by Hour in the {season}')
    plt.xlabel('Hour of the Day')
    plt.ylabel('Number of Reports')
    plt.xticks(rotation=0)
    plt.legend(title='Animal')

    # plt.savefig(f'Stacked Bar Charts for Animal Reports for Each Season by Hour/animal_reports_by_hour_in_{season}.png')

    plt.show()

df =  df = pd.read_csv("Stacked Bar Charts for Animal Reports for Each Season by Hour/animal_and_time_df.csv", dtype=object)
generate_stacked_bar_chart_by_hour_by_season('fall' , df)