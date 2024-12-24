import os
import sys
import argparse

# Add the project root directory to the Python path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from my_package.evaluation import evaluate_predictions

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
