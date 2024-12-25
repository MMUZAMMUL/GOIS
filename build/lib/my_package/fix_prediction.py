import json

def fix_predictions_format(predictions_path):
    """Ensure the predictions file is a flat array of objects."""
    with open(predictions_path, 'r') as f:
        data = json.load(f)

    # If the predictions are wrapped in a COCO-style object
    if isinstance(data, dict) and "annotations" in data:
        fixed_data = data["annotations"]
        print("Extracting annotations from COCO-style object...")
    else:
        fixed_data = data
        print("Predictions file already in the correct format.")

    # Save the fixed predictions file
    with open(predictions_path, 'w') as f:
        json.dump(fixed_data, f, indent=4)

    print(f"Predictions file fixed and saved to: {predictions_path}")
