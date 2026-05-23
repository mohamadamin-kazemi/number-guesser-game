import random


def validate_input(user_guess):
    if not user_guess.isdigit():
        print("Please enter a valid number.")
        return False
    if not 0 <= int(user_guess) <= 100:
        print("Your guess is out of range. Please enter a number between 1 and 100.")
        return False
    return True


def main():
    rand_num = random.randint(1, 100)
    score = 100

    while True:
        user_guess = input("Guess a number between 1 and 100: ")
        if user_guess == "q":
            break

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
        score = max(score, 0)
    

if __name__ == "__main__":
    main()
rand_num = random.randint(1, 100)
