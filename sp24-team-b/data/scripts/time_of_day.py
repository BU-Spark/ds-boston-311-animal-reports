import pandas as pd

#input -- update with file path accordingly
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

#get what we need
all_years= []
amount = ['amount',0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
clean = ['clean',0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
percent = ['percent',0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
start = 2013
for df in dfs:
    year_hour = [str(start),0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
    date_time = pd.to_datetime(df['open_dt'], format='%Y-%m-%d %H:%M:%S')
    df['hour'] = date_time.dt.hour
    for i in range(24):
        year_hour[i+1] = df[df['hour'] == i]['hour'].count()
        amount[i+1] += df[df['hour'] == i]['hour'].count()
        clean[i+1] += df[(df['hour'] == i) & (df['reason'] == 'Street Cleaning')]['hour'].count()
    all_years += [year_hour]
    start += 1
all_years += [amount]

# get percent for amount of street cleaning work being done during these hours
for j in range(24):
    percent[j+1] = round(clean[j+1]/amount[j+1], 2)

all_years += [percent]
print(all_years)  

df = pd.DataFrame(all_years, columns=['Year', '0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12', '13', '14', '15', '16', '17', '18', '19', '20', '21', '22', '23' ])
df.to_csv('hour_counts.csv', index=False)

