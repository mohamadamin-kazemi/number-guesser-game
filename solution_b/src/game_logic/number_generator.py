import random


def generate_random_number(start: int, end: int) -> int:
    """
    Generate a random integer within a given range.

    Args:
        start (int): Minimum possible value.
        end (int): Maximum possible value.

    Returns:
        int: Randomly generated integer.
    """
    return random.randint(start, end)
