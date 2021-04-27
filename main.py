play = "y"
import random
while play == "y":
    print("...rock...")
    print("...paper...")
    print("...scissors...")
    choices = ["rock", "paper", "scissors"]
    comp_choice = random.choice(choices)
    user_choice = input("Player choice: ")
    print("Shoot!")
    if comp_choice == user_choice:
        print("Tie!")
    elif comp_choice == "rock" and user_choice == "scissors":
        print("You lose!")
    elif comp_choice == "rock" and user_choice == "paper":
        print("You win!")
    elif comp_choice == "scissors" and user_choice == "rock":
        print("You win!")
    elif comp_choice == "scissors" and user_choice == "paper":
        print("You lose!")
    elif comp_choice == "paper" and user_choice == "rock":
        print("You lose!")
    elif comp_choice == "paper" and user_choice == "scissors":
        print("You win!")
    print("")
    play = input("Another round?(y/n) ")
    if play == "n":
        print("Bye-bye")
    print("")
