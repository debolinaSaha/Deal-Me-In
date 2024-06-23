# Blackjack Project
# from replit import clear
from art1 import logo
import random
import os
import platform
wanna_play = input("Do you want to play Blackjack? \n Type y/n : \n")

def clear_console():
    if platform.system() == "Windows":
        os.system("cls")
    else:
        os.system("clear")

clear_console()


print(logo)
numbers = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

def add_cards(your_cards1, your_cards2, your_cards3):
    return your_cards1 + your_cards2 + your_cards3

def computer_cards(computer_cards1, computer_card_reveal, computer_card2):
    return computer_cards1 + computer_card_reveal + computer_card2

game_on = True
while game_on == True:
# user's card choosing.
    your_cards1 = random.choice([11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10])
    your_cards2 = random.choice([11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10])
    print("Your cards: ", [your_cards1, your_cards2])

    total = add_cards(your_cards1, your_cards2, 0)
    print("Total number of cards you've got is", total)

    # computer's card choosing.
    computer_card1 = random.choice([11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10])
    computer_card_reveal = "hidden"
    print("Computer's first card: ", computer_card1)
    print(f"Computer's second card is {computer_card_reveal}.")

    get_or_lose = input("Type 'y' to get another card, type 'n' to pass: \n")
    your_cards3 = random.choice([11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10])
    if get_or_lose == "y":
        print("Your cards: ", [your_cards1, your_cards2, your_cards3])
        total = add_cards(your_cards1, your_cards2, your_cards3)
        print("Total number of cards you've got is", total)
    else:
        total = add_cards(your_cards1, your_cards2, 0)
        print("Total number of cards you've got is", total)

    # computer's cards
    computer_card_reveal = random.choice([11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10])
    print("Computer's second card: ", computer_card_reveal)
    computer_card2 = random.choice([11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10])
    print("Computer's third card: ", computer_card2)

    # total cards the computer has got
    computer_total = computer_cards(computer_card1, computer_card_reveal, computer_card2)
    print("Total number of cards the computer has:", computer_total)

    if total > computer_total:
        print("You win!")
    elif total == computer_total:
        print("It's a draw!")
    elif total < computer_total:
        print("You lose!")
    elif total > 21:
        print("Bust!")

    add_cards(your_cards1, your_cards2, your_cards3)
    print()
    replay = input("Do you want to play again? Enter (y/n): ")
    if replay == 'y':
        game_on = True
        clear_console()
    else:
        game_on = False
        print("Game Ended!")




