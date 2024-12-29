from pycocotools.coco import COCO
from pycocotools.cocoeval import COCOeval

def get_evaluation_metrics(ground_truth_path, predictions_path):
    """
    Evaluate predictions using COCO metrics and extract key metrics.

    Args:
        ground_truth_path (str): Path to the ground truth COCO JSON file.
        predictions_path (str): Path to the predictions COCO JSON file.

    Returns:
        dict: A dictionary of evaluation metrics.
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

    # Extract metrics
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
        "AR@[large]": coco_eval.stats[11]
    }

    return metrics
