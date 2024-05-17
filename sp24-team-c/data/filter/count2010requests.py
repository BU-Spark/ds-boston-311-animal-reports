import pandas as pd
import os

directory = "."  


file_path_2010_2014 = os.path.join(directory, "2010_2014.csv")
try:

    data_2010_2014 = pd.read_csv(file_path_2010_2014, low_memory=False)
    
    data_2010_2014['OPEN_DT'] = pd.to_datetime(data_2010_2014['OPEN_DT'], errors='coerce')

    data_2010 = data_2010_2014[data_2010_2014['OPEN_DT'].dt.year == 2010]
    total_requests_2010 = len(data_2010)
    
    print(f"Total number of requests in 2010: {total_requests_2010}")
        
except FileNotFoundError:
    print("File for 2010-2014 not found.")
