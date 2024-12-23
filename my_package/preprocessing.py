import os
import json

def custom_to_coco(images_folder, annotations_folder):
    """
    Convert custom annotation format to COCO format.

    Args:
        images_folder (str): Path to the folder containing image files.
        annotations_folder (str): Path to the folder containing annotation files.

    Returns:
        dict: COCO-formatted dictionary.
    """
    coco_format = {
        "images": [],
        "annotations": [],
        "categories": [
            {"id": 1, "name": "pedestrian"},
            {"id": 4, "name": "bicycle"},
            {"id": 6, "name": "car"},
            {"id": 7, "name": "motorcycle"},
            {"id": 8, "name": "bus"},
            {"id": 9, "name": "truck"}
        ]
    }
    annotation_id = 1

    # Iterate through all images
    for i, image_file in enumerate(os.listdir(images_folder)):
        if image_file.endswith(('.jpg', '.png', '.jpeg')):
            image_id = i + 1

            # Add image details
            coco_format["images"].append({
                "id": image_id,
                "file_name": image_file,
                "width": 1920,  # Replace with actual dimensions if known
                "height": 1080  # Replace with actual dimensions if known
            })

            # Get corresponding annotation file
            annotation_file = os.path.join(annotations_folder, os.path.splitext(image_file)[0] + '.txt')
            if os.path.exists(annotation_file):
                with open(annotation_file, 'r') as f:
                    for line in f:
                        # Parse the annotation line
                        x_min, y_min, bbox_width, bbox_height, _, category_id, _, iscrowd = map(int, line.strip().split(','))

                        # Add annotation details
                        coco_format["annotations"].append({
                            "id": annotation_id,
                            "image_id": image_id,
                            "category_id": category_id,
                            "bbox": [x_min, y_min, bbox_width, bbox_height],
                            "area": bbox_width * bbox_height,
                            "iscrowd": iscrowd
                        })
                        annotation_id += 1

    return coco_format


def save_coco_format(coco_data, output_path):
    """
    Save the COCO-formatted data to a JSON file.

    Args:
        coco_data (dict): COCO-formatted data.
        output_path (str): Path to save the JSON file.
    """
    with open(output_path, 'w') as f:
        json.dump(coco_data, f, indent=4)
    print(f"COCO annotations saved to: {output_path}")
