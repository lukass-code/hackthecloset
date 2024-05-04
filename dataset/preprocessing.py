import pandas as pd

# Load the CSV file
df = pd.read_csv('images.csv')

# Define the string to remove
remove_string = 'https://static.zara.net/photos///'

# Iterate over each row
for index, row in df.iterrows():
    # Iterate over each column in the row
    for column_name in df.columns:
        # Convert the value to a string
        value = str(row[column_name])
        # Check if the string is long enough and if the 41st character is '4' or '2'
        if len(value) > 40 and value[40] in ['4', '2']:
            # Remove the entire string
            df.loc[index, column_name] = ''
    # Create a mask for rows where all columns are empty
    mask = df.apply(lambda row: row.str.len().sum() == 0, axis=1)

    # Drop all rows where all columns are empty
    df = df.loc[~mask]

# Save the modified CSV file
df.to_csv('images_modified.csv', index=False)