







## GOIS Live Deployed Applications on Hugging Face 🚀

To evaluate the real-time effectiveness of **Guided Object Inference Slicing (GOIS)**, several live applications have been deployed on Hugging Face. These applications allow users to test GOIS across images, videos, and live camera feeds while comparing it to full-image inference (FI). 

### **Live Test Links**
Below is a list of available GOIS test environments with descriptions, tested datasets, applied models, and direct links.

| **Function/Purpose** | **Tested Data/Type** | **Models Applied** | **Short Description** | **Research Paper (Section/Figure)** | **Test Link (Live)** |
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

For more details, please refer to the **research paper** where these experiments and methodologies are explained in depth.

---

### **Cite This Work**
If you use GOIS in your research, please consider citing our paper:








