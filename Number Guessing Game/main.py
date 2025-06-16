from random import randint
from art import logo
EASY_LEVEL_TURNS = 10
HARD_LEVEL_TURNS = 5

turns = 0


# Function to check users' guess against actual answer
def check_answer(user_guess, actual_answer, turns):
    if user_guess > actual_answer:
        print("Too high! Guess again!")
        return turns - 1
    elif user_guess < actual_answer:
        print("Too low! Guess again!")
        return turns - 1
    else: 
        print(f"You guessed it! The answer was {actual_answer}")

# Function to set difficulty
def set_difficulty():
    level = input("Choose a difficulty. Type 'easy' or 'hard': ")
    if level == "easy":
        return EASY_LEVEL_TURNS
    else:
        return HARD_LEVEL_TURNS

def game():
    print (logo)
    # Choosing a random number between 1 and 100
    print("This is the Number Guessing Game!")
    print("Guess the Number I'm thinking of from 1 - 100!")
    answer = randint(1, 100)
    # print(f"The correct answer is {answer}. Maybe next time!")


    turns = set_difficulty()

    # Repeat the guessing functionality if they get it wrong
    guess = 0
    while guess != answer:
        print(f"You have {turns} attempts remaining to guess the number.")
        # Let the user guess a number
        guess = int(input("What's your guess?: "))
        # Track the number of turn sand reduce by 1 if they get it wrong
        turns = check_answer(guess, answer, turns)
        if turns == 0:
            print("You don't have any guesses left! You lose! Try again!")
            return turns
        elif guess != answer:
            print("Guess again!")

game()