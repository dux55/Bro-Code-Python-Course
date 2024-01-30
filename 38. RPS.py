import random

choices = ["rock", "paper", "scissors"]

while True:
    player = None
    while player not in choices:
        player = input().lower()
    computer = random.choice(choices)

    if player == computer:
        print("player: ", player)
        print("computer: ", computer)
        print("Tie!")
    elif player == "rock":
        if computer == "paper":
            print("player: ", player)
            print("computer: ", computer)
            print("You lose!")
        if computer == "scissors":
            print("player: ", player)
            print("computer: ", computer)
            print("You win!")
    elif player == "paper":
        if computer == "scissors":
            print("player: ", player)
            print("computer: ", computer)
            print("You lose!")
        if computer == "rock":
            print("player: ", player)
            print("computer: ", computer)
            print("You win!")
    elif player == "scissors":
        if computer == "rock":
            print("player: ", player)
            print("computer: ", computer)
            print("You lose!")
        if computer == "paper":
            print("player: ", player)
            print("computer: ", computer)
            print("You win!")
    
    play_again = input("Play again? y/n: ").lower()
    if play_again != "y":
        break

print("Bye!")
