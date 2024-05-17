import pandas as pd

# list of types to filter for
types_to_filter = ['Pick up Dead Animal',
                   'Bed Bugs', 'Pest Infestation - Residential', 'Animal Lost', 
                   'Animal Generic Request', 'Animal Noise Disturbances', 'Animal Found']

for year in range(2013, 2024):
    file_path = f'{year}.csv'
    
    df = pd.read_csv(file_path, low_memory=False)
    
    filtered_df = df[df['type'].isin(types_to_filter)]
    
    output_file = f'/Path/to/desired/location/file{year}.csv'
    
    filtered_df.to_csv(output_file, index=False)
