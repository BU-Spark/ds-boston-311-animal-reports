import pandas as pd
import os


directory = "."  

animal_related_types = ['Animal Found', 'Animal Generic Request', 'Animal Lost', 'Animal Noise Disturbances', 'Pick up Dead Animal']

animal_complaints_2010_df = pd.DataFrame()


file_path_2010_2014 = os.path.join(directory, "2010_2014.csv")
try:
  
    data_2010_2014 = pd.read_csv(file_path_2010_2014, low_memory=False)

    data_2010_2014['OPEN_DT'] = pd.to_datetime(data_2010_2014['OPEN_DT'], errors='coerce')

    data_2010 = data_2010_2014[data_2010_2014['OPEN_DT'].dt.year == 2010]
    
    filtered_data_2010 = data_2010[data_2010['TYPE'].isin(animal_related_types)]

    animal_complaints_2010_df = pd.concat([animal_complaints_2010_df, filtered_data_2010], ignore_index=True)

    if not animal_complaints_2010_df.empty:

        output_file_path_2010 = os.path.join(directory, "animal_related_complaints_2010.csv")
        
        animal_complaints_2010_df.to_csv(output_file_path_2010, index=False)
        print(f"Animal related complaints for 2010 saved to {output_file_path_2010}")
    else:
        print("No animal-related complaints were found for 2010.")
        
except FileNotFoundError:
    print("File for 2010-2014 not found. Skipping to the next years.")
