from random import randint
from guess import logo
EASY_LEVEL_TURNS=10
HARD_LEVEL_TURNS=5



# Function to check user guess with selected number
def check_answer(guess,answer,turns):
    print(logo)
    """Checks answers against guess.Returns number of turns remaining"""
    if guess>answer:
        print("Too High")
        return turns-1
    elif guess<answer:
        print("Too Low")
        return turns-1
    else:
        print(f"You got it! The answer was {answer}")




# Make fucntion to set difficulty
def set_difficulty():
    level=input("Choose a difficulty. Type 'easy' or 'hard':")
    if level=='easy':
        return EASY_LEVEL_TURNS
    else:
        return HARD_LEVEL_TURNS




def game():
    # Choosing a random number between 1 and 100
    print("Welcome to the Number Guessing Game!")
    print("I'm thinking of a number between 1 and 100.")
    answer = randint(1, 100)
    turns=set_difficulty()


    # Repeat the guessing fucntionality if they get it wrong.
    # Let the user guess a number
    guess=0
    while guess!=answer:
        print(f"You have {turns} attempts remaining to guess the number.")
        guess = int(input("Make a guess:"))
        turns=check_answer(guess,answer,turns)
        if turns==0:
            print("You have run out of guesses.You Lose!!")
            return  #stops the proogram
        elif guess!=answer:
            print("Guess Again")
game()





# Track the number of turns and reduce by 1 if they got it wrong


