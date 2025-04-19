import random

options = ["rock", "paper" , "scissors"]
wins_options = {"rock": "paper",
                    "paper": "scissors",
                    "scissors": "rock"}

def game():
    while True:
        user_choice = input("Enter your choice rock/paper/scissors\n")
        if user_choice == "!exit":
            print("Bye!")
            break
        if user_choice not in options:
            print("Wrong input, try again!")
        else:
            computer_choice = random.choice(options)

            if user_choice == computer_choice:
                print(f"There is a draw ({computer_choice})")
            elif wins_options[user_choice] == computer_choice:
                print(f"Well done. The computer chose {computer_choice} and failed")
            else:
                print(f"Sorry, but the computer chose {computer_choice}\n")
game()