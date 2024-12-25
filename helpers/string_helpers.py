def reverse_string(s):
    """Reverse a string."""
    return s[::-1]

def count_vowels(s):
    """Count vowels in a string."""
    return sum(1 for char in s.lower() if char in 'aeiou')
