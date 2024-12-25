# Script to create a 15% subset of the VisDrone dataset
# This script will copy 15% of images and their corresponding annotations 
# to a separate folder in your Google Drive.

import os
import random
import shutil
from google.colab import drive

# Step 1: Mount Google Drive
# Ensure your Google Drive is mounted to access the dataset
drive.mount('/content/gdrive')

# Step 2: Define paths
# Update these paths based on where your dataset is stored in Google Drive
dataset_path = '/content/gdrive/MyDrive/VisDrone/train/VisDrone2019-DET-train'  # Path to the full dataset
images_folder = os.path.join(dataset_path, 'images')  # Folder containing images
annotations_folder = os.path.join(dataset_path, 'annotations')  # Folder containing annotations

# Define the output paths where the 15% subset will be saved
output_path = '/content/gdrive/MyDrive/VisDrone/15_percent_subset'  # Base folder for the subset
output_images = os.path.join(output_path, 'images')  # Folder for subset images
output_annotations = os.path.join(output_path, 'annotations')  # Folder for subset annotations

# Create output directories if they do not exist
os.makedirs(output_images, exist_ok=True)
os.makedirs(output_annotations, exist_ok=True)

# Step 3: Get all image files
# Collect all image files from the dataset folder
all_images = [f for f in os.listdir(images_folder) if f.endswith(('.jpg', '.png'))]
total_images = len(all_images)

# Step 4: Randomly select 15% of the images
# Calculate the number of images to include in the subset
num_samples = max(1, int(total_images * 0.15))  # Ensure at least 1 file is selected
selected_images = random.sample(all_images, num_samples)

# Display information about the selection
print(f"Total images in dataset: {total_images}")
print(f"Selected {num_samples} images for the 15% subset.")

# Step 5: Copy selected images and annotations
# Iterate through the selected images and copy them to the output folder
for image_file in selected_images:
    # Copy image file to the output folder
    src_image_path = os.path.join(images_folder, image_file)
    dest_image_path = os.path.join(output_images, image_file)
    shutil.copy(src_image_path, dest_image_path)

    # Copy the corresponding annotation file
    annotation_file = os.path.splitext(image_file)[0] + '.txt'  # Assuming annotations match image names
    src_annotation_path = os.path.join(annotations_folder, annotation_file)
    dest_annotation_path = os.path.join(output_annotations, annotation_file)
    
    if os.path.exists(src_annotation_path):
        shutil.copy(src_annotation_path, dest_annotation_path)
    else:
        # Log a warning if the annotation file is missing
        print(f"Warning: Annotation file not found for {image_file}")

# Step 6: Final message
# Inform the user that the subset has been created
print(f"15% subset successfully saved to: {output_path}")
