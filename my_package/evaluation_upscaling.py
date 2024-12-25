from pycocotools.coco import COCO
from pycocotools.cocoeval import COCOeval
import pandas as pd

def get_evaluation_metrics(ground_truth_path, predictions_path):
    """
    Evaluate predictions using COCO metrics.

    Args:
        ground_truth_path (str): Path to the ground truth COCO JSON file.
        predictions_path (str): Path to the predictions COCO JSON file.

    Returns:
        dict: Evaluation metrics (AP and AR values).
    """
    print(f"Evaluating predictions: {predictions_path} with ground truth: {ground_truth_path}")
    
    # Load ground truth and predictions
    coco_gt = COCO(ground_truth_path)
    coco_dt = coco_gt.loadRes(predictions_path)

    # Initialize COCOeval
    coco_eval = COCOeval(coco_gt, coco_dt, iouType='bbox')

    # Perform evaluation
    coco_eval.evaluate()
    coco_eval.accumulate()
    coco_eval.summarize()

    # Extract metrics from COCOeval
    metrics = {
        "AP@[IoU=0.50:0.95]": coco_eval.stats[0],
        "AP@[IoU=0.50]": coco_eval.stats[1],
        "AP@[IoU=0.75]": coco_eval.stats[2],
        "AP@[small]": coco_eval.stats[3],
        "AP@[medium]": coco_eval.stats[4],
        "AP@[large]": coco_eval.stats[5],
        "AR@[IoU=0.50:0.95|max=1]": coco_eval.stats[6],
        "AR@[IoU=0.50:0.95|max=10]": coco_eval.stats[7],
        "AR@[IoU=0.50:0.95|max=100]": coco_eval.stats[8],
        "AR@[small]": coco_eval.stats[9],
        "AR@[medium]": coco_eval.stats[10],
        "AR@[large]": coco_eval.stats[11],
    }
    return metrics

def evaluate_and_generate_upscaling_results(ground_truth_path, full_inference_path, gois_inference_path):
    """
    Evaluate Full Inference and GOIS Inference and apply upscaling.

    Args:
        ground_truth_path (str): Path to the ground truth COCO JSON file.
        full_inference_path (str): Path to the Full Inference JSON file.
        gois_inference_path (str): Path to the GOIS Inference JSON file.

    Returns:
        tuple: Original results DataFrame, upscaled results DataFrame
    """
    # Get metrics for Full Inference and GOIS Inference
    full_metrics = get_evaluation_metrics(ground_truth_path, full_inference_path)
    gois_metrics = get_evaluation_metrics(ground_truth_path, gois_inference_path)

    # Generate the original results table
    original_results = []
    for metric, full_value in full_metrics.items():
        gois_value = gois_metrics[metric]
        improvement = ((gois_value - full_value) / full_value * 100) if full_value != 0 else "N/A"
        original_results.append({
            "Metric": metric,
            "Full Inference": round(full_value, 3),
            "GOIS Inference": round(gois_value, 3),
            "% Improvement": round(improvement, 2) if improvement != "N/A" else "N/A"
        })
    original_df = pd.DataFrame(original_results)

    # Generate the upscaled results table
    upscaled_results = []
    for metric, full_value in full_metrics.items():
        gois_value = gois_metrics[metric]
        full_upscaled = full_value * 10
        gois_upscaled = gois_value * 10
        improvement_upscaled = ((gois_upscaled - full_upscaled) / full_upscaled * 100) if full_upscaled != 0 else "N/A"
        upscaled_results.append({
            "Metric": metric,
            "Full Inference (Upscaled)": round(full_upscaled, 3),
            "GOIS Inference (Upscaled)": round(gois_upscaled, 3),
            "% Improvement (Upscaled)": round(improvement_upscaled, 2) if improvement_upscaled != "N/A" else "N/A"
        })
    upscaled_df = pd.DataFrame(upscaled_results)

    return full_metrics, gois_metrics, original_df, upscaled_df
