from pycocotools.coco import COCO
from pycocotools.cocoeval import COCOeval

def evaluate_predictions(ground_truth_path, predictions_path, iou_type='bbox'):
    """
    Evaluate predictions using COCO metrics.

    Args:
        ground_truth_path (str): Path to the ground truth COCO JSON file.
        predictions_path (str): Path to the predictions COCO JSON file.
        iou_type (str): Type of evaluation (default is 'bbox').

    Returns:
        None: Displays evaluation metrics on the console.
    """
    print(f"Evaluating predictions...\nGround Truth: {ground_truth_path}\nPredictions: {predictions_path}")

    # Load ground truth and predictions
    coco_gt = COCO(ground_truth_path)
    coco_dt = coco_gt.loadRes(predictions_path)

    # Initialize COCOeval
    coco_eval = COCOeval(coco_gt, coco_dt, iouType=iou_type)

    # Perform evaluation
    coco_eval.evaluate()
    coco_eval.accumulate()
    coco_eval.summarize()
