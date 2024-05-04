import os
import pandas as pd
import requests

# Function to download an image from a URL and save it to a specified path
def download_image(url, path):
    response = requests.get(url)
    if response.status_code == 200:
        with open(path, 'wb') as file:
            file.write(response.content)
            return True
    else:
        print(f"Failed to download image from {url}")
        return False

# Load DataFrame from CSV file
df = pd.read_csv(r"C:\Users\roksh\OneDrive\Desktop\GitHub\hackthecloset\dataset\holy_grail.csv")  # Replace 'your_dataset.csv' with the path to your CSV file

# Directory to save the dataset
dataset_dir = r'C:\Users\roksh\OneDrive\Desktop\GitHub\hackthecloset\dataset'

# Create the dataset directory if it doesn't exist
os.makedirs(dataset_dir, exist_ok=True)

# Iterate over each row in the DataFrame
for index, row in df.iterrows():
    set_id = row['set_id']
    set_dir = os.path.join(dataset_dir, f"set_{set_id}")
    
    # Create directory for the set
    os.makedirs(set_dir, exist_ok=True)
    
    # Download and save images for each set
    for i in range(1, 4):  # Assuming there are 3 images per set
        image_url = row[f'IMAGE_VERSION_{i}']
        if image_url == ' ':
          continue
        print(image_url, type(image_url))
        image_path = os.path.join(set_dir, f"image_{i}.jpg")
        download_image(image_url, image_path)