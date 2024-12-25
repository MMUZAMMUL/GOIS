import os
import sys
import argparse
import pandas as pd

# Add the project root directory to the Python path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from my_package.evaluation_res import evaluate_predictions, get_evaluation_metrics

def calculate_percentage_improvement(full_metrics, gois_metrics):
    """
    Calculate percentage improvement between Full Inference and GOIS metrics.

    Args:
        full_metrics (dict): Evaluation metrics from Full Inference.
        gois_metrics (dict): Evaluation metrics from GOIS.

    Returns:
        dict: Percentage improvement for each metric.
    """
    improvements = {}
    for key in full_metrics:
        if full_metrics[key] != 0:  # Avoid division by zero
            improvements[key] = ((gois_metrics[key] - full_metrics[key]) / full_metrics[key]) * 100
        else:
            improvements[key] = 0.0  # If full metric is zero, improvement is zero
    return improvements

def main():
    """
    Main function to calculate and display evaluation results.
    """
    parser = argparse.ArgumentParser(description="Calculate evaluation metrics and improvements.")
    parser.add_argument("--ground_truth_path", type=str, required=True, help="Path to the ground truth COCO JSON file.")
    parser.add_argument("--full_inference_path", type=str, required=True, help="Path to the Full Inference predictions JSON file.")
    parser.add_argument("--gois_inference_path", type=str, required=True, help="Path to the GOIS predictions JSON file.")
    args = parser.parse_args()

    # Evaluate Full Inference
    print("Evaluating Full Inference...")
    full_metrics = get_evaluation_metrics(args.ground_truth_path, args.full_inference_path)
    print("\nFull Inference Metrics:")
    for k, v in full_metrics.items():
        print(f"{k}: {v:.3f}")

    # Evaluate GOIS
    print("\nEvaluating GOIS Inference...")
    gois_metrics = get_evaluation_metrics(args.ground_truth_path, args.gois_inference_path)
    print("\nGOIS Inference Metrics:")
    for k, v in gois_metrics.items():
        print(f"{k}: {v:.3f}")

    # Calculate Percentage Improvement
    improvements = calculate_percentage_improvement(full_metrics, gois_metrics)
    print("\nPercentage Improvements:")
    for k, v in improvements.items():
        print(f"{k}: {v:.2f}%")

    # Create and display result table
    model_name = os.path.splitext(os.path.basename(args.full_inference_path))[0].replace("_full_inference", "")
    data = {
        "Metrics": list(full_metrics.keys()),
        "Model Name": [model_name] * len(full_metrics),
        "Full Inference": list(full_metrics.values()),
        "GOIS": list(gois_metrics.values()),
        "Percentage Improvement": list(improvements.values())
    }
    results_df = pd.DataFrame(data)
    print("\nEvaluation Results Table:")
    print(results_df.to_string(index=False))

    # Optionally save the table as a CSV file
    results_df.to_csv(f"./{model_name}_evaluation_results.csv", index=False)
    print(f"\nResults saved to {model_name}_evaluation_results.csv")

if __name__ == "__main__":
    main()
