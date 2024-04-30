# Boston 311 Animal Complaint Analysis Project
<br>

## Project Description/Overview 
This project aims to analyze animal-related complaints reported through the City of Boston's 311 service. The analysis focuses on identifying trends, types of animals involved, geographic distribution of complaints, and seasonal/temporal factors that influence these incidents. The insights derived from this project are intended to help the city enhance its responsiveness and effectiveness in handling animal-related issues.
<br>

## Team Members
 - Muntasir Meah
 - Mohammed Aldahmani
 - Shivam Goyal
 - Sangheon Jeong
 - Yuqi Jin
 - Shanshang Zeng
<br>

## Team Accomplishments
### Base Analysis
Objective: Gain insights into the trends and patterns in animal complaints to improve the 311 service’s effectiveness.

 - Trend Analysis: Evaluated animal report volumes from October 2013 to present to assess whether complaint frequency is increasing, stable, or decreasing.
 - Animal Type Analysis: Identified which animals are most commonly involved in complaints, aiding in resource prioritization for the 311 service.
 - Geographic Distribution: Analyzed the locations of complaints across Boston to pinpoint high-incident areas, informing targeted interventions.
 - Temporal Analysis: Examined how seasonal changes and times of day affect complaint patterns, allowing for optimized staffing and resource allocation.
### Extension Analysis 
Objective: Delve deeper into the data to uncover nuanced insights that address complex dynamics influencing animal complaints.

- Hourly and Seasonal Variation: Investigated how the frequency of animal complaints varies by hour and across different seasons. This analysis helps understand peak times and seasons for different types of animal incidents, enabling tailored response strategies.
- Spatial and Geographic Correlations: Analyzed the correlation between animal report frequencies and their proximity to parks. This included studying the spatial distribution across Boston’s neighborhoods to understand the environmental and urban factors affecting animal complaints.
- Predictive Modeling: Developed a SARIMA model to forecast the number of animal reports by month, assisting the city in proactive resource planning and operational adjustments.
- Community Engagement and Reliability: Evaluated the impact of 311 services over time on community engagement by analyzing the trends in opened and closed cases, providing a measure of the department's responsiveness and effectiveness.
<br>

## Respository Navigation
 - The AnimalReportsCoordinates folder contains CSV files with geographical coordinates for animal complaints in Boston, categorized by animal type such as bats, birds, cats, dogs, and raccoons. Each file includes data specifying the animal type and the corresponding latitude and longitude of reported locations.
   
 - The Heatmaps folder features datasets and scripts essential for generating visualizations of animal complaints across Boston.
   Animal Datasets: CSV files detailing coordinates and timestamps for complaints related to different animals.
   Animal Heatmaps: HTML files with interactive heat maps displaying complaint hotspots by animal type and specific years.
   Annual Datasets: Yearly comprehensive datasets from 2014 to 2023.
   Annual Heatmaps: HTML files for each year from 2014 to 2023, showcasing the geographic distribution of complaints annually.
   heatmaps.py contains Python code to produce and manage heatmaps using Folium, facilitating spatial and temporal analysis.
   
 - The MLModel folder hosts machine learning models and supporting datasets focused on predicting and analyzing trends in animal complaints within Boston. Key components include:
   Utilize SARIMAX and other predictive models to forecast complaint trends and analyze data by animal type.
   Data & Visual Output: Contain historical animal complaint data and geographical information, and includes visualizations to represent data insights, particularly regarding the proximity of animal complaints to parks.
   
 - The Maps folder contains interactive HTML maps for visualizing animal complaints in Boston by type, such as bats, birds, cats, dogs, and raccoons. Each map provides dynamic views of complaint distributions across the city.
   
 - The Plot folder contains a variety of visualizations that illustrate different aspects of animal complaint data in Boston.These visualizations cover temporal patterns (daily, monthly, yearly), geographic distributions (by zip code and neighborhood), and detailed statistical analysis.
   
 - The Proximity folder contains Python scripts and visual outputs that analyze the spatial relationships between animal complaint reports and their proximity to parks in Boston. Python scripts for analyzing animal distribution across neighborhoods and calculating distances to nearby parks.
   
 - The Stacked Bar Charts for Animal Reports for Each Season includes detailed visualizations and scripts that analyze the frequency of animal reports by time of day across different seasons.
   
 - The Data folder serves as the comprehensive source for all datasets used in analysis of animal complaints in Boston. Contains Comprehensive Animal Report Records which provides extensive data from 2013 onwards, enabling detailed historical analysis of animal complaint trends and patterns.Geographical and Temporal report which includes datasets that link animal reports with time stamps and geographic locations, such as proximity to parks, which are crucial for spatial and temporal analyses.Demographic Correlations includes features data that combines animal report information with Boston's population statistics, useful for assessing how demographic factors influence animal complaints.

<br>

## Running The Project
<br>
