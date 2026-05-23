def provide_hint(guess_number: int, actual_number: int) -> None:
    """
    Display a hint comparing the guessed number
    with the actual number.

    Args:
        guess_number (int): Number guessed by the player.
        actual_number (int): Correct target number.
    """
    if guess_number < actual_number:
        print("Your guess is too low.")
    else:
        print("Your guess is too high.")
