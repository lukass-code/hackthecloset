import pandas as pd


''' TO BE FIXED
# Load the CSV file
df = pd.read_csv('images_modified.csv')

# Iterate over each row
for index, row in df.iterrows():
    # Iterate over each column in the row
    for column_name in df.columns:
        # Convert the value to a string
        value = str(row[column_name])
        # Check if the string is long enough and if the 43rd character is '1' or '3'
        if len(value) > 42 and value[42] in ['1', '3']:
            # Remove the entire string
            df.loc[index, column_name] = ''

# Create a mask for rows where all columns are empty
mask = df.apply(lambda row: row.astype(str).str.strip().str.len().sum() == 0, axis=1)

# Drop all rows where all columns are empty
df = df.loc[~mask]

# Save the modified CSV file
df.to_csv('images_men.csv', index=False)
'''






# Load the CSV file
df = pd.read_csv('images_men.csv')

#add set_id column, where id is the index of the row
df.insert(0, 'set_id', range(1, 1 + len(df)))

#after IMAGE_VERSION_3, add year column, where year is the 33rd up to 36th character of IMAGE_VERSION_1
df.insert(4, 'year', df['IMAGE_VERSION_1'].str[33:37])

#after year, add season column, where season is the 38th character of IMAGE_VERSION_1
df.insert(5, 'season', df['IMAGE_VERSION_1'].str[38])

#after season, add product_type column, where product_type is the 40th character of IMAGE_VERSION_1
df.insert(6, 'product_type', df['IMAGE_VERSION_1'].str[40])

#after product_type, add category column, where category is the 42nd character of IMAGE_VERSION_1
df.insert(7, 'category', df['IMAGE_VERSION_1'].str[42])



# Save the modified CSV file
df.to_csv('images_men_df.csv', index=False)


## set_id,IMAGE_VERSION_1,IMAGE_VERSION_2,IMAGE_VERSION_3,year,season,product_type,category
