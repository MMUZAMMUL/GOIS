import sys
import os

# Add the project root directory to the Python path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from my_package.preprocessing import custom_to_coco, save_coco_format


# Paths
annotations_folder = '/content/gdrive/MyDrive/100%GOIS/TEST-GOIS15%/VisDrone2019-DET-train-15%Subset970-Images/annotations'
images_folder = '/content/gdrive/MyDrive/100%GOIS/TEST-GOIS15%/VisDrone2019-DET-train-15%Subset970-Images/images'
output_coco_path = '/content/GOIS/data/ground_truth/ground_truth_coco.json'

def main():
    """
    Main function to generate COCO-formatted ground truth JSON.
    """
    # Ensure folders exist
    if not os.path.exists(annotations_folder):
        raise FileNotFoundError(f"Annotations folder not found: {annotations_folder}")
    if not os.path.exists(images_folder):
        raise FileNotFoundError(f"Images folder not found: {images_folder}")

    # Convert custom annotations to COCO format
    coco_data = custom_to_coco(images_folder, annotations_folder)

    # Save the COCO annotations to a JSON file
    save_coco_format(coco_data, output_coco_path)

if __name__ == "__main__":
    main()
