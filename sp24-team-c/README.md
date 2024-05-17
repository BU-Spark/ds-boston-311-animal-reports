# Boston 311 Animal Reports Project

## TEAM C: Eric Gaudreau, Raghu Nema, Mariano Amaya, Sam Dvorin, Shangyuan Chen


### Project Overview
The city of Boston seeks a comprehensive understanding of the nature and distribution of animal-related complaints reported by its residents. This respository collects data collected through the city's 311 reporting system to provide an in-depth analysis of animal complaints, encompassing their frequency, types, locations, and potential influencing factors such as seasonality and weather. This project will assist the city in optimizing resource allocation, developing targeted interventions, and enhancing its responsiveness to animal-related concerns.


### Repository Structure

#### csv
- 2011_2024.csv contains all 311 requests that pertain to an animal related type of requests. This was created by the python file filteranimal.py in EarlyInsights/Code.
- animal_counts_by_zipcode.csv contains the year, location_zipcode, animal type, and count. This was created by the python file zipcode.py in MidSemester/Code.

#### Early Insights Report
- Code folder contains all python files
- - countPerMonth.py counts how many requests were in each month and creates associated graphics
- - countPerTime.py counts how many requests were in each time of day bucket and creates associated graphics
- - countPerYearTotal.py counts how many requests were in each year and creates associated graphics
- - season_graphs.ipynb creates graphics that do the above and compare each year to the previous and next
- - filteranimal.py creates csv of only animal related requests
- Graphics folder contains all graphics
- There is also a copy of our Early Insights Presentation

#### Mid Semester Report
- Code folder contains all python files
- - averageTimeBetweenRequests.py counts the average time between requests per year and creates associated graphics
- - areaCodes.ipynb creates heat map and plot for the number of requests using lat and long
- - gifMaking.ipynb creates individual heatmaps for every year and every month and then creates gifs
- - zipcode.py creates csv containing the year, location_zipcode, animal type, and count
- - visualizeanimal.py, overalltop5.py, and deeper.py all help visualize the the types of different animals over the years
- Graphics folder contains all graphics
- There is also a copy of our Mid Semester Presentation

#### Final Report
- Code folder contains all python files
- - case_title.py counts how many requests pertain to each type of request (Pick Up Dead Animal, etc) and creates associated graphics
- - countLateAndByHowMuch.py counts number of late requests per year
- - countUnclosed.py counts number of unclosed requests per year
- - DemographicZipCode.py and LogisticRegression.py uses data from number of requests in each zipcode and data about population data to plot population density by number of requests
- - weather.ipynb creates plots for number of requests vs amount of snowfall and temperature from meteostat extension
- - zipcodecluster.ipynb creates graphics for clustering request density in each zipcode
- Graphics folder contains all graphics
- There is also a copy of our Final Presentation as well as our Final Report


### Prerequisites
- Python 3.8 or higher
- pip package manager


### GIT
   git clone https://github.com/BU-Spark/ds-boston-311-animal-reports.git
   cd ds-boston-311-animal-reports
   cd sp24-team-c
