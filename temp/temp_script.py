import time

def temp_process():
    """Simulate a temporary process."""
    for i in range(5):
        print(f"Running temp process {i + 1}/5...")
        time.sleep(1)
    print("Temporary process complete.")
