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

We conducted a comprehensive analysis of animal complaint data from Boston's 311 service, aiming to enhance the effectiveness of city responses. Our project involved identifying trends over time, analyzing the types of animals involved, and examining the geographic distribution of complaints. We also assessed how seasonal and daily time variations affect complaint patterns. Additionally, our extended analysis included spatial correlation with environmental features like parks and predictive modeling using SARIMA to forecast future complaint volumes.

### Base Analysis
**Objective**: Gain insights into the trends and patterns in animal complaints to improve the 311 service’s effectiveness.

 - **Trend Analysis:** Evaluated animal report volumes from October 2013 to present to assess whether complaint frequency is increasing, stable, or decreasing.
 - **Animal Type Analysis:** Identified which animals are most commonly involved in complaints, aiding in resource prioritization for the 311 service.
 - **Geographic Distribution:** Analyzed the locations of complaints across Boston to pinpoint high-incident areas, informing targeted interventions.
 - **Temporal Analysis:** Examined how seasonal changes and times of day affect complaint patterns, allowing for optimized staffing and resource allocation.

### Extension Analysis 
**Objective:** Delve deeper into the data to uncover nuanced insights that address complex dynamics influencing animal complaints.

- **Hourly and Seasonal Variation:** Investigated how the frequency of animal complaints varies by hour and across different seasons. This analysis helps understand peak times and seasons for different types of animal incidents, enabling tailored response strategies.
- **Spatial and Geographic Correlations:** Analyzed the correlation between animal report frequencies and their proximity to parks. This included studying the spatial distribution across Boston’s neighborhoods to understand the environmental and urban factors affecting animal complaints.
- **Predictive Modeling:** Developed a SARIMA model to forecast the number of animal reports by month, assisting the city in proactive resource planning and operational adjustments.
- **Community Engagement and Reliability:** Evaluated the impact of 311 services over time on community engagement by analyzing the trends in opened and closed cases, providing a measure of the department's responsiveness and effectiveness.
<br>

## Respository Navigation
 - The **AnimalReportsCoordinates** folder contains CSV files with latitude and longitude coordinates for different types of animal complaints within Boston such as bats, birds, cats, dogs, and raccoons. Each CSV is specific to one type of animal, aiding in spatial analysis to determine hotspots and patterns in animal complaints.
   
 - The **Heatmaps** folder contains houses tools and data for generating interactive heatmaps that display the distribution of animal complaints across different areas of Boston. This includes annual datasets and specific animal complaint data, visualized to help identify trends and problem areas effectively.
   
 - The **MLModel** folder contains machine learning models and associated data crucial for predicting and understanding trends in animal complaints. It features Jupyter notebooks for time series modeling with SARIMAX and datasets for analyzing the impact of proximity to parks on animal complaints, alongside other predictive modeling tools.
   
 - The **Maps** folder contains interactive HTML maps for visualizing animal complaints in Boston by type, such as bats, birds, cats, dogs, and raccoons. Each map provides dynamic views of complaint distributions across the city.
   
 - The **Plots** folder is filled with PNG images and Python scripts that generate detailed visualizations of animal complaint data. These visuals cover a range of analytical aspects, including temporal distributions over days, months, and years, and geographic distributions across neighborhoods and zip codes.
   
 - The **Proximity** folder features Python scripts and visual outputs that analyze the proximity of animal complaint reports to parks. This includes calculating distances to the nearest park and examining how this proximity influences the frequency and type of animal complaints, with visuals like histograms to illustrate these relationships.
   
 - The **Stacked Bar Charts for Animal Reports** folder contains detailed bar charts and the underlying data and scripts used to produce them. These charts analyze animal report frequencies by hour throughout different seasons, highlighting how time of day and season affect animal complaint patterns.
   
 - The **Data** folder is the central repository for all datasets used in the project, including comprehensive records of animal complaints, population data, and other relevant information. This folder supports all analytical and modeling tasks by providing the raw and processed data necessary for various analyses.

 - The files in the repository are various and support the analysis, visualization, and reporting of animal complaint data in Boston. Important file 311_Animal_Reports_Team_A.ipynb performs detailed data processing and creates visual representations, helping to uncover trends and patterns in animal-related incidents. PDF files provide formal reports and presentation slides that summarize findings. Additional Python scripts and pictures focus on specific analyses like neighborhood distributions and proximity to parks, enhancing the spatial factors in animal complaints. 

<br>

## Running The Project

To get started with this project, make sure you have Python installed, and install required dependencies such as pandas, numpy, matplotlib, folium, and statsmodels by running pip install in command line. Open the project in a Jupyter Notebook environment to access and execute the analysis notebooks. When running Python scripts from terminal to process data or generate visualizations, ensure that you check which CSV files are needed as input and place them in the same directory; these dependencies are detailed in the repository navigation part. Additionally, you can view the interactive maps and other visual outputs by opening the HTML files in any web browser. This setup will allow you to replicate our analysis, explore the data further, or even build upon the existing framework with new data or methodologies. Thank you for your interest in viewing our work.
