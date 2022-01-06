import random
options = ["rock", "paper", "scissors"]
computer_selection = options[random.randrange(0,3)]

while True:
    user_selection = input("Please choose rock, paper or scissors: ").lower()
    if user_selection in options:
        break
    else:
        user_selection = input("Please write rock, paper or scissors as your response: ").lower()

if user_selection == computer_selection:
    print(f"Nobody won. You and computer selected {user_selection} as response")
    exit()

if user_selection == "rock" and computer_selection == "scissors":
    print(f"You won. You selected {user_selection} and computer selected {computer_selection}")
elif user_selection == "paper" and computer_selection == "rock":
    print(f"You won. You selected {user_selection} and computer selected {computer_selection}")
elif user_selection == "scissors" and computer_selection == "paper":
    print(f"You won. You selected {user_selection} and computer selected {computer_selection}")
else:
    print(f"Computer won. You selected {user_selection} and computer selected {computer_selection}")
