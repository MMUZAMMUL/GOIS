### License

[**MIT License**](LICENSE) - All rights reserved to the author. This project may be used for study and educational purposes, but **redistribution, redevelopment, or use of the code for personal or commercial purposes is strictly prohibited without the author's written consent.**

## 🚀 GOIS: Enhancing Tiny Object Detection Without Fine-Tuning
**Guided-Object Inference Slicing (GOIS) with YOLO & RT-DETR**  
🔬 Research by: Muhammad Muzammul, Xuewei Li, Xi Li  
📄 Under Review in *Neurocomputing*  

### 📌 Citation
```bash
@ MUHAMMAD MUZAMMUL, Xuewei LI, Xi Li et al.  
Enhancing Tiny Object Detection without Fine Tuning:  
Dynamic Adaptive Guided Object Inference Slicing Framework  
with Latest YOLO Models and RT-DETR Transformer,  
07 January 2025, PREPRINT (Version 1)  
[https://doi.org/10.21203/rs.3.rs-5780163/v1]
```
### 📥 Quick Start
| **Step** | **Command** |
|----------|------------|
| **1️⃣ Clone Repo** | `git clone https://github.com/MMUZAMMUL/GOIS.git && cd GOIS` |
| **2️⃣ Download Data** | Follow [Dataset Instructions](data/dataset.md) or [Download 15% Dataset](https://drive.google.com/drive/folders/12rsLCoPL_7w_oGKurWoDJ8gH1yQ77KJh?usp=drive_link) |
| **3️⃣ Download Models** | `cd Models && python download_models.py` |
| **4️⃣ Generate Ground Truth** | `python scripts/generate_ground_truth.py --annotations_folder "<annotations_path>" --images_folder "<images_path>" --output_coco_path "./data/ground_truth/ground_truth_coco.json"` |
| **5️⃣ Full Inference (FI-Det)** | `python scripts/full_inference.py --images_folder "<path>" --model_path "Models/yolo11n.pt" --model_type "YOLO" --output_base_path "./data/FI_Predictions"` |
| **6️⃣ GOIS Inference** | `python scripts/gois_inference.py --images_folder "<path>" --model_path "Models/yolo11n.pt" --model_type "YOLO" --output_base_path "./data/gois_Predictions"` |
| **7️⃣ Evaluate FI-Det** | `python scripts/evaluate_prediction.py --ground_truth_path "./data/ground_truth/ground_truth_coco.json" --predictions_path "./data/FI_Predictions/full_inference.json" --iou_type bbox` |
| **8️⃣ Evaluate GOIS-Det** | `python scripts/evaluate_prediction.py --ground_truth_path "./data/ground_truth/ground_truth_coco.json" --predictions_path "./data/gois_Predictions/gois_inference.json" --iou_type bbox` |
| **9️⃣ Compare Results** | `python scripts/calculate_results.py --ground_truth_path "./data/ground_truth/ground_truth_coco.json" --full_inference_path "./data/FI_Predictions/full_inference.json" --gois_inference_path "./data/gois_Predictions/gois_inference.json"` |
| **🔟 Upscale Metrics** | `python scripts/evaluate_upscaling.py --ground_truth_path "./data/ground_truth/ground_truth_coco.json" --full_inference_path "./data/FI_Predictions/full_inference.json" --gois_inference_path "./data/gois_Predictions/gois_inference.json"` |

---

### 📊 Benchmarks & Live Demo  
📂 [GOIS Benchmarks Repository](https://github.com/MMUZAMMUL/TinyObjectDetection-GOIS)  
🎥 [Watch Live Demo (YouTube)](https://youtu.be/T5t5eb_w0S4) | 🎥 [Watch Live Demo (Bilibili)](https://www.bilibili.com/video/BV1jJCFYGEY4/?share_source=copy_web)  

🔑 **MIT License** - Study & Educational Use Only  
📧 **Contact**: *[Author Email](mailto:muzamal@zju.edu.cn)*  

## 🚀 GOIS Live Deployed Applications on Hugging Face ✅ <img src="https://huggingface.co/front/assets/huggingface_logo-noborder.svg" alt="Hugging Face" width="32">
Experience **Guided Object Inference Slicing (GOIS)** across **images, videos, and live cameras** with configurable parameters. Evaluate **real-time small object detection** and compare against **full-image inference (FI-Det).**  

📂 **Compatible Datasets:** VisDrone, UAV Surveillance (100-150ft), Pedestrian & Tiny Object Detection, Geo-Sciences  
🖥️ **Applied Models:** YOLO11, YOLOv10, YOLOv9, YOLOv8, YOLOv6, YOLOv5, RT-DETR-L, YOLOv8s-Worldv2  

GOIS incorporates a **two-stage hierarchical slicing** strategy, dynamically adjusting **coarse-to-fine slicing** and overlap rates to **optimize tiny object detection** while reducing false positives. These live applications allow users to test GOIS against full-image inference, analyze **occlusion handling**, **boundary artifacts**, and **false positive reductions**, while adjusting key parameters.

| **Test Function** | **Description** | 🔗 **Test Link** |
|------------------|----------------|------------------------------|
| **GOIS vs. Full-Image Detection** | Evaluates **dynamic slicing vs. full-image inference (FI-Det)** across images, identifying missed objects and reducing false positives. | <img src="https://huggingface.co/front/assets/huggingface_logo-noborder.svg" alt="Hugging Face" width="20"> [GOIS Live Image Processing](https://huggingface.co/spaces/MMUZAMMUL123/GOIS_Live_ImageProcessing) |
| **Video Detection (Single Stage)** | Tests **frame-wise GOIS slicing** to improve small object detection, mitigating occlusion issues. | <img src="https://huggingface.co/front/assets/huggingface_logo-noborder.svg" alt="Hugging Face" width="20"> [GOIS Video Inference (Single Stage)](https://huggingface.co/spaces/MMUZAMMUL123/GOIS_Video_Inference_Single_Stage) |
| **Advanced Video Detection (Two Stage)** | Uses **coarse-to-fine GOIS slicing** based on object density to dynamically adjust slicing strategies and eliminate boundary artifacts. | <img src="https://huggingface.co/front/assets/huggingface_logo-noborder.svg" alt="Hugging Face" width="20"> [GOIS Video Inference (Two Stage)](https://huggingface.co/spaces/MMUZAMMUL123/GOIS_Video_Inference_Two_Stage) |
| **Live Camera Detection (FI vs. GOIS)** | Compares **full-frame inference vs. GOIS slicing** in real-time, highlighting differences in object localization and accuracy. | <img src="https://huggingface.co/front/assets/huggingface_logo-noborder.svg" alt="Hugging Face" width="20"> [GOIS Live Camera Test](https://huggingface.co/spaces/MMUZAMMUL123/GOIS_Live_Camera_Test_Single_Stage) |
| **Live Camera Advanced Detection** | Demonstrates **adaptive slicing based on object density**, improving small object retrieval while maintaining efficiency. | <img src="https://huggingface.co/front/assets/huggingface_logo-noborder.svg" alt="Hugging Face" width="20"> [GOIS Live Camera Advanced](https://huggingface.co/spaces/MMUZAMMUL123/GOIS_LiveCamera_AdvanceLevel) |

### 🔹 How to Use  
1️⃣ **Click a Test Link** → 2️⃣ **Upload Image/Video** → 3️⃣ **Adjust Parameters (Slice Size, Overlap, NMS)** → 4️⃣ **Compare FI vs. GOIS Results** → 5️⃣ **Analyze Performance in Real-Time**  

---

## 📌 Google Colab Live Test Links for GOIS ![Google Colab](https://www.tensorflow.org/images/colab_logo_32px.png)
To validate ✅ the **Guided Object Inference Slicing (GOIS)** framework, the following **Google Colab notebooks** provide real-time inference and analysis. These tests allow users to compare **GOIS vs. Full-Image Detection (FI-Det)** across different **datasets and models**.

📂 **Compatible Datasets:** VisDrone, UAV Surveillance (100-150ft), Pedestrian & Tiny Object Detection, Geo-Sciences  
🖥️ **Applied Models:** YOLO11, YOLOv10, YOLOv9, YOLOv8, YOLOv6, YOLOv5, RT-DETR-L, YOLOv8s-Worldv2  

GOIS differs from traditional slicing methods (SAHI, ASAHI) by **dynamically adjusting** slicing parameters **based on object density** rather than static window sizes. These notebooks enable **comparative testing**, allowing users to **experiment with slicing sizes, overlap rates, and NMS thresholds**, addressing key performance trade-offs.

| **Test Function** | **Description** | **Colab Link** |
|------------------|----------------|----------------|
| **GOIS vs. SAHI/ASAHI (Proposed Method)** | Compares **GOIS dynamic slicing** vs. **static slicing (SAHI, ASAHI-like),** analyzing boundary artifacts and false positive rates. | ![Google Colab](https://www.tensorflow.org/images/colab_logo_32px.png)[📌 GOIS vs. SAHI/ASAHI](https://colab.research.google.com/drive/1QTgSVe4_PYqPC5uBEcjA5bTcvDNc_Wbc?usp=sharing) |
| **GOIS - Single Image Inference** | Runs **GOIS on a single image**, adjusting slicing parameters and overlap rates. | ![Google Colab](https://www.tensorflow.org/images/colab_logo_32px.png)[📌 GOIS Single Image Test](https://colab.research.google.com/drive/1TPQKq_17Wg1NiXD5Mah0a_6bkOt4-t9b?usp=sharing) |
| **GOIS vs. FI-Det (Single Image)** | Side-by-side **visual comparison of GOIS vs. FI-Det**, addressing occlusion and small object visibility. | ![Google Colab](https://www.tensorflow.org/images/colab_logo_32px.png)[📌 GOIS vs. FI-Det (Single Image)](https://colab.research.google.com/drive/1ijdnfFA3tQ9PSJDMqPXCka3KRWhrblIh?usp=sharing) |
| **GOIS vs. FI-Det (Multiple Images)** | Processes **multiple images** to compare detection consistency across datasets. | ![Google Colab](https://www.tensorflow.org/images/colab_logo_32px.png)[📌 GOIS vs. FI-Det (Multiple Images)](https://colab.research.google.com/drive/1kwGJDVoSZ4NOTQsxdsYreYz_twRhoX0S?usp=sharing) |
| **Detection Count & Metrics Comparison** | Evaluates **object count, area coverage, and false positive reduction rates.** | ![Google Colab](https://www.tensorflow.org/images/colab_logo_32px.png)[📌 GOIS vs. FI-Det (Metrics Test)](https://colab.research.google.com/drive/1X1t-L3tW1bIfVT6PtzKKFqU52PEMqivI?usp=sharing) |
| **Slice Size Optimization - Speed Test** | Tests how **different slicing sizes and overlap settings impact speed vs. accuracy.** | ![Google Colab](https://www.tensorflow.org/images/colab_logo_32px.png)[📌 GOIS Optimized Speed Test](https://colab.research.google.com/drive/1LYFnEjIinIW_4HHyVYVtg7aZVikWfnea?usp=sharing) |
| **GOIS - 81 Parameter Combinations Test** | Tests **81 slicing, overlap, and NMS variations** for optimal performance. | ![Google Colab](https://www.tensorflow.org/images/colab_logo_32px.png)[📌 GOIS 81 Combinations Test](https://colab.research.google.com/drive/18H8HtFYDc0On6KMAIkfxW5xWW1hsUeFc?usp=sharing) |

### 🛠 **How to Use**
1️⃣ **Open any Colab link** → 2️⃣ **Run the notebook** → 3️⃣ **Upload images or use datasets** → 4️⃣ **Adjust GOIS parameters (slice size, overlap, NMS)** → 5️⃣ **Compare FI vs. GOIS results**  

---

### **Cite This Work**
If you use GOIS in your research, please consider citing our paper:








