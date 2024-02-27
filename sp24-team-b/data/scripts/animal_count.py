import pandas as pd
from collections import defaultdict

animals = [animal.lower() for animal in ['chameleon', 'beagle', 'snake', 'quail', 'skunk', 'nightingale', 
    'beaver', 'frog', 'feral cat', 'hamster', 'fox', 'dog', 'chihuahua', 'rat', 'duck', 'seagull', 
    'turtle', 'mice', 'mouse', 'wasp', 'dragon', 'lizard', 'robin', 'rabbit', 'pigeon', 'owl', 
    'bat', 'hawk', 'seal', 'turkey', 'guinea pig', 'pig', 'goose', 'kitten', 
    'pike', 'bee', 'horse', 'possum', 'stray dog', 'parrot', 'fish', 'raccoon', 
    'coyote', 'falcon', 'ferret', 'chicken', 'goat', 'bird', 'peacock', 'wolf', 'swan', 'cat', 'opossum', 
    'crow', 'squirrel', 'deer', 'snake', 'chipmunk', 'alligator', 'cockroach', 'sparrow', 
    'eagle', 'turtle', 'bed bug']]

# Map variations to primary categories
animal_group_mapping = {
    'stray dog': 'dog',
    'beagle': 'dog',
    'chihuahua': 'dog',
    'kitten': 'cat',
    'feral cat': 'cat',
    'mice' : 'mouse'
}
def get_primary_category(animal):
    return animal_group_mapping.get(animal, animal)
# Initialize a dictionary to hold the sum of occurrences for each animal
animal_counts = defaultdict(int)

# Function to process each file and update the animal_counts dictionary
def process_file(file_path):
    # Read the CSV file
    df = pd.read_csv(file_path)
    # Concatenate the 'closure_reason' and 'type' columns into one series for unified processing
    combined_texts = df['closure_reason'].str.lower()
    if 'type' in df.columns:
        combined_texts = combined_texts.fillna('') + ' ' + df['type'].str.lower().fillna('')
    
    # Process each animal in the list
    for animal in animals:
        primary_category = get_primary_category(animal)
        pattern = rf"\b{animal}s?\b" # Regular expression pattern to match the whole word
        count = combined_texts.str.contains(pattern, regex=True).sum()
        animal_counts[primary_category] += count

# Loop through each year from 2013 to 2023 and process the corresponding file
for year in range(2013, 2024):
    file_name = f"filtered_{year}.csv" # the names of each of our files follows this format
    process_file(file_name)

# sorting by sum of occurrences for each animal
sorted_animal_counts = sorted(animal_counts.items(), key=lambda x: x[1], reverse=True)

# Print the sum of occurrences for each animal
for animal, count in sorted_animal_counts:
    print(f"{animal}: {count}")

# Convert the sorted list to a DataFrame
df = pd.DataFrame(sorted_animal_counts, columns=['Animal', 'Count'])

# Write the DataFrame to a CSV file
csv_file_path = 'animal_counts.csv'
df.to_csv(csv_file_path, index=False)