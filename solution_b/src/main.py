from src.utils.input_validator import get_valid_input
from src.game_logic.number_generator import generate_random_number
from src.game_logic.hint_generator import provide_hint
from src.game_logic.scorer import Scorer


MIN_NUMBER = 1
MAX_NUMBER = 100
PENALTY = 10


def main():
    """
    Run the number guessing game.

    The player tries to guess a randomly generated number.
    After each incorrect guess, a hint is displayed and
    the player's score is reduced.
    """
    scorer = Scorer()
    actual_number = generate_random_number(MIN_NUMBER, MAX_NUMBER)

    while True:
        user_guess = get_valid_input(MIN_NUMBER, MAX_NUMBER)

        if user_guess == actual_number:
            print("Congratulations! You've guessed the number!")
            print(f"Final score: {scorer.get_score()}")
            break

        provide_hint(user_guess, actual_number)

        scorer.decrement_score(PENALTY)

        print(f"Current score: {scorer.get_score()}")

        if scorer.get_score() <= 0:
            print("Game over!")
            break


if __name__ == "__main__":
    main()
