import pandas as pd
import os

directory = "."  

animal_related_types = ['Animal Found', 'Animal Generic Request', 'Animal Lost', 'Animal Noise Disturbances', 'Pick up Dead Animal']

animal_complaints_df = pd.DataFrame()

for year in range(2011, 2025):

    file_path = os.path.join(directory, f"{year}.csv")
    
    try:
        data = pd.read_csv(file_path, low_memory=False)
        filtered_data = data[data['type'].isin(animal_related_types)]
        
        animal_complaints_df = pd.concat([animal_complaints_df, filtered_data], ignore_index=True)
    except FileNotFoundError:
        print(f"File for {year} not found. Skipping to the next year.")


if not animal_complaints_df.empty:

    output_file_path = os.path.join(directory, "2011_2024.csv")

    animal_complaints_df.to_csv(output_file_path, index=False)
    print(f"Animal related complaints saved to {output_file_path}")
else:
    print("No animal-related complaints were found in the files.")
