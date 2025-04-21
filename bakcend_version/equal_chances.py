import random

options = ["rock", "paper", "scissors"]
wins_options = {"rock": "paper",
                "paper": "scissors",
                "scissors": "rock"}

def get_user_choice():
    choice = input("Enter your choice rock/paper/scissors\n")
    return choice

def get_computer_choice():
    return random.choice(options)

def determine_winner(user, computer):
    if user == computer:
        return "draw"
    elif wins_options[user] == computer:
        return "win"
    else:
        return "lose"

def print_result(result, computer_choice):
    if result == "draw":
        print(f"There is a draw ({computer_choice})")
    elif result == "win":
        print(f"Well done. The computer chose {computer_choice} and failed")
    else:
        print(f"Sorry, but the computer chose {computer_choice}")

def game():
    while True:
        user_choice = get_user_choice()
        if user_choice == "!exit":
            print("Bye!")
            break
        if user_choice not in options:
            print("Wrong input, try again!")
            continue

        computer_choice = get_computer_choice()
        result = determine_winner(user_choice, computer_choice)
        print_result(result, computer_choice)

game()
