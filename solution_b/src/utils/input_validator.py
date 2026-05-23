def get_valid_input(start: int, end: int) -> int:
    """
    Prompt the user to enter a valid integer within a range.

    Args:
        start (int): Minimum acceptable value.
        end (int): Maximum acceptable value.

    Returns:
        int: A validated integer entered by the user.
    """
    while True:
        try:
            user_input = int(
                input(f"Please enter a number between {start} and {end}: ")
            )

            if start <= user_input <= end:
                return user_input

            print(f"Input must be between {start} and {end}.")

        except ValueError:
            print("Invalid input. Please enter a valid integer.")

if __name__ == "__main__":
    print(get_valid_input(1, 100))
