import random
from art import logo

number = random.randint(1, 100)
GUESS_LEFT_EASY = 10
GUESS_LEFT_HARD = 5
GUESS_LEFT_LIMITLESS = 999999999


# To test
# print(number)
def set_difficulty():
    difficulty = input("Choose a difficulty. Type 'easy', 'hard' or 'limitless': ")
    if difficulty == "easy":
        return GUESS_LEFT_EASY
    elif difficulty == "hard":
        return GUESS_LEFT_HARD
    elif difficulty == "limitless":
        return GUESS_LEFT_LIMITLESS


print(logo)
print("Are you ready to Guess the Number?\nI'm thinking a number between 1 and 100")
guess_left = set_difficulty()
print(f"You have {guess_left} attempts left")

while guess_left > 0:
    guess = int(input("Make a guess: "))
    if guess == number:
        if guess_left < 10:
            print(f"We have a winner!! The answer was {number}")
        else:
            print(f"Good for you. The answer was {number} now play like a normal person and choose easy or hard")
        break
    elif guess > number:
        guess_left -= 1
        print(f"Too high.\n Guess again.\nYou have {guess_left} attempts left")
    else:
        guess_left -= 1
        print(f"Too low.\n Guess again.\nYou have {guess_left} attempts left")

if guess_left == 0:
    print(f"Aww was it too hard for you? :( The number was {number}")
