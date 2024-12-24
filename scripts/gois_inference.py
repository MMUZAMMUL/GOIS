import os
import sys
import argparse

# Add the project root directory to the Python path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from my_package.gois_inference import perform_sliced_inference
from my_package.fix_prediction import fix_predictions_format
from ultralytics import YOLO

def main():
    """
    Main function to perform GOIS inference.
    """
    # Parse command-line arguments
    parser = argparse.ArgumentParser(description="Perform GOIS inference with YOLO model.")
    parser.add_argument("--images_folder", type=str, required=True, help="Path to the images folder.")
    parser.add_argument("--model_path", type=str, required=True, help="Path to the YOLO model file.")
    parser.add_argument("--output_base_path", type=str, required=True, help="Base path to save output files.")
    args = parser.parse_args()

    # Extract paths from arguments
    images_folder = args.images_folder
    model_path = args.model_path
    output_base_path = args.output_base_path

    # Ensure input paths exist
    if not os.path.exists(images_folder):
        raise FileNotFoundError(f"Images folder not found: {images_folder}")
    if not os.path.exists(model_path):
        raise FileNotFoundError(f"Model file not found: {model_path}")
    os.makedirs(output_base_path, exist_ok=True)

    # Automatically generate output paths based on model name
    model_name = os.path.splitext(os.path.basename(model_path))[0]
    predictions_path = os.path.join(output_base_path, f'{model_name}_GOIS.coco.json')
    annotated_images_folder = os.path.join(output_base_path, f'{model_name}_GOIS_ImgOutput')
    os.makedirs(annotated_images_folder, exist_ok=True)

    # Load YOLO model
    print(f"Loading model from: {model_path}")
    model = YOLO(model_path)

    # Perform sliced inference
    print("Performing GOIS inference...")
    perform_sliced_inference(images_folder, model, predictions_path, annotated_images_folder)

    # Fix predictions format
    print("Fixing predictions format...")
    fix_predictions_format(predictions_path)

    # Completion message
    print("GOIS inference completed successfully!")
    print(f"Predictions saved to: {predictions_path}")
    print(f"Annotated images saved to: {annotated_images_folder}")

if __name__ == "__main__":
    main()
