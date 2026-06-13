import random

def number_guess():
    number_to_guess = random.randint(1, 100)
    print("Welcome to the Number Guessing Game!")
    print("I have selected a number between 1 and 100. Can you guess it?")
    while True:
        try:
            user_guess = int(input("Enter your guess: "))
        except ValueError:
            print("Invalid input. Please enter a number between 1 and 100.")
            continue
        finally:
            print("Thank you for your guess!")

        if user_guess < 1 or user_guess > 100:
            print("Please guess a number between 1 and 100.")
            continue

        if user_guess < number_to_guess:
            print("Too low! Try again.")
        elif user_guess > number_to_guess:
            print("Too high! Try again.")
        else:
            print(f"Congratulations! You've guessed the number {number_to_guess} correctly!")
            break

    

number_guess()