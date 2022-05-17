"""
Team C
Monday, May 2nd, 2022
COMP-310
Project 4: Gambling Philosophers
"""

#Including nescessary libraries and packages
import os
import threading

from random_threads import getRand

#Define dealing functions
def deal():
    hand = []
    for i in range(2):
        card = getRand()
        #Convert high-numbers to face cards
        if card == 11:card = "J"
        if card == 12: card = "Q"
        if card == 13: card = "K"
        if card == 14: card = "A"
        hand.append(card)
    return hand

def play_again():
    again = input("Do you want to play again? (Y/N) : ").lower()
    if again == "y":
        dealer_hand = []
        player_hand = []
        game()
    else: 
        print("Bye!")
        exit()

def total(hand): 
    total = 0
    for card in hand: 
        if card == "J" or card == "Q" or card == "K":
            total += 10
        elif card == "A":
            if total >= 11: total += 1
            else: total += 11
        else: 
            total += card
    return total

def hit(hand):
    card = getRand()
    if card == 11:card = "J"
    if card == 12:card = "Q"
    if card == 13:card = "K"
    if card == 14:card = "A"
    hand.append(card)
    return hand

def clear():
    if os.name == 'nt':
        os.system('CLS')
    if os.name == 'posix':
        os.system('clear')

def print_results(dealer_hand, player_hand):
    clear()
    print ("The dealer has a " + str(dealer_hand) + " for a total of " + str(total(dealer_hand)))
    print ("You have a " + str(player_hand) + " for a total of " + str(total(player_hand)))

def blackjack(dealer_hand, player_hand):
    if total(player_hand) == 21:
        print_results(dealer_hand, player_hand)
        print ("Congratulations! You got a Blackjack!\n")
        play_again()
    elif total(dealer_hand) == 21:
        print_results(dealer_hand, player_hand)		
        print ("Sorry, you lose. The dealer got a blackjack.\n")
        play_again()
    elif total(player_hand) > 21:
        print_results(dealer_hand, player_hand)
        print("Sorry, you busted. You lost\n")

def score(dealer_hand, player_hand):
    if total(player_hand) == 21:
        print_results(dealer_hand, player_hand)
        print("Congratulations! You've got a Blackjack!\n")
        play_again()
    elif(total(dealer_hand) == 21):
        print_results(dealer_hand, player_hand)
        print("Sorry, you lose. The dealer got a blackjack.\n")
        play_again()
    elif total(player_hand) > 21:
        print_results(dealer_hand, player_hand)
        print("Sorry, you busted. You lost\n")
        play_again()
    elif total(dealer_hand) > 21:
        print_results(dealer_hand, player_hand)
        print("Dealer busts. You win!\n")
        play_again()
    elif total(player_hand) < total(dealer_hand):
        print_results(dealer_hand, player_hand)
        print("Sorry. Your score isn't higher than the dealer. You lose\n")
        play_again()
    elif total(player_hand) > total(dealer_hand):
        print_results(dealer_hand, player_hand)
        print("Congratulations! Your score is higher than the dealer. You win!\n")
        play_again()


def game():
    choice = 0
    clear()
    print ("WELCOME TO BLACKJACK!\n")
    dealer_hand = deal()
    player_hand = deal()
    while choice != "q":
        print ("The dealer is showing a " + str(dealer_hand[0]))
        print ("You have a " + str(player_hand) + " for a total of " + str(total(player_hand)))
        blackjack(dealer_hand, player_hand)
        choice = input("Do you want to [H]it, [S]tand, or [Q]uit: ").lower()
        clear()
        if choice == "h":
            hit(player_hand)
            if total(dealer_hand) < 17:
                hit(dealer_hand)
            blackjack(dealer_hand, player_hand)
        elif choice == "s":
            while total(dealer_hand) < 17:
                hit(dealer_hand)
            score(dealer_hand, player_hand)
        elif choice == "q":
            print ("Bye!")
            exit()
    
if __name__ == "__main__":
   game()	
   
