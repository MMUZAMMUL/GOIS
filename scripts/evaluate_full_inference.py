import os
from my_package.evaluation import evaluate_predictions

# Paths to ground truth and predictions
ground_truth_path = './data/ground_truth/ground_truth_coco.json'
predictions_path = './data/full_inference/yolov10n/yolov10n_predictions.json'

def main():
    """
    Main function to evaluate full inference results.
    """
    # Check if the files exist
    if not os.path.exists(ground_truth_path):
        raise FileNotFoundError(f"Ground truth file not found: {ground_truth_path}")
    if not os.path.exists(predictions_path):
        raise FileNotFoundError(f"Predictions file not found: {predictions_path}")

    # Perform evaluation
    evaluate_predictions(ground_truth_path, predictions_path, iou_type='bbox')

if __name__ == "__main__":
    main()
