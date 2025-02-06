
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

## 🚀 GOIS Live Deployed Applications on Hugging Face  
Experience **Guided Object Inference Slicing (GOIS)** across **images, videos, and live cameras** with configurable parameters. Evaluate **real-time small object detection** and compare against **full-image inference (FI-Det).**  

| 🚀 **Function/Purpose**  |🗂 **Tested Data/Type** |🏆 **Models** |🔗 **Test Link** |
|-------------|--------------|------------|--------------|
| **GOIS vs. Full-Image Detection** <br> (Configurable Slicing) | Single/Multi-Image <br> VisDrone, UAV, Pedestrian | YOLO11, YOLOv10, YOLOv9, YOLOv8, YOLOv5, RT-DETR | [🔗 GOIS Live Image Processing](https://huggingface.co/spaces/MMUZAMMUL123/GOIS_Live_ImageProcessing) |
| **Video Detection (Single Stage)** <br> (Frame-wise GOIS Slicing) | Video Analysis <br> VisDrone, UAV, Pedestrian | YOLO11, YOLOv10, YOLOv9, YOLOv8, YOLOv5, RT-DETR | [🔗 GOIS Video Inference (Single Stage)](https://huggingface.co/spaces/MMUZAMMUL123/GOIS_Video_Inference_Single_Stage) |
| **Advanced Video Detection** <br> (Two-Stage GOIS Slicing) | Video Analysis <br> UAV, Tiny Object Detection | YOLO11, YOLOv10, YOLOv9, YOLOv8, YOLOv5, RT-DETR | [🔗 GOIS Video Inference (Two Stage)](https://huggingface.co/spaces/MMUZAMMUL123/GOIS_Video_Inference_Two_Stage) |
| **Live Camera Detection (FI vs. GOIS)** <br> (Real-Time Object Detection) | Live Camera <br> UAV Surveillance, Pedestrian | YOLO11, YOLOv10, YOLOv9, YOLOv8, YOLOv5, RT-DETR | [🔗 GOIS Live Camera Test](https://huggingface.co/spaces/MMUZAMMUL123/GOIS_Live_Camera_Test_Single_Stage) |
| **Live Camera Advanced Detection** <br> (Adaptive GOIS Slicing) | Live Camera <br> Tiny Object Analysis | YOLO11, YOLOv10, YOLOv9, YOLOv8, YOLOv5, RT-DETR | [🔗 GOIS Live Camera Advanced](https://huggingface.co/spaces/MMUZAMMUL123/GOIS_LiveCamera_AdvanceLevel) |

### 🔹 How to Use  
1️⃣ **Click a Test Link** → 2️⃣ **Upload Image/Video** → 3️⃣ **Adjust Parameters** → 4️⃣ **Compare FI vs. GOIS Results** → 5️⃣ **Analyze Performance in Real-Time**  


## GOIS Live Deployed Applications on Hugging Face 🚀

To evaluate the real-time effectiveness of **Guided Object Inference Slicing (GOIS)**, several live applications have been deployed on Hugging Face. These applications allow users to test GOIS across images, videos, and live camera feeds while comparing it to full-image inference (FI). 

### **Live Test Links**
Below is a list of available GOIS test environments with descriptions, tested datasets, applied models, and direct links.

|🚀 **Function/Purpose** |🗂 **Tested Data/Type** |🏆 **Models Applied** |🔍 **Short Description** |📖 **Research Paper (Section/Figure)** |🔗 **Test Link (Live) Hugging Face🚀** |
|----------------------|---------------------|-------------------|----------------------|----------------------------------|----------------------|
| **GOIS vs. Full-Image Detection** <br> Configurable Parameters: Coarse/Fine Slice Size, Overlap, NMS | Single & Multiple Image Processing <br> Datasets: VisDrone, UAV Surveillance (100-150ft), Pedestrian, Tiny Object Detection, Geo-Sciences | YOLO11, YOLOv10, YOLOv9, YOLOv8, YOLOv6, YOLOv5, RT-DETR-L, YOLOv8s-Worldv2 | GOIS slices images dynamically (coarse → fine) to detect objects missed in full-image inference. <br> - Reduces false positives by skipping uniform regions. <br> - Enhances occlusion handling through finer slicing. | Fig. 1, Sec. 1 | [GOIS Live Image Processing](https://huggingface.co/spaces/MMUZAMMUL123/GOIS_Live_ImageProcessing) |
| **Video Detection (Normal)** <br> Configurable Confidence Threshold | Video Analysis <br> Datasets: VisDrone, UAV Surveillance, Pedestrian & Tiny Object Detection, Geo-Sciences | YOLO11, YOLOv10, YOLOv9, YOLOv8, YOLOv6, YOLOv5, RT-DETR-L, YOLOv8s-Worldv2 | GOIS applies dynamic frame-wise slicing, improving small object detection in dense environments while ensuring real-time processing. | Sec. 1.4 | [GOIS Video Inference (Single Stage)](https://huggingface.co/spaces/MMUZAMMUL123/GOIS_Video_Inference_Single_Stage) |
| **Advanced Video Detection** <br> Full Inference vs. GOIS Two-Stage Slicing | Video Analysis <br> Datasets: VisDrone, UAV Surveillance (100-150ft), Pedestrian & Tiny Object Detection, Geo-Sciences | YOLO11, YOLOv10, YOLOv9, YOLOv8, YOLOv6, YOLOv5, RT-DETR-L, YOLOv8s-Worldv2 | Two-stage coarse-to-fine GOIS dynamically adjusts slicing based on object density, reducing false positives while enhancing small object detection. | Sec. 1.4 | [GOIS Video Inference (Two Stage)](https://huggingface.co/spaces/MMUZAMMUL123/GOIS_Video_Inference_Two_Stage) |
| **Live Camera Detection (FI vs. GOIS, Two Outputs)** <br> Configurable Confidence, Slice Size, Overlap Rate | Real-Time Live Camera <br> Datasets: UAV Road Surveillance, Pedestrian & Vehicle Detection (40-50ft), Dense Object Environments | YOLO11, YOLOv10, YOLOv9, YOLOv8, YOLOv6, YOLOv5, RT-DETR-L, YOLOv8s-Worldv2 | Full Inference: Single-pass detection across full frame. <br> GOIS Slicing: Divides frames into patches, applies NMS, improving small object retrieval. | Sec. TBD | [GOIS Live Camera Test (Single Stage)](https://huggingface.co/spaces/MMUZAMMUL123/GOIS_Live_Camera_Test_Single_Stage) |
| **Live Camera Advanced Detection (FI vs. GOIS, Two Outputs)** <br> Configurable Parameters | Real-Time Live Camera <br> Datasets: UAV Road Surveillance, Pedestrian & Vehicle Detection (40-50ft), Tiny Object Analysis | YOLO11, YOLOv10, YOLOv9, YOLOv8, YOLOv6, YOLOv5, RT-DETR-L, YOLOv8s-Worldv2 | Advanced GOIS Slicing: Adaptive slicing based on object density, enhances occluded and small object detection, optimizes real-time performance. | Sec. TBD | [GOIS Live Camera Advanced Level](https://huggingface.co/spaces/MMUZAMMUL123/GOIS_LiveCamera_AdvanceLevel) |

---
### **How to Use the GOIS Test Links**
1. **Click on any of the test links** in the table above.
2. **Upload an image or video** (or use live camera mode).
3. **Adjust GOIS parameters** such as slice size, overlap, or NMS.
4. **Compare GOIS vs. Full Image Inference results** and analyze small object detection performance.
5. **View processed results in real-time** and test different models.

---
## 📌 Google Colab Live Test Links for GOIS

To validate ✅ the **Guided Object Inference Slicing (GOIS)** framework, the following **Google Colab** test notebooks are available for real-time inference and analysis. These tests allow users to **compare GOIS with full-image detection (FI-Det)** across different datasets and parameter settings.

### 📝 **Table: GOIS Colab Test Links**
| 🚀 **Function/Purpose** | 🗂 **Tested Data/Type** | 🏆 **Models Applied** | 🔍 **Short Description** | 📖 **Ref to Research Paper (Section/Figure)** | 🔗 **Test Link (Live)**📌 Google Colab |
|-------------------------|------------------------|----------------------|------------------------|----------------------|----------------------|
| **GOIS (Coarse/Fine) Slicing Methodology vs. Static SAHI/ASAHI (our proposed version)** | VisDrone, UAV Surveillance (100-150ft), Pedestrian & Tiny Object Detection, Geo-Sciences | YOLO11, YOLOv10, YOLOv9, YOLOv8, YOLOv6, YOLOv5, RT-DETR-L, YOLOv8s-Worldv2 | Comparative analysis of **GOIS dynamic slicing** vs. **static slicing (SAHI, ASAHI-like)** (proposed and tested by us). | **Fig. 1, Sec. 3.2** | [![Google Colab](https://www.tensorflow.org/images/colab_logo_32px.png) **GOIS vs. Own Proposed Method (SAHI/ASAHI-like)**](https://colab.research.google.com/drive/1QTgSVe4_PYqPC5uBEcjA5bTcvDNc_Wbc?usp=sharing) |
| **Visual Test - GOIS (Single Image Inference)** | Same as above | Same as above | Users can **download a model**, load any image, set paths, and run GOIS inference. | **Fig. 3, Sec. 4.1** | [![Google Colab](https://www.tensorflow.org/images/colab_logo_32px.png) **GOIS Single Image Test**](https://colab.research.google.com/drive/1TPQKq_17Wg1NiXD5Mah0a_6bkOt4-t9b?usp=sharing) |
| **FI-Det vs. GOIS-Det (Single Image Test)** | Same as above | Same as above | Direct comparison of **GOIS-Det vs. FI-Det** on a **single image** (outputs two images). | **Fig. 5, Sec. 4.2** | [![Google Colab](https://www.tensorflow.org/images/colab_logo_32px.png) **GOIS vs. FI-Det (Single Image)**](https://colab.research.google.com/drive/1ijdnfFA3tQ9PSJDMqPXCka3KRWhrblIh?usp=sharing) |
| **FI-Det vs. GOIS-Det (Multiple Images Test)** | Same as above | Same as above | Tests **GOIS-Det vs. FI-Det** on **multiple images** with direct visual comparison. | **Fig. 6, Sec. 4.3** | [![Google Colab](https://www.tensorflow.org/images/colab_logo_32px.png) **GOIS vs. FI-Det (Multiple Images)**](https://colab.research.google.com/drive/1kwGJDVoSZ4NOTQsxdsYreYz_twRhoX0S?usp=sharing) |
| **Count-Based Metrics Detection (FI-Det vs. GOIS-Det)** | Same as above | Same as above | Computes **detection count, object area coverage, and inference speed** for both methods. | **Table 2, Sec. 5.1** | [![Google Colab](https://www.tensorflow.org/images/colab_logo_32px.png) **GOIS vs. FI-Det (Metrics Test)**](https://colab.research.google.com/drive/1X1t-L3tW1bIfVT6PtzKKFqU52PEMqivI?usp=sharing) |
| **Slice Size Optimized Speed Test (FI-Det vs. GOIS-Det)** | Same as above | Same as above | Analyzes **how different slicing sizes impact inference speed and accuracy**. | **Table 3, Sec. 5.2** | [![Google Colab](https://www.tensorflow.org/images/colab_logo_32px.png) **GOIS Optimized Speed Test**](https://colab.research.google.com/drive/1LYFnEjIinIW_4HHyVYVtg7aZVikWfnea?usp=sharing) |
| **GOIS - 81 Combinations Test (Stage 1 & 2 Slicing, IOU, NMS)** | VisDrone, UAV Surveillance, Single Image Input | Same as above | **Tests 81 different GOIS parameter combinations** (slice sizes, overlap rates, NMS thresholds). | **Fig. 7, Sec. 6.1** | [![Google Colab](https://www.tensorflow.org/images/colab_logo_32px.png) **GOIS 81 Combinations Test**](https://colab.research.google.com/drive/18H8HtFYDc0On6KMAIkfxW5xWW1hsUeFc?usp=sharing) |
| **GOIS - Three Ideal Slicing Conditions Test (Stage 1 & 2 Slicing, IOU, NMS)** | Same as above | Same as above | Evaluates three **best GOIS configurations**: <br>🔹 **C1**: 512 px / 128 px (0.1 overlap, NMS 0.3) <br>🔹 **C2**: 640 px / 256 px (0.2 overlap, NMS 0.4) <br>🔹 **C3**: 768 px / 384 px (0.3 overlap, NMS 0.5) | **Table 4, Sec. 6.2** | [![Google Colab](https://www.tensorflow.org/images/colab_logo_32px.png) **GOIS Ideal Slicing Test**](https://colab.research.google.com/drive/1Zi5b1dXFG3gZyxwSLDiG6g-EIarUnAjK?usp=sharing) |

---

### 🛠 **How to Use**
1. **Open any Colab link** 🔗 from the table above.
2. **Run the notebook**, follow the instructions to set model paths and data.
3. **Upload custom images** if needed or use provided test datasets.
4. **Compare results** between **GOIS vs. FI-Det** and adjust parameters.

---



### **Cite This Work**
If you use GOIS in your research, please consider citing our paper:








