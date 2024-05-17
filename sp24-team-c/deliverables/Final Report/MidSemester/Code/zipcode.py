import pandas as pd
import re  # For regular expressions

# Load the dataset
df = pd.read_csv('2011_2024.csv')

# Filter and rename the relevant columns
relevant_columns = ['open_dt', 'closure_reason', 'location']
df = df[relevant_columns]

# Extract the year from 'open_dt'
df['year'] = pd.to_datetime(df['open_dt']).dt.year

# Filter data from 2011 to 2023
df = df[df['year'].between(2011, 2023)]

# Extract the zip code from the 'location' column using regular expressions
df['location_zipcode'] = df['location'].apply(lambda x: re.findall(r'\b\d{5}\b', x)[-1] if re.findall(r'\b\d{5}\b', x) else None)

# Define the list of animals to check in the 'closure_reason'
animals = {
    ' dog ': 'Dog', ' squirrel ': 'Squirrel', ' cat ': 'Cat', ' bird ': 'Bird', ' bat ': 'Bat', 
    ' raccoon ': 'Raccoon', ' deer ': 'Deer', ' possum ': 'Possum', ' rabbit ': 'Rabbit',
    ' crow ': 'Crow', ' fly ': 'Fly', ' skunk ': 'Skunk', ' hawk ': 'Hawk', ' chicken ': 'Chicken',
    ' goose ': 'Goose', ' coyote ': 'Coyote', ' opossum ': 'Opossum', ' turkey ': 'Turkey',
    ' duck ': 'Duck', ' beaver ': 'Beaver', ' turtle ': 'Turtle', ' owl ': 'Owl', ' snake ': 'Snake',
    ' pigeon ': 'Pigeon', ' gull ': 'Gull', ' ferret ': 'Ferret', ' dragon ': 'Dragon', 
    ' swan ': 'Swan', ' sparrow ': 'Sparrow', ' dove ': 'Dove', ' fish ': 'Fish', 
    ' rooster ': 'Rooster', ' hamster ': 'Hamster', ' falcon ': 'Falcon', ' cardinal ': 'Cardinal',
    ' parakeet ': 'Parakeet', ' raven ': 'Raven', ' jay ': 'Jay', ' fox ': 'Fox', ' quail ': 'Quail',
    ' peacock ': 'Peacock', ' fowl ': 'Fowl', ' pig ': 'Pig', ' frog ': 'Frog', ' bear ': 'Bear', 
    ' ten ': 'Ten', ' chipmunk ': 'Chipmunk', ' lizard ': 'Lizard', ' parrot ': 'Parrot', 
    ' python ': 'Python', ' chinchilla ': 'Chinchilla', ' sheep ': 'Sheep'
}

# Normalize 'closure_reason' to check for animal information and filter out irrelevant data
pattern = '|'.join(animals)  # Creates a pattern like 'Dog|Squirrel|Cat|...'
df['animal'] = df['closure_reason'].apply(lambda x: next((animal for animal in animals if animal.lower() in x.lower()), 'Unknown'))

# Keep only the rows with known animal types
df = df[df['animal'] != 'Unknown']

# Group by year, zip code, and animal type, then count the occurrences
grouped_data = df.groupby(['year', 'location_zipcode', 'animal']).size().reset_index(name='count')

# Export the grouped data to a new CSV file
grouped_data.to_csv('animal_counts_by_zipcode.csv', index=False)

print('Data has been processed and saved to animal_counts_by_zipcode.csv.')
