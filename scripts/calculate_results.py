import os
import sys
import argparse
import pandas as pd

# Add the project root directory to the Python path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from my_package.evaluation_res import get_evaluation_metrics

def main():
    """
    Main function to calculate results and generate evaluation table.
    """
    # Parse command-line arguments
    parser = argparse.ArgumentParser(description="Calculate evaluation results for Full Inference and GOIS.")
    parser.add_argument("--ground_truth_path", type=str, required=True, help="Path to the ground truth COCO JSON file.")
    parser.add_argument("--full_inference_path", type=str, required=True, help="Path to the Full Inference JSON file.")
    parser.add_argument("--gois_inference_path", type=str, required=True, help="Path to the GOIS Inference JSON file.")
    args = parser.parse_args()

    # Get metrics for Full Inference
    print("Evaluating Full Inference...")
    full_metrics = get_evaluation_metrics(args.ground_truth_path, args.full_inference_path)

    # Get metrics for GOIS Inference
    print("Evaluating GOIS Inference...")
    gois_metrics = get_evaluation_metrics(args.ground_truth_path, args.gois_inference_path)

    # Generate evaluation results table
    results = []
    for metric, full_value in full_metrics.items():
        gois_value = gois_metrics[metric]

        # Calculate % Improvement
        if full_value != 0:
            improvement = ((gois_value - full_value) / full_value) * 100
            improvement = round(improvement, 2)  # % Improvement rounded to 2 decimal places
        else:
            improvement = "N/A"

        # Append results
        results.append({
            "Metric": metric,
            "Full Inference": round(full_value, 3),  # Round Full Inference to 3 decimal places
            "GOIS Inference": round(gois_value, 3),  # Round GOIS Inference to 3 decimal places
            "% Improvement": improvement
        })

    # Convert to DataFrame
    results_df = pd.DataFrame(results)

    # Display results
    print("\nEvaluation Results:")
    print(results_df)

    # Save results to CSV
    output_path = "evaluation_results.csv"
    results_df.to_csv(output_path, index=False)
    print(f"\nResults saved to {output_path}")

if __name__ == "__main__":
    main()
