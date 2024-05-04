import os
import cv2
import numpy as np
import tensorflow as tf
from tensorflow.keras.applications import ResNet50
from tensorflow.keras.applications.resnet50 import preprocess_input

# Load pre-trained ResNet model
resnet_model = ResNet50(weights='imagenet', include_top=False, pooling='avg')

# Function to preprocess images and extract ResNet features
def preprocess_and_extract_features(image):
    # Resize image to match ResNet input size (usually 224x224)
    resized_image = cv2.resize(image, (224, 224))

    # Normalize the image to range [-1, 1] (required for ResNet)
    normalized_image = preprocess_input(resized_image)

    # Reshape image for batch processing (ResNet expects batch input)
    batch_image = np.expand_dims(normalized_image, axis=0)

    # Extract features using ResNet model
    resnet_features = resnet_model.predict(batch_image)

    return resnet_features

# Path to your dataset directory
dataset_path = r"C:\Users\roksh\OneDrive\Desktop\GitHub\hackthecloset\dataset"

# Initialize dictionary to store average features for each item
item_avg_features = {}

# Iterate through the dataset directory
for set_folder in os.listdir(dataset_path):
    set_folder_path = os.path.join(dataset_path, set_folder)
    if os.path.isdir(set_folder_path):
        print(f"Processing images in {set_folder}...")
        
        # Initialize list to store features for variants of the current item
        variant_features = []
        
        for image_name in os.listdir(set_folder_path):
            image_path = os.path.join(set_folder_path, image_name)
            # Load image
            image = cv2.imread(image_path)
            if image is not None:
                # Preprocess image and extract ResNet features
                resnet_features = preprocess_and_extract_features(image)
                
                # Add ResNet features to list of variant features
                variant_features.append(resnet_features)
            else:
                print(f"Failed to load image: {image_path}")
        
        # Compute average feature vector for variants of the current item
        if variant_features:
            avg_feature_vector = np.mean(variant_features, axis=0)
            # Store the average feature vector for the current item
            item_avg_features[set_folder] = avg_feature_vector
        else:
            print(f"No valid images found for item: {set_folder}")

# Convert item average features dictionary to numpy array for further analysis
item_avg_features_array = np.array(list(item_avg_features.values()))

import json

# Save item_avg_features dictionary to a JSON file
with open('item_avg_features.json', 'w') as f:
    json.dump(item_avg_features, f)

from sklearn.metrics.pairwise import cosine_similarity

# Compute cosine similarity between pairs of feature vectors
cosine_similarities = cosine_similarity(item_avg_features_array)

# Example: Print cosine similarity matrix
print("Cosine Similarity Matrix:")
print(cosine_similarities)

# Save cosine similarity matrix to a CSV file
np.savetxt("cosine_similarities.csv", cosine_similarities, delimiter=",")


