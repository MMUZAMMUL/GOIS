import os
from my_package.gois_inference import perform_sliced_inference
from my_package.fix_predictions import fix_predictions_format
from ultralytics import YOLO

# User-configurable paths
model_name = input("Enter the model name (e.g., yolov10n): ")
model_path = f"./models/{model_name}.pt"
images_folder = './data/ground_truth/images'
output_base_path = f'./data/gois_results/{model_name}/'
predictions_path = os.path.join(output_base_path, f'{model_name}_GOIS_predictions.json')
annotated_images_folder = os.path.join(output_base_path, 'annotated_images')

def main():
    # Ensure paths exist
    os.makedirs(output_base_path, exist_ok=True)
    os.makedirs(annotated_images_folder, exist_ok=True)

    # Load model
    if not os.path.exists(model_path):
        raise FileNotFoundError(f"Model not found: {model_path}")
    model = YOLO(model_path)

    # Perform sliced inference
    perform_sliced_inference(images_folder, model, predictions_path, annotated_images_folder)

    # Fix predictions format
    fix_predictions_format(predictions_path)

if __name__ == "__main__":
    main()
