import pandas as pd

def filter_dog_reports(file_path, output_path):
    df = pd.read_csv(file_path)
    
    # concatenate 'closure_reason' and 'type' columns for unified processing.
    df['combined_info'] = df['closure_reason'].astype(str) + ' ' + df['type'].astype(str)
    
    keywords = ['dog', 'stray dog', 'beagle', 'chihuahua']
    
    dog_reports = df[df['combined_info'].str.lower().apply(lambda x: any(keyword in x for keyword in keywords))]
    
    dog_reports.to_csv(output_path, index=False)
    print(f"Filtered dataset saved to {output_path}")

base_input_path = 'filtered_{}.csv'
base_output_path = '/Path/to/desired/output/file{}.csv' # {} for each year

for year in range(2013, 2024):
    input_path = base_input_path.format(year)
    output_path = base_output_path.format(year)
    
    filter_dog_reports(input_path, output_path)


