[MIT License](LICENSE) -All rights reserved to the author. This project may be used for study and educational purposes, but **redistribution, redevelopment, or use of the code for personal or commercial purposes is strictly prohibited without the author's written consent.

🎥 [Watch Live Demo (YouTube)](https://youtu.be/ukWUfXBFZ5I) | 🎥 [Watch Live Demo (Bilibili)](https://www.bilibili.com/video/BV1sLKjebEQK/?vd_source=f4edde9395a4d640571ae4487880e1ce)  
## 🚀 Enhancing Tiny Object Detection Using Guided Object Inference Slicing (GOIS): An Efficient Dynamic Adaptive Framework for Fine-Tuned and Non-Fine-Tuned Deep Learning Models
**Guided-Object Inference Slicing (GOIS) Innovatory Framework with Several Open source code Deployed on Google Colab/Gradio Live/Huggingface**  
🔬 Research by: Muhammad Muzammul, Xuewei Li, Xi Li  
📄 Published in *Neurocomputing* Journal-> https://doi.org/10.1016/j.neucom.2025.130327
**Contact**: muzamal@zju.edu.cn 

### 📌 Citation
```bash
@article{MUZAMMUL2025130327,
title = {Enhancing Tiny Object Detection Using Guided Object Inference Slicing (GOIS): An efficient dynamic adaptive framework for fine-tuned and non-fine-tuned deep learning models},
journal = {Neurocomputing},
volume = {640},
pages = {130327},
year = {2025},
issn = {0925-2312},
doi = {https://doi.org/10.1016/j.neucom.2025.130327},
url = {https://www.sciencedirect.com/science/article/pii/S0925231225009993},
author = {Muhammad Muzammul and Xuewei Li and Xi Li},
keywords = {Tiny Object Detection, Guided Object Inference Slicing (GOIS), Adaptive slicing-based detection, UAV-based real-time inference, High-resolution remote sensing imagery, Computationally efficient object detection, Deep learning for small-object recognition, Non-maximum suppression optimization, Transformer-based object detection},
abstract = {Tiny Object Detection (TOD) in UAV and standard imaging remains challenging due to extreme scale variations, occlusion, and cluttered backgrounds. This paper presents the Dynamic Adaptive Guided Object Inference Slicing (GOIS) framework, a two-stage adaptive slicing strategy that dynamically reallocates computational resources to Regions of Interest (ROIs), enhancing detection precision and recall. Unlike static and semi-adaptive slicing methods like SAHI and ASAHI, evaluated with models such as FNet, TOOD, and TPH-YOLO, GOIS leverages VisDrone and xView datasets to optimize hierarchical slicing and dynamic Non-Maximum Suppression (NMS), improving tiny object detection while reducing boundary artifacts and false positives. Comprehensive experiments using MS COCO-pretrained Ultralytics models under fine-tuning and non-fine-tuning conditions validate its effectiveness. Evaluations across YOLO11, RT-DETR-L, YOLOv8s-WorldV2, YOLOv10, YOLOv8, and YOLOv5 demonstrate that GOIS consistently outperforms Full-Image Inference (FI-Det), achieving up to 3-4× improvements in small-object recall. On the VisDrone2019 dataset, GOIS-Det improved mAP@0.50:0.95 from 0.12 (FI-Det) to 0.33 (+175%) on YOLO11 and from 0.18 to 0.38 (+111.10%) on YOLOv5n. Fine-tuning further enhanced AP-Small by 278.66% and AR-Small by 279.22%, confirming GOIS’s adaptability across diverse deployment scenarios. Additionally, GOIS reduced false positives by 40%–60%, improving real-world detection reliability. Ablation studies validate GOIS’s hierarchical slicing and parameter optimization, with 640-pixel coarse slices and 256-pixel fine slices achieving an optimal balance between accuracy and efficiency. As the first open-source TOD slicing framework on Hugging Face Apps and Google Colab, GOIS delivers real-time inference, open-source code, and live demonstrations, establishing itself as a breakthrough in object detection. The code and results are publicly available at https://github.com/MMUZAMMUL/GOIS with a live demoe at https://youtu.be/ukWUfXBFZ5I.}
}

```
![Graphical Abstract](https://github.com/MMUZAMMUL/GOIS/raw/main/data/GA-.jpg)
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

### 📊 Test GOIS Benchmarks & Gradio Live Deployement
📂 [GOIS Benchmarks Repository](https://github.com/MMUZAMMUL/TinyObjectDetection-GOIS)  
🎥 [Watch Live Demo (YouTube)](https://youtu.be/ukWUfXBFZ5I) | 🎥 [Watch Live Demo (Bilibili)](https://www.bilibili.com/video/BV1sLKjebEQK/?vd_source=f4edde9395a4d640571ae4487880e1ce)  

🔑 **MIT License** - Study & Educational Use Only  
📧 **Contact**: *[Author Email](mailto:muzamal@zju.edu.cn)*  

# 🚀 GOIS Live Deployed Applications on Gradio ✅  

Explore the **GOIS-Det vs. FI-Det** benchmark results through live interactive applications on **Gradio**. These applications provide detailed comparisons using graphs, tables, and output images, demonstrating the effectiveness of **GOIS-Det** in tiny object detection.

## 🔥 Live Benchmark Tests different categories

| **Test Function** | **Description** | **Live Test** |
|-------------------|---------------|--------------|
| **1️⃣ Single Image Analysis (GOIS-Det vs. FI-Det)** | Perform a single image test to visualize graphs and results, comparing **FI-Det vs. GOIS-Det**. View detection metrics such as the number of detections and class diversity. Outputs include **pie charts, bar charts, and two comparative images** that highlight the significance of GOIS. | [![Open in Colab](https://img.shields.io/badge/Open%20in-Colab-F9AB00?logo=googlecolab&style=for-the-badge)](https://colab.research.google.com/drive/1RM4WAPRlrCXaIwXDrWmt_lglsWkIN1eU?usp=sharing) |
| **2️⃣ Multiple Images Analysis (GOIS-Det vs. FI-Det)** | Upload multiple images simultaneously and compare **GOIS-Det** and **FI-Det** outputs. A table of detection metrics is generated to clearly evaluate the improvements achieved by GOIS. | [![Open in Colab](https://img.shields.io/badge/Open%20in-Colab-F9AB00?logo=googlecolab&style=for-the-badge)](https://colab.research.google.com/drive/1JqDhiLBb5sDNhh5z0pleiVvwpEzMtd2_?usp=sharing) |
| **3️⃣ Video Analysis (GOIS-Det vs. FI-Det)** | Perform a **video-based** evaluation of GOIS-Det vs. FI-Det. The application generates a table comparing the number of detections and detected classes, providing insights into GOIS's effectiveness. | [![Open in Colab](https://img.shields.io/badge/Open%20in-Colab-F9AB00?logo=googlecolab&style=for-the-badge)](https://colab.research.google.com/drive/1dRQepcV3ddQQOvHfRmlkOCbSZ4qHZr3b?usp=sharing) |
| **4️⃣ Metrics Evaluation & Results Graphs (GOIS-Det vs. FI-Det)** | Compare key detection metrics, including **AP, AR, mAP, and F1-score** for FI-Det and GOIS-Det. View **graphs, tables, percentage improvements, and output images** to assess GOIS's impact on detection performance. | [![Open in Colab](https://img.shields.io/badge/Open%20in-Colab-F9AB00?logo=googlecolab&style=for-the-badge)](https://colab.research.google.com/drive/1mhP8Z2-eWlGDKqg8tl0hGfghVpW6Nt55?usp=sharing) |

---

### 📌 Instructions:
1. Click on any **"Open in Colab"** button above to launch the interactive notebook.
2. Follow the instructions in the notebook to test **GOIS-Det vs. FI-Det**.
3. Evaluate detection performance using provided visualizations and metrics.


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
| **GOIS - Three Best Slicing Configurations** | Evaluates **three optimized GOIS slicing setups** based on empirical results: <br> **C1:** 512px/128px (0.1 overlap, NMS 0.3) <br> **C2:** 640px/256px (0.2 overlap, NMS 0.4) <br> **C3:** 768px/384px (0.3 overlap, NMS 0.5). These configurations were determined as optimal trade-offs between accuracy, false positive reduction, and computational efficiency. | ![Google Colab](https://www.tensorflow.org/images/colab_logo_32px.png)[📌 GOIS Ideal Slicing Test](https://colab.research.google.com/drive/1Zi5b1dXFG3gZyxwSLDiG6g-EIarUnAjK?usp=sharing) |


### 🛠 **How to Use**
1️⃣ **Open any Colab link** → 2️⃣ **Run the notebook** → 3️⃣ **Upload images or use datasets** → 4️⃣ **Adjust GOIS parameters (slice size, overlap, NMS)** → 5️⃣ **Compare FI vs. GOIS results**  

---
## 📊 GOIS Benchmark Results - Performance Comparison Across Datasets

The following tables present **benchmark evaluations** of the **Guided Object Inference Slicing (GOIS) framework**, comparing **Full Inference (FI-Det) vs. GOIS-Det** across different datasets and model configurations. 

GOIS integrates a **two-stage hierarchical slicing strategy**, dynamically adjusting **slice size, overlap rate, and NMS thresholds** to optimize detection performance. These results highlight **improvements in small object detection**, **reduction of boundary artifacts**, and **comparisons with existing slicing methods like SAHI and ASAHI**.

| **Test/Part** | **Dataset & Setup** | **Description** | **Benchmark Link** |
|--------------|---------------------|----------------|--------------------|
| **Part 1** | **Without Fine-Tuning - 15% Dataset (970 Images) - VisDrone2019Train** | Evaluates FI-Det vs. GOIS-Det on a **small dataset subset**. The table presents **AP and AR metrics for seven models**, comparing detection performance with and without GOIS enhancements. The percentage improvement achieved by GOIS is included for each model. | 📌 [Section 1 - GOIS Benchmarks](https://github.com/MMUZAMMUL/TinyObjectDetectionGOIS-Benchmarks) |
| **Part 2** | **Fine-Tuned Models (10 Epochs) - Full Dataset (6,471 Images) - VisDrone2019Train** | GOIS performance is tested after **10 epochs of fine-tuning**. The **impact of GOIS slicing parameters (coarse-fine slice size, overlap rate, NMS filtering) is analyzed**. The table provides **detailed AP and AR metrics for five models**, highlighting GOIS's ability to improve small object recall while managing computational efficiency. | 📌 [Section 2 - GOIS Benchmarks](https://github.com/MMUZAMMUL/TinyObjectDetectionGOIS-Benchmarks) |
| **Part 3** | **Without Fine-Tuning - Five Models - Full Dataset (6,471 Images) - VisDrone2019Train** | Evaluates **GOIS on a large-scale dataset without fine-tuning**, highlighting its **robust generalization ability**. **Comparative results for five models (YOLO11, YOLOv10, YOLOv9, YOLOv8, YOLOv5) include FI-Det, GOIS-Det, and % improvement achieved by GOIS.** This setup assesses GOIS’s impact on both small and large object detection. | 📌 [Section 3 - GOIS Benchmarks](https://github.com/MMUZAMMUL/TinyObjectDetectionGOIS-Benchmarks) |
| **Part 4** | **General Analysis - Pretrained Weights on VisDrone, xView, MS COCO** | GOIS's adaptability is tested across **multiple datasets and model architectures**. This section evaluates **pretrained YOLO and transformer-based detectors** (e.g., RT-DETR-L) to measure **cross-domain effectiveness, computational trade-offs, and improvements in occlusion handling**. **Key focus: Can GOIS be applied universally?** | 📌 [Section 4,5 - GOIS Benchmarks](https://github.com/MMUZAMMUL/TinyObjectDetectionGOIS-Benchmarks) |
| **Part 5** | **Comparative Analysis - SAHI vs. ASAHI vs. GOIS** | A **quantitative and qualitative comparison** between GOIS and **other slicing frameworks (SAHI, ASAHI)** across **VisDrone2019 and xView datasets**. This section examines: 1️⃣ **Boundary artifact reduction**, 2️⃣ **False positive minimization**, and 3️⃣ **Effectiveness of dynamic slicing in handling occlusion issues**. Detailed benchmark tables are included. | 📌 [Section 4,5 - GOIS vs. SAHI/ASAHI Benchmarks](https://github.com/MMUZAMMUL/TinyObjectDetectionGOIS-Benchmarks) |

---

### 🔍 **Key Improvements in GOIS Over Other Methods**
✅ **Dynamic Slicing Optimization**: Unlike static SAHI/ASAHI methods, GOIS **adjusts slice sizes and overlap rates** based on object density, reducing redundant processing.  
✅ **Occlusion Handling & Boundary Artifact Reduction**: GOIS minimizes **false detections** and **truncated object artifacts** by dynamically refining inference slices.  
✅ **Scalability Across Models & Datasets**: Successfully applied to **YOLO models, RT-DETR, and various datasets**, proving its **universal applicability**.  
✅ **Performance Gains in Small Object Detection**: GOIS consistently improves **AP-Small and AR-Small metrics**, as validated on **VisDrone and xView datasets**.  

📌 **For additional benchmark results and evaluation scripts, visit:**
[GOIS Benchmarks Repository](https://github.com/MMUZAMMUL/TinyObjectDetectionGOIS-Benchmarks)


### **Cite This Work**
If you use GOIS in your research, please consider citing our paper:








