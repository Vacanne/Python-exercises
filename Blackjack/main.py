from replit import clear
from art import logo
import random


def deal():
    """Adds a random card to hand"""
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    card = random.choice(cards)
    return card


def score(cards):
    """ Take a list of cards and returns the sum as score"""
    if sum(cards) == 21 and len(cards) == 2:
        return 0
    if 11 in cards and sum(cards) > 21:
        cards.remove(11)
        cards.append(1)
    return sum(cards)


def compare(score_user, score_computer):
    if score_user == score_computer:
        return "Draw"
    elif score_computer == 0:
        return "Lose, Computer has blackjack"
    elif score_user == 0:
        return "Win with a blackjack"
    elif score_user > 21:
        return "You went over. You Lose"
    elif score_computer > 21:
        return "Computer went over. You win"
    elif score_user > score_computer:
        return "You win"
    else:
        return "You lose"


def play():
    print(logo)

    user_hand = []
    computer_hand = []
    is_game_over = False

    for _ in range(2):
        user_hand.append(deal())
        computer_hand.append(deal())

    while not is_game_over:
        user_score = score(user_hand)
        computer_score = score(computer_hand)

        print(f"Your cards: {user_hand}, current score: {user_score}")
        print(f"Computer's first card: {computer_hand[0]}")

        if user_score == 0 or computer_score == 0 or user_score > 21:
            is_game_over = True
        else:
            deal_to_user = input("Do you want another card? ('y' or 'n')")
            if deal_to_user == "y":
                user_hand.append(deal())
            else:
                is_game_over = True

    while 0 < computer_score < 17:
        computer_hand.append(deal())
        computer_score = score(computer_hand)

    print(f"Your final hand: {user_hand}, final score: {score(user_hand)}")
    print(f"Computer's final hand: {computer_hand}, final score:{score(computer_hand)}")
    print(compare(user_score, computer_score))


while input("Do you want to play blackjack? ('y' or 'n')") == "y":
    play()
    clear()
