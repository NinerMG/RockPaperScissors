import random
from ast import literal_eval
from os import linesep

options = ["rock", "paper", "scissors"]
wins_options = {"rock": "paper",
                "paper": "scissors",
                "scissors": "rock"}

def get_user_name():
    name = input("Enter your name: ")
    print(f"Hello, {name}!")
    return name

def get_user_choice():
    choice = input("Enter your choice rock/paper/scissors\n")
    return choice

def get_computer_choice():
    return random.choice(options)

def determine_winner(user, computer):
    if user == computer:
        return "draw", 50
    elif wins_options[user] == computer:
        return "win", 100
    else:
        return "lose", 0

def print_result(result, computer_choice):
    if result == "draw":
        print(f"There is a draw ({computer_choice})")
    elif result == "win":
        print(f"Well done. The computer chose {computer_choice} and failed")
    else:
        print(f"Sorry, but the computer chose {computer_choice}")

def get_rating_from_file(name):
    try:
        with open("rating.txt", "r") as file:
            all_players = file.readlines()

    except FileNotFoundError:
        with open("rating.txt", "w") as file:
            file.write(f"{name} 0")
    else:
        for player in all_players:
            part_player = player.strip().split()
            if len(part_player) == 2 and part_player[0] == name:
                return int(part_player[1])
        return 0

def save_rating_to_file(name, rating):
    lines = []
    try:
        with open("rating.txt", "r") as file:
            lines = file.readlines()
    except FileNotFoundError:
        pass

    for i, line in enumerate(lines):
        parts = line.split()
        if len(parts) == 2 and parts[0] == name:
            score = int(parts[1]) + rating
            lines[i] = f"{name} {score}\n"
            break
        else:
            lines.append(f"{name} {rating}")

    with open("rating.txt", "w") as file:
        file.writelines(lines)

def game():
    name = get_user_name()
    score = get_rating_from_file(name)
    while True:
        user_choice = get_user_choice()
        if user_choice == "!exit":
            save_rating_to_file(name, score)
            print("Bye!")
            break
        if user_choice == "!rating":
            print(f"Your rating: {score}")
            continue
        if user_choice not in options:
            print("Wrong input, try again!")
            continue

        computer_choice = get_computer_choice()

        result, points = determine_winner(user_choice, computer_choice)
        score = score + points
        print_result(result, computer_choice)

game()
