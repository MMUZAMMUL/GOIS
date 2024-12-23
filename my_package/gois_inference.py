import os
import json
from PIL import Image, ImageDraw
from ultralytics import YOLO

# YOLO to COCO category mapping for VisDrone dataset
yolo_to_coco_category = {
    0: {"id": 1, "name": "pedestrian"},
    1: {"id": 4, "name": "bicycle"},
    2: {"id": 6, "name": "car"},
    3: {"id": 7, "name": "motorcycle"},
    4: {"id": 8, "name": "bus"},
    5: {"id": 9, "name": "truck"}
}

def draw_detections_on_image(image, predictions):
    """Draw predictions on the original image."""
    draw = ImageDraw.Draw(image)
    for pred in predictions:
        x_min, y_min, w, h = pred["bbox"]
        x_max, y_max = x_min + w, y_min + h
        category_id = pred["category_id"]
        score = pred["score"]
        class_name = next((cat["name"] for cat in yolo_to_coco_category.values() if cat["id"] == category_id), "unknown")

        # Draw bounding box
        draw.rectangle([x_min, y_min, x_max, y_max], outline="red", width=2)

        # Draw label
        label = f"{class_name} {score:.2f}"
        draw.text((x_min, y_min), label, fill="yellow")

    return image

def perform_sliced_inference(images_folder, model, predictions_path, annotated_images_folder, slice_size=640, overlap=0.2):
    """Perform YOLO inference on sliced images and save predictions in COCO format and annotated images."""
    coco_format = {
        "images": [],
        "annotations": [],
        "categories": list(yolo_to_coco_category.values())
    }
    annotation_id = 1

    for i, image_file in enumerate(os.listdir(images_folder)):
        if image_file.endswith(('.jpg', '.png', '.jpeg')):
            image_path = os.path.join(images_folder, image_file)
            img = Image.open(image_path).convert("RGB")
            width, height = img.size

            coco_format["images"].append({
                "id": i + 1,
                "file_name": image_file,
                "width": width,
                "height": height
            })

            # Generate slices
            step = int(slice_size * (1 - overlap))
            image_predictions = []
            for y in range(0, height, step):
                for x in range(0, width, step):
                    x_end = min(x + slice_size, width)
                    y_end = min(y + slice_size, height)

                    # Crop slice
                    slice_box = (x, y, x_end, y_end)
                    img_slice = img.crop(slice_box)

                    # Run inference on slice
                    results = model.predict(img_slice, conf=0.25)[0]

                    # Map slice results back to original image coordinates
                    for box in results.boxes:
                        x_min, y_min, x_max, y_max = box.xyxy[0].tolist()
                        w, h = x_max - x_min, y_max - y_min
                        yolo_class_id = int(box.cls[0].item())
                        confidence = float(box.conf[0].item())

                        # Map YOLO class ID to COCO category
                        if yolo_class_id in yolo_to_coco_category:
                            category = yolo_to_coco_category[yolo_class_id]
                            bbox = [x_min + x, y_min + y, w, h]  # Add slice offsets
                            annotation = {
                                "id": annotation_id,
                                "image_id": i + 1,
                                "category_id": category["id"],
                                "bbox": bbox,
                                "area": w * h,
                                "iscrowd": 0,
                                "score": confidence
                            }
                            coco_format["annotations"].append(annotation)
                            image_predictions.append(annotation)
                            annotation_id += 1

            # Save annotated image
            annotated_image = draw_detections_on_image(img.copy(), image_predictions)
            annotated_image.save(os.path.join(annotated_images_folder, image_file))

    # Save predictions to file
    with open(predictions_path, 'w') as f:
        json.dump(coco_format, f, indent=4)

    print(f"Sliced predictions saved to: {predictions_path}")
    print(f"Annotated images saved to: {annotated_images_folder}")
