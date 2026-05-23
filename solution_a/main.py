import random

def validate_input(user_guess):
    if not user_guess.isdigit():
        print("Please enter a valid number.")
        return False
    if not 1 <= int(user_guess) <= 100:
        print("Your guess is out of range. Please enter a number between 1 and 100.")
        return False
    return True

def main():
    while True:
        rand_num = random.randint(1, 100)
        # print(rand_num)  # Uncomment for debugging
        score = 100

        while True:
            user_guess = input("Guess a number between 1 and 100: ").strip()
            if user_guess.lower() == "q":
                print("Thanks for playing! Have a nice day!")
                return

            if not validate_input(user_guess):
                continue

            user_guess = int(user_guess)
            if user_guess < rand_num:
                print("Too low!")
            elif user_guess > rand_num:
                print("Too high!")
            else:
                print(f"Congratulations! You guessed the correct number! Your score is {score}.")
                break

            score -= 10
            if score <= 0:
                print(f"Game over! The correct number was {rand_num}.")
                break

        play_again = input("If you want to play again, enter 'y', else enter any other key to exit: ").strip()
        if play_again.lower() != 'y':
            print("Thanks for playing! Have a nice day!")
            break

if __name__ == "__main__":
    main()
    