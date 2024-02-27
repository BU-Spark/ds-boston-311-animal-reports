import pandas as pd

# List of types to filter for
types_to_filter = ['Pick up Dead Animal', 'Rodent Activity', 'Mice Infestation - Residential',
                   'Bed Bugs', 'Pest Infestation - Residential', 'Animal Lost', 
                   'Animal Generic Request', 'Animal Noise Disturbances', 'Animal Found', 'Rat Bite']

# Loop through years 2013 to 2023
for year in range(2013, 2024):
    # Construct file path for each year
    file_path = f'{year}.csv'
    
    # Read CSV file for the current year
    df = pd.read_csv(file_path, low_memory=False)
    
    # Filter DataFrame for types in the specified list
    filtered_df = df[df['type'].isin(types_to_filter)]
    
    # Construct output file path for the filtered data
    output_file = f'Path/To/csv/file{year}.csv'
    
    # Write filtered DataFrame to CSV
    filtered_df.to_csv(output_file, index=False)
