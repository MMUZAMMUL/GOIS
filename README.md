```markdown
# GOIS: Guided Object Inference Slicing Framework

## Overview

GOIS is a robust framework designed for **inference slicing**, providing enhanced evaluation metrics and comparisons for object detection models. The project features functionality for **data preparation**, **model evaluation**, and **comparative analysis**. It supports **full inference** and **sliced inference (GOIS)** to benchmark performance improvements.

---

## Key Features

- **Full Inference Predictions (FI-Det):** Evaluate models on complete images.
- **Guided Object Inference Slicing (GOIS-Det):** Perform inference using a slicing approach for improved accuracy.
- **Ground Truth Generation:** Prepare COCO-style ground truth annotations for evaluation.
- **Evaluation Metrics:** Analyze performance with COCO metrics, including precision, recall, and IoU.
- **Upscaled Results:** Visualize upscaled metrics for enhanced understanding of improvements.

---

## Installation

### Clone Repository
```bash
git clone https://github.com/MMUZAMMUL/GOIS.git
cd GOIS
```

### Install Requirements
Install the necessary dependencies:
```bash
pip install -r requirements.txt
```


## Usage Instructions

### 1. **Download Data**
Follow instructions in `data/dataset.md` to prepare the dataset or directly download the 15% subset:
[15% Subset Download Link](https://drive.google.com/drive/folders/12rsLCoPL_7w_oGKurWoDJ8gH1yQ77KJh?usp=drive_link)

### 2. **Download Models**
Run the script to download required models:
```bash
python Models/download_models.py
```

### 3. **Generate Ground Truth**
Generate COCO-format ground truth annotations:
```bash
python scripts/generate_ground_truth.py \
    --annotations_folder <path_to_annotations> \
    --images_folder <path_to_images> \
    --output_coco_path ./data/ground_truth/ground_truth_coco.json
```

### 4. **Run Full Inference**
Perform full image inference:
```bash
python scripts/full_inference.py \
    --images_folder <path_to_images> \
    --model_path ./Models/yolov8s-worldv2.pt \
    --model_type YOLOWorld \
    --output_base_path ./data/full_inference/
```

### 5. **Run GOIS Inference**
Perform sliced inference using GOIS:
```bash
python scripts/gois_inference.py \
    --images_folder <path_to_images> \
    --model_path ./Models/yolov8s-worldv2.pt \
    --model_type YOLOWorld \
    --output_base_path ./data/gois_results/
```

### 6. **Evaluate Results**
#### Evaluate Full Inference:
```bash
python scripts/evaluate_prediction.py \
    --ground_truth_path ./data/ground_truth/ground_truth_coco.json \
    --predictions_path ./data/full_inference/full_inference.json \
    --iou_type bbox
```

#### Evaluate GOIS:
```bash
python scripts/evaluate_prediction.py \
    --ground_truth_path ./data/ground_truth/ground_truth_coco.json \
    --predictions_path ./data/gois_results/gois_inference.json \
    --iou_type bbox
```

### 7. **Compare Results**
Compare evaluation metrics and calculate percentage improvements:
```bash
python scripts/calculate_results.py \
    --ground_truth_path ./data/ground_truth/ground_truth_coco.json \
    --full_inference_path ./data/full_inference/full_inference.json \
    --gois_inference_path ./data/gois_results/gois_inference.json
```

### 8. **Upscale Metrics**
Visualize results with upscaled metrics:
```bash
python scripts/evaluate_upscaling.py \
    --ground_truth_path ./data/ground_truth/ground_truth_coco.json \
    --full_inference_path ./data/full_inference/full_inference.json \
    --gois_inference_path ./data/gois_results/gois_inference.json
```

---

## Contributing
Read the [Contributing Guidelines](CONTRIBUTING.md) for more details.

## License
This project is licensed under the MIT License. See [LICENSE](LICENSE) for details.

## Security
For reporting vulnerabilities, refer to [SECURITY.md](SECURITY.md).

---

## Contact
Author: **Muhammad Muzammul**  
Email: [munagreat123@gmail.com](mailto:munagreat123@gmail.com)  


```
