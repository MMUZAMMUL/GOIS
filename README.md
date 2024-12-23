# **GOIS Project Instructions**

Welcome to the **GOIS** project! This guide will walk you through the setup and usage of the project, including running full inference, GOIS inference, and evaluation of results.

---

## **Project Structure**
The project is organized as follows:

```
GOIS/
├── my_package/                # Core logic for inference, evaluation, and prediction fixes
│   ├── inference.py
│   ├── gois_inference.py
│   ├── fix_predictions.py
│
├── models/                    # Model management
│   ├── download_models.py     # Script to download models
│
├── data/                      # Data and results
│   ├── ground_truth/          # Ground truth JSON and input images
│   ├── full_inference/        # Full inference results
│   ├── gois_results/          # GOIS results
│
├── scripts/                   # Scripts for running tasks
│   ├── full_inference.py      # Perform full inference
│   ├── gois_inference.py      # Perform GOIS inference
│   ├── evaluate_full_inference.py  # Evaluate full inference results
│   ├── evaluate_gois.py       # Evaluate GOIS results
│
├── setup.py                   # Installable package setup
├── requirements.txt           # Python dependencies
└── instructions.md            # User guide (this file)
```

---

## **Setup**

### 1. **Clone the Repository**
Clone the repository to your local system:
```bash
git clone https://github.com/yourusername/GOIS.git
cd GOIS
```

### 2. **Install Dependencies**
Install the required Python dependencies:
```bash
pip install -r requirements.txt
```

### 3. **Download Models**
Run the script to download all required models:
```bash
python models/download_models.py
```
This will save the models in the `./models/` directory.

### 4. **Prepare Dataset**
Place your dataset (images and annotations) in the `./data/ground_truth/` directory:
- **Images:** Place input images in `./data/ground_truth/images/`.
- **Annotations:** Ensure the ground truth COCO JSON file is saved as `./data/ground_truth/ground_truth_coco.json`.

---

## **Running Inference**

### **1. Full Inference**
To perform full inference using a specific model:
```bash
python scripts/full_inference.py
```
- The script will list all available models in `./models/`.
- Select a model by entering its number.
- Outputs:
  - **Predictions JSON:** Saved in `./data/full_inference/{model_name}/{model_name}_predictions.json`.
  - **Annotated Images:** Saved in `./data/full_inference/{model_name}/annotated_images/`.

---

### **2. GOIS Inference**
To perform GOIS inference:
```bash
python scripts/gois_inference.py
```
- The script will prompt you to select a model.
- Outputs:
  - **Predictions JSON:** Saved in `./data/gois_results/{model_name}/{model_name}_GOIS_predictions.json`.
  - **Annotated Images:** Saved in `./data/gois_results/{model_name}/annotated_images/`.

---

## **Evaluation**

### **1. Evaluate Full Inference**
To evaluate the full inference results:
```bash
python scripts/evaluate_full_inference.py
```
- The script will prompt you to select the model whose results you want to evaluate.
- Outputs:
  - Displays Average Precision (AP) and Average Recall (AR) metrics.

---

### **2. Evaluate GOIS**
To evaluate GOIS results:
```bash
python scripts/evaluate_gois.py
```
- The script will prompt you to select the model whose results you want to evaluate.
- Outputs:
  - Displays Average Precision (AP) and Average Recall (AR) metrics.

---

## **Customization**

### **Modify Dataset Paths**
You can update the dataset paths in the scripts if your data is stored elsewhere. For example:
- In `scripts/full_inference.py` and `scripts/gois_inference.py`, modify `images_folder` and `output_base_path` accordingly.

### **Add New Models**
If you want to add additional models:
1. Add the model details to `models/download_models.py`.
2. Run the script to download the new model.

---

## **Troubleshooting**

1. **Missing Models**
   - Ensure models are downloaded correctly in the `./models/` directory by running:
     ```bash
     python models/download_models.py
     ```

2. **File Not Found Errors**
   - Verify that the ground truth JSON file and input images are correctly placed in `./data/ground_truth/`.

3. **Evaluation Metrics Not Displayed**
   - Ensure predictions JSON files are correctly generated during inference.

---

## **Contact**
For any issues or feature requests, please contact:
- **Email:** your.email@example.com
- **GitHub Issues:** [https://github.com/yourusername/GOIS/issues](https://github.com/yourusername/GOIS/issues)

---

