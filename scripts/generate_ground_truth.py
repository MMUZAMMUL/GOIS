import os
from my_package.preprocessing import custom_to_coco, save_coco_format

# Paths
annotations_folder = './data/ground_truth/annotations'
images_folder = './data/ground_truth/images'
output_coco_path = './data/ground_truth/ground_truth_coco.json'

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
