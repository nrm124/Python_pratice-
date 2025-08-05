import random


EASY_ATTEMPT =10
HARD_ATTEMPT =5

def check_answer (g_number,a_number,turn):
    if g_number > a_number:
        print("To High")
        return turn- 1
    elif g_number <a_number:
        print("To Low")
        return turn -1
    else:
        print(f"you got it! the answer is {a_number}")




def difficulty():
    level = input("difficulty levek 'hard ' or 'easy '").lower()
    if level =='easy':
        return EASY_ATTEMPT
    else:
        return HARD_ATTEMPT


def game():
    print("Welcome to the Number Guessing Game! \n" 
          "I'm thinking of a number between 1 and 100.")
    answer = random.choice(list(range(1,101)))
    turns = difficulty()

    guess = 0
    while guess != answer:
        print(f"You have {turns} attempts remaining to guess the number")
        guess =int(input("Make a guess :"))
        turns = check_answer(guess,answer,turns)
        if turns == 0:
            print("you are out of guesses!")
            return


game()