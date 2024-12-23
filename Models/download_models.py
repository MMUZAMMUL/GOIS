import os
from ultralytics import YOLO, RTDETR, YOLOWorld

# List of models with names and associated handlers
models = {
    "yolo11n": ("YOLO", "yolo11n.pt"),
    "yolov10n": ("YOLO", "yolov10n.pt"),
    "yolov9c": ("YOLO", "yolov9c.pt"),
    "yolov8n": ("YOLO", "yolov8n.pt"),
    "yolov5nu": ("YOLO", "yolov5nu.pt"),
    "rtdetr-l": ("RTDETR", "rtdetr-l.pt"),
    "yolov8s-world": ("YOLOWorld", "yolov8s-worldv2.pt"),
}

def download_yolo_models(models_folder='./models'):
    """
    Downloads YOLO, RTDETR, and YOLOWorld models using Ultralytics API.
    """
    os.makedirs(models_folder, exist_ok=True)

    for model_name, (model_type, model_file) in models.items():
        model_path = os.path.join(models_folder, model_file)

        if os.path.exists(model_path):
            print(f"{model_name} already exists, skipping download.")
            continue

        try:
            print(f"Downloading {model_name} ({model_type})...")
            if model_type == "YOLO":
                model = YOLO(model_file)
            elif model_type == "RTDETR":
                model = RTDETR(model_file)
            elif model_type == "YOLOWorld":
                model = YOLOWorld(model_file)
            else:
                print(f"Unsupported model type for {model_name}. Skipping...")
                continue

            # Export the model and save it in the models folder
            model.export(format="torchscript", imgsz=640, dynamic=True, device="cpu", save_dir=models_folder)

        except Exception as e:
            print(f"Error downloading {model_name}: {e}")

    print("All available models are ready.")

if __name__ == "__main__":
    download_yolo_models()
