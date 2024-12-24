import os
from my_package.inference import perform_inference
from my_package.inference import perform_inference
from my_package.fix_predictions import fix_predictions_format
from ultralytics import YOLO
from models.download_models import download_models

# Paths and configurations
images_folder = './data/ground_truth/images'
output_base_path = './data/full_inference/'
models_folder = './models/'

def main():
    # Ensure models are downloaded
    download_models(models_folder)

    # List available models
    available_models = [file.replace('.pt', '') for file in os.listdir(models_folder) if file.endswith('.pt')]

    if not available_models:
        print("No models available. Please check the models directory.")
        return

    # Display models for user selection
    print("Available models:")
    for idx, model_name in enumerate(available_models, 1):
        print(f"{idx}. {model_name}")

    # User selects a model
    selected_idx = int(input("Select a model by entering its number: "))
    if selected_idx < 1 or selected_idx > len(available_models):
        print("Invalid selection. Exiting.")
        return

    selected_model = available_models[selected_idx - 1]
    print(f"Selected model: {selected_model}")

    # Configure paths
    model_path = os.path.join(models_folder, f"{selected_model}.pt")
    model_output_path = os.path.join(output_base_path, selected_model)
    predictions_path = os.path.join(model_output_path, f"{selected_model}_predictions.json")
    annotated_images_folder = os.path.join(model_output_path, "annotated_images")

    # Create output directories
    os.makedirs(model_output_path, exist_ok=True)
    os.makedirs(annotated_images_folder, exist_ok=True)

    # Perform inference
    print(f"Running inference with model: {selected_model}...")
    model = YOLO(model_path)
    perform_inference(images_folder, model, predictions_path, annotated_images_folder)

    # Fix predictions format
    print(f"Fixing predictions format for: {predictions_path}")
    fix_predictions_format(predictions_path)

    # Completion message
    print(f"Inference completed successfully!")
    print(f"Predictions saved to: {predictions_path}")
    print(f"Annotated images saved to: {annotated_images_folder}")

if __name__ == "__main__":
    main()
