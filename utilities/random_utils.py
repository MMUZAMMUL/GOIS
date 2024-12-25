import random

def generate_random_numbers(size=10):
    """Generate a list of random numbers."""
    return [random.randint(0, 100) for _ in range(size)]

def dummy_math_function(a, b):
    """Perform a dummy mathematical operation."""
    return (a * b) + random.randint(1, 10)
