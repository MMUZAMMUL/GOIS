from pycocotools.coco import COCO
from pycocotools.cocoeval import COCOeval
import argparse

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

def main():
    """
    Main function to parse arguments and run evaluation.
    """
    parser = argparse.ArgumentParser(description="Evaluate predictions using COCO metrics.")
    parser.add_argument("--ground_truth_path", type=str, required=True, help="Path to the ground truth COCO JSON file.")
    parser.add_argument("--predictions_path", type=str, required=True, help="Path to the predictions COCO JSON file.")
    parser.add_argument("--iou_type", type=str, default='bbox', help="Type of evaluation (default: 'bbox').")
    args = parser.parse_args()

    # Run the evaluation
    evaluate_predictions(args.ground_truth_path, args.predictions_path, args.iou_type)

if __name__ == "__main__":
    main()
