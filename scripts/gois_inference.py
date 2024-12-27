import os
import sys
import argparse
from ultralytics import YOLO, YOLOWorld, RTDETR
from my_package.gois1_inference import perform_sliced_inference
from my_package.fix_prediction import fix_predictions_format

# Add the project root directory to the Python path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

def load_model(model_path, model_type):
    """
    Load the appropriate model based on the model type.
    """
    if model_type == "YOLO":
        return YOLO(model_path)
    elif model_type == "YOLOWorld":
        return YOLOWorld(model_path)
    elif model_type == "RTDETR":
        return RTDETR(model_path)
    else:
        raise ValueError(f"Unsupported model type: {model_type}")

def main():
    """
    Main function to perform GOIS inference.
    """
    # Parse command-line arguments
    parser = argparse.ArgumentParser(description="Perform GOIS inference using YOLO or YOLOWorld or RTDETR.")
    parser.add_argument("--images_folder", type=str, required=True, help="Path to the images folder.")
    parser.add_argument("--model_path", type=str, required=True, help="Path to the model file.")
    parser.add_argument("--model_type", type=str, required=True, choices=["YOLO", "YOLOWorld", "RTDETR"], help="Type of model (e.g., YOLO, YOLOWorld,RTDETR).")
    parser.add_argument("--output_base_path", type=str, required=True, help="Base path to save output files.")
    args = parser.parse_args()

    # Extract paths from arguments
    images_folder = args.images_folder
    model_path = args.model_path
    model_type = args.model_type
    output_base_path = args.output_base_path

    # Generate output paths
    model_name = os.path.splitext(os.path.basename(model_path))[0]
    predictions_path = os.path.join(output_base_path, f"{model_name}_GOIS.coco.json")
    annotated_images_folder = os.path.join(output_base_path, f"{model_name}_GOIS_ImgOutput")

    # Ensure paths exist
    if not os.path.exists(model_path):
        raise FileNotFoundError(f"Model file not found: {model_path}")
    os.makedirs(output_base_path, exist_ok=True)
    os.makedirs(annotated_images_folder, exist_ok=True)

    # Load the model
    print(f"Loading {model_type} model from: {model_path}")
    model = load_model(model_path, model_type)

    # Perform GOIS inference
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
