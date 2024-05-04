
import pandas as pd

# Load the data
df = pd.read_csv('raw_dataset.csv')

# Replace NaN values with an empty string
df = df.fillna(" ")


# Define a function to replace "assets" and "contents" with " "
def replace_strings(value):
    if 'assets' in str(value) or 'contents' in str(value):
        return ' '
    return value

# Apply the function to each element of the DataFrame
for column in df.columns:
    df[column] = df[column].apply(replace_strings)


# set_id, IMAGE_VERSION_1,IMAGE_VERSION_2,IMAGE_VERSION_3, year, season, product_type, category

#add set_id column as first column
df.insert(0, 'set_id', range(1, 1 + len(df)))

#add year column as next column of the ones we have
df.insert(4, 'year', "")

#add season column as next column of the ones we have
df.insert(5, 'season', "")

#add product_type column as next column of the ones we have
df.insert(6, 'product_type', "")

#add category column as next column of the ones we have
df.insert(7, 'category', "")

def extract_features_url(url):
    url_cutted = url.split("/")
    #print(url_cutted)
    if (url_cutted[7]=="S" or url_cutted[7]=="V"):
        season = "S"
    else:
        season = "W"
    feature_dict = {
        "section": url_cutted[9],
        "product_type": url_cutted[8],
        "season": season,#attention original 4
        "year": url_cutted[6],
        "enc_feature": 0000
    }
    return feature_dict


def extract_and_populate(df):
    for index in range(0, len(df)):
        row = df.loc[index]
        if (len(row["IMAGE_VERSION_1"]) > 1):
            data_dict = extract_features_url(row["IMAGE_VERSION_1"])
        else:
            if (len(row["IMAGE_VERSION_2"]) > 1):
                row["IMAGE_VERSION_1"] = row["IMAGE_VERSION_2"]
                row["IMAGE_VERSION_3"] = row["IMAGE_VERSION_2"]
            else:
                row["IMAGE_VERSION_1"] = row["IMAGE_VERSION_3"]
                row["IMAGE_VERSION_2"] = row["IMAGE_VERSION_3"]        

        #populate the columns year, season, product_type, category with the extracted values
        df.at[index, 'year'] = data_dict["year"]
        df.at[index, 'season'] = data_dict["season"]
        df.at[index, 'product_type'] = data_dict["product_type"]
        df.at[index, 'category'] = data_dict["section"]

    return df

# Call the function to extract parts and populate columns
df = extract_and_populate(df)

# Write the modified DataFrame back to a new CSV file
df.to_csv('modified_file.csv', index=False)

# Delete row if product_type value is 2 or 4
for index in range(0, len(df)):
    row = df.loc[index]
    if (row["product_type"] == 2 or row["product_type"] == 4):
        df = df.drop(index)
    print(index)


for index in range(0, len(df)):
    row = df.loc[index]
    if not(row["year"] == "2023"):
        df = df.drop(index)
    else:
        print(index)



# Save the DataFrame to a new CSV file
df.to_csv('processed_dataset.csv', index=False)