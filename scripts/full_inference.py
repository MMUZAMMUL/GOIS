import os
import sys
import argparse

# Add the project root directory to the Python path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from my_package.inference import perform_inference
from my_package.fix_prediction import fix_predictions_format
from ultralytics import YOLO


def main(args):
    """
    Main function to perform full inference.
    """
    images_folder = args.images_folder
    model_path = args.model_path
    output_base_path = args.output_base_path

    # Extract model name from the model path
    model_name = os.path.splitext(os.path.basename(model_path))[0]
    predictions_path = os.path.join(output_base_path, f"{model_name}_full_inference.json")
    annotated_images_folder = os.path.join(output_base_path, f"{model_name}_full_inference_images_output")

    # Ensure the model file exists
    if not os.path.exists(model_path):
        raise FileNotFoundError(f"Model file not found: {model_path}")

    # Ensure output directories exist
    os.makedirs(output_base_path, exist_ok=True)
    os.makedirs(annotated_images_folder, exist_ok=True)

    # Load YOLO model
    print(f"Loading model from: {model_path}")
    model = YOLO(model_path)

    # Perform inference
    print("Performing inference...")
    perform_inference(images_folder, model, predictions_path, annotated_images_folder)

    # Fix predictions format
    print("Fixing predictions format...")
    fix_predictions_format(predictions_path)

    # Completion message
    print("Full inference completed successfully!")
    print(f"Predictions saved to: {predictions_path}")
    print(f"Annotated images saved to: {annotated_images_folder}")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Perform full inference using YOLO.")
    parser.add_argument("--images_folder", type=str, required=True, help="Path to the folder containing images.")
    parser.add_argument("--model_path", type=str, required=True, help="Path to the YOLO model file.")
    parser.add_argument("--output_base_path", type=str, required=True, help="Base directory for saving predictions and annotated images.")
    args = parser.parse_args()

    main(args)
