import os
import sys
import argparse
import pandas as pd

# Add the project root directory to the Python path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from my_package.evaluation_upscaling import evaluate_and_generate_upscaling_results

# Ensure pandas does not truncate wide tables in the console
pd.set_option("display.max_columns", None)  # Show all columns
pd.set_option("display.width", 1000)       # Set a wide display width

def main():
    """
    Main function to evaluate upscaling results and generate tables.
    """
    # Parse command-line arguments
    parser = argparse.ArgumentParser(description="Evaluate results and apply upscaling.")
    parser.add_argument("--ground_truth_path", type=str, required=True, help="Path to the ground truth COCO JSON file.")
    parser.add_argument("--full_inference_path", type=str, required=True, help="Path to the Full Inference JSON file.")
    parser.add_argument("--gois_inference_path", type=str, required=True, help="Path to the GOIS Inference JSON file.")
    args = parser.parse_args()

    # Run evaluation and upscaling
    print("Running evaluation with upscaling...")
    full_results, gois_results, combined_table, upscaled_table = evaluate_and_generate_upscaling_results(
        args.ground_truth_path, args.full_inference_path, args.gois_inference_path
    )

    # Display the results
    print("\nOriginal Evaluation Results:")
    print(combined_table)

    print("\nUpscaled Evaluation Results:")
    print(upscaled_table)

    # Save results to CSV
    combined_table.to_csv("original_evaluation_results.csv", index=False)
    upscaled_table.to_csv("upscaled_evaluation_results.csv", index=False)

    print("\nResults saved to 'original_evaluation_results.csv' and 'upscaled_evaluation_results.csv'")

if __name__ == "__main__":
    main()
