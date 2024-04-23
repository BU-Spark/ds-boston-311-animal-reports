import pandas as pd

#input
df2013 = pd.read_csv("filtered_2013.csv")
df2014 = pd.read_csv("filtered_2014.csv")
df2015 = pd.read_csv("filtered_2015.csv")
df2016 = pd.read_csv("filtered_2016.csv")
df2017 = pd.read_csv("filtered_2017.csv")
df2018 = pd.read_csv("filtered_2018.csv")
df2019 = pd.read_csv("filtered_2019.csv")
df2020 = pd.read_csv("filtered_2020.csv")
df2021 = pd.read_csv("filtered_2021.csv")
df2022 = pd.read_csv("filtered_2022.csv")
df2023 = pd.read_csv("filtered_2023.csv")
dfs = [df2013, df2014, df2015, df2016, df2017, df2018, df2019, df2020, df2021, df2022, df2023]

#helper function

def get_season_amt (month):
    if month == 12 or month == 1 or month == 2:
        return 0 # winter
    elif month == 3 or month == 4 or month == 5:
        return 1 # spring
    elif month == 6 or month == 7 or month == 8:
        return 2 # summer
    elif month == 9 or month == 10 or month == 11:
        return 3 # fall
    else:
        return -1 
    
#get what we need
all_years= []
amount = ['amount',0,0,0,0]
start = 2013
for df in dfs:
    year_season = [str(start),0,0,0,0]
    date_time = pd.to_datetime(df['open_dt'], format='%Y-%m-%d %H:%M:%S')
    month = date_time.dt.month
    df['seasons'] = month.apply(get_season_amt)
    year_season[1] = df[df['seasons'] == 1]['seasons'].count()
    year_season[2] = df[df['seasons'] == 2]['seasons'].count()
    year_season[3] = df[df['seasons'] == 3]['seasons'].count()
    year_season[4] = df[df['seasons'] == 0]['seasons'].count()
    amount[1] += df[df['seasons'] == 1]['seasons'].count()
    amount[2] += df[df['seasons'] == 2]['seasons'].count()
    amount[3] += df[df['seasons'] == 3]['seasons'].count()
    amount[4] += df[df['seasons'] == 0]['seasons'].count()
    all_years += [year_season]
    start += 1
all_years += [amount]
print(all_years)

#output
df = pd.DataFrame(all_years, columns=['Year', 'Spring', 'Summer', 'Fall', 'winter'])
df.to_csv('season_counts.csv', index=False)




