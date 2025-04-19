#In this version computer always wins with user

computer_options = {"rock": "paper",
                    "paper": "scissors",
                    "scissors": "rock"}

def game():
    user_choice = input("Enter your choice rock/paper/scissors\n")
    if user_choice not in computer_options:
        print("Wrong input, try again!")
        game()
    else:
        computer_choice = computer_options[user_choice]
        print(f"Sorry, but the computer chose {computer_choice}")

game()