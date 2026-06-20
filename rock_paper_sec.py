import random 

class RockPaperScissors:
    def __init__(self):
        self.choices = ["rock", "paper", "scissors"]

    def play(self):
        for _ in range(3):
            user_choice = input("Enter your choice (rock, paper, scissors): ").lower().strip()
            if user_choice not in self.choices:
                print("Invalid choice. Please choose rock, paper, or scissors.")
                return

            computer_choice = random.choice(self.choices)
            print(f"Computer chose: {computer_choice}")

            if user_choice == computer_choice:
                print("It's a tie!")
            elif (user_choice == "rock" and computer_choice == "scissors") or \
                 (user_choice == "paper" and computer_choice == "rock") or \
                 (user_choice == "scissors" and computer_choice == "paper"):
                print("user wins this round!")
            else:
                print("Computer wins this round!")
            print("continue playing to see who wins the game!")

rock_paper_scissors_game = RockPaperScissors()
rock_paper_scissors_game.play()