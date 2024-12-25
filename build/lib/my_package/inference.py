import os
import json
from PIL import Image, ImageDraw
from ultralytics import YOLO

# Mapping YOLO classes to COCO categories
yolo_to_coco_category = {
    0: {"id": 1, "name": "pedestrian"},
    1: {"id": 4, "name": "bicycle"},
    2: {"id": 6, "name": "car"},
    3: {"id": 7, "name": "motorcycle"},
    4: {"id": 8, "name": "bus"},
    5: {"id": 9, "name": "truck"}
}

def draw_detections(image, results, class_names):
    """
    Draw detections on the image.
    """
    draw = ImageDraw.Draw(image)
    for box in results.boxes:
        x_min, y_min, x_max, y_max = box.xyxy[0].tolist()
        class_id = int(box.cls[0].item())
        confidence = float(box.conf[0].item())
        label = f"{class_names[class_id]} {confidence:.2f}"
        draw.rectangle([x_min, y_min, x_max, y_max], outline="red", width=2)
        draw.text((x_min, y_min), label, fill="yellow")
    return image

def perform_inference(images_folder, model, predictions_path, annotated_images_folder, conf_threshold=0.25):
    """
    Perform inference and save predictions and annotated images.
    """
    coco_format = {
        "images": [],
        "annotations": [],
        "categories": list(yolo_to_coco_category.values())
    }
    annotation_id = 1
    os.makedirs(annotated_images_folder, exist_ok=True)

    for i, image_file in enumerate(os.listdir(images_folder)):
        if image_file.endswith(('.jpg', '.png', '.jpeg')):
            image_path = os.path.join(images_folder, image_file)
            img = Image.open(image_path).convert("RGB")
            width, height = img.size
            image_id = i + 1

            # Add image details to COCO format
            coco_format["images"].append({
                "id": image_id,
                "file_name": image_file,
                "width": width,
                "height": height
            })

            # Perform prediction
            results = model.predict(image_path, conf=conf_threshold)[0]

            # Save annotated image
            annotated_img = draw_detections(img.copy(), results, model.names)
            annotated_img.save(os.path.join(annotated_images_folder, image_file))

            # Add annotations to COCO format
            for box in results.boxes:
                x_min, y_min, x_max, y_max = box.xyxy[0].tolist()
                w, h = x_max - x_min, y_max - y_min
                yolo_class_id = int(box.cls[0].item())
                confidence = float(box.conf[0].item())

                if yolo_class_id in yolo_to_coco_category:
                    category = yolo_to_coco_category[yolo_class_id]
                    coco_format["annotations"].append({
                        "id": annotation_id,
                        "image_id": image_id,
                        "category_id": category["id"],
                        "bbox": [x_min, y_min, w, h],
                        "area": w * h,
                        "iscrowd": 0,
                        "score": confidence
                    })
                    annotation_id += 1

    # Save predictions in COCO format
    with open(predictions_path, 'w') as f:
        json.dump(coco_format, f, indent=4)
    print(f"Predictions saved to: {predictions_path}")
    print(f"Annotated images saved to: {annotated_images_folder}")
