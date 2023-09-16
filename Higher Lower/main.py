import random
import art
from data import data
import os

CELEB_A_FOLLOWER = 0
CELEB_B_FOLLOWER = 0
CELEB_A = {}
CELEB_B = {}


def compare(celeb_a, celeb_b):
    print(f"Compare A: {celeb_a['name']}, a/an {celeb_a['description']}, from {celeb_a['country']}.")

    print(art.vs)
    print(f"Against B: {celeb_b['name']}, a/an {celeb_b['description']}, from {celeb_b['country']}.")


def followers(a, b):
    if a > b:
        return "A"
    elif b > a:
        return "B"
    else:
        return "A"


def game():
    score = 0
    is_game_ended = False
    CELEB_A = random.choice(data)
    print(art.logo)
    while not is_game_ended:
        CELEB_B = random.choice(data)
        CELEB_A_FOLLOWER = CELEB_A['follower_count']
        CELEB_B_FOLLOWER = CELEB_B['follower_count']
        compare(CELEB_A, CELEB_B)
        winner = followers(CELEB_A_FOLLOWER, CELEB_B_FOLLOWER)
        ask = input("Who has more followers? 'A' or 'B'")
        if ask == winner:
            score += 1
            os.system('clear')
            print(art.logo)
            print(f"You're right! Current score: {score}.")
            if winner == "B":
                CELEB_A = CELEB_B
        else:
            os.system('clear')
            print(art.logo)
            print(f"Sorry, that's wrong. Final Score: {score}.")
            is_game_ended = True


game()
