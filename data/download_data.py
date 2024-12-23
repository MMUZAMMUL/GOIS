import os
import gdown
import shutil

def download_dataset():
    """
    Downloads a public Google Drive folder containing images and annotations 
    into the local 'data/ground_truth' directory, organizing files into subfolders.
    """
    # Public Google Drive folder link
    folder_url = "https://drive.google.com/drive/folders/12rsLCoPL_7w_oGKurWoDJ8gH1yQ77KJh?usp=drive_link"

    # Destination directory in your project
    base_path = './data/ground_truth/'
    images_path = os.path.join(base_path, 'images/')
    annotations_path = os.path.join(base_path, 'annotations/')
    
    # Ensure the destination directories exist
    os.makedirs(images_path, exist_ok=True)
    os.makedirs(annotations_path, exist_ok=True)
    
    # Convert folder URL to folder ID
    folder_id = folder_url.split('/')[-2]
    
    # Temporary download location
    temp_path = os.path.join(base_path, 'temp/')
    os.makedirs(temp_path, exist_ok=True)
    
    # Command to download entire folder using gdown
    gdown_command = f"gdown --folder https://drive.google.com/drive/folders/{folder_id} -O {temp_path}"
    os.system(gdown_command)
    
    # Move files into respective folders
    for root, dirs, files in os.walk(temp_path):
        for file in files:
            file_path = os.path.join(root, file)
            if file.lower().endswith(('.jpg', '.png', '.jpeg')):  # Image files
                shutil.move(file_path, images_path)
            elif file.lower().endswith(('.json', '.xml', '.txt')):  # Annotation files
                shutil.move(file_path, annotations_path)
    
    # Remove the temporary download folder
    shutil.rmtree(temp_path)
    
    # Display success message
    print(f"Images saved to: {images_path}")
    print(f"Annotations saved to: {annotations_path}")
