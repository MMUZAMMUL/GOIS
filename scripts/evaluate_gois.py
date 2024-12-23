import os
from pycocotools.coco import COCO
from pycocotools.cocoeval import COCOeval

# User-configurable paths
ground_truth_path = './data/ground_truth/ground_truth_coco.json'
gois_results_path = './data/gois_results/'

def evaluate_gois_results():
    """
    Evaluate GOIS predictions using COCO metrics.
    """
    # List available GOIS result folders
    available_models = [folder for folder in os.listdir(gois_results_path) if os.path.isdir(os.path.join(gois_results_path, folder))]

    if not available_models:
        print("No GOIS results available. Please run GOIS inference first.")
        return

    # Display available models
    print("Available GOIS results for evaluation:")
    for idx, model_name in enumerate(available_models, 1):
        print(f"{idx}. {model_name}")

    # User selects a model
    selected_idx = int(input("Select a model by entering its number: "))
    if selected_idx < 1 or selected_idx > len(available_models):
        print("Invalid selection. Exiting.")
        return

    selected_model = available_models[selected_idx - 1]
    print(f"Selected model for evaluation: {selected_model}")

    # Configure paths
    sliced_predictions_path = os.path.join(gois_results_path, selected_model, f"{selected_model}_GOIS_predictions.json")

    # Check if necessary files exist
    if not os.path.exists(ground_truth_path):
        raise FileNotFoundError(f"Ground truth file not found: {ground_truth_path}")
    if not os.path.exists(sliced_predictions_path):
        raise FileNotFoundError(f"Predictions file not found: {sliced_predictions_path}")

    # Perform evaluation
    print("Starting evaluation...")
    coco_gt = COCO(ground_truth_path)
    coco_dt = coco_gt.loadRes(sliced_predictions_path)

    coco_eval = COCOeval(coco_gt, coco_dt, iouType='bbox')
    coco_eval.evaluate()
    coco_eval.accumulate()
    coco_eval.summarize()

    print(f"Evaluation completed for model: {selected_model}")

if __name__ == "__main__":
    evaluate_gois_results()
