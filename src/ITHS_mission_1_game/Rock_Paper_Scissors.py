import random
import os


def get_user_choice():

    print("=========================================")
    print("Let´s play the Rock, Paper, Scissors Game\nIt starts by you choising the rock, paper or scissors.\nPlease make your choice!")
    print("=========================================")
    print("rock")
    print("paper")
    print("scissors")
    choice = input(str("\nEnter your choice (rock/paper/scissors): "))
    return choice


def get_computer_choice():
    return random.choice(["rock", "paper", "scissors"])


def aras_determine_winner(user_choice, computer_choice):

    if user_choice == computer_choice:
        print(f"Both players selected {user_choice}. It's a tie!")
    elif user_choice == "rock":
        if computer_choice == "scissors":
            print("\n~~ Rock smashes scissors! You win! ~~")
        else:
            print("\n~~ Paper covers rock! You lose! ~~")
    elif user_choice == "paper":
        if computer_choice == "rock":
            print("\n ~~Paper covers rock! You win! ~~")
        else:
            print("\n~~ Scissors cuts paper! You lose! ~~")
    elif user_choice == "scissors":
        if computer_choice == "paper":
            print("\n ~~Scissors cuts paper! You win! ~~")
        else:
            print("\n~~ Rock smashes scissors! You lose! ~~")


def main():
    while True:
        user_choice = get_user_choice()
        if user_choice not in ["rock", "paper", "scissors"]:
            os.system('clear')
            print("\n========================================")
            print("\n\n!!!!!!!!Invalid choice. Please enter rock, paper, or scissors!!!!!!!\n")
            continue

        computer_choice = get_computer_choice()

        print(f"You chose {user_choice}!")
        print(f"Computer chose {computer_choice}!")
        aras_determine_winner(user_choice, computer_choice)
        play_again = input("\nPlay again? (y/n): ").lower()
        if play_again != "y":
            break


os.system('clear')  # Clearing the Screen

if __name__ == "__main__":
    main()
