
import random
import art

def deal_card():
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    card = random.choice(cards)
    return card

def calculate_score(card_input):
        if 11 in card_input and 10 in card_input and len(user_cards) == 2:
            return 0
        if 11 in card_input and sum(card_input) > 21:
            card_input.remove(11)
            card_input.append(1)
        return sum(card_input)

def compare(user_score1, computer_score1):
    if computer_score1 and user_score1 == 0:
        return "Its Draw!"
    elif computer_score1 == 0 :
        return  "Lose, Computer has Black jack"
    elif user_score1 ==0:
        return "You win!, with a black jack"
    elif user_score1 >21:
        return "Lose! went over "
    elif computer_score1 > 21:
        return "you win!, computer went over"
    elif user_score1 > computer_score1:
        return "You win"
    else:
        return "you lose"

def play_game():
    print(art.logo)
    user_cards = []
    computer_cards = []
    is_game_over = False
    computer_score = -1
    user_score = -1

    for card in range(2):
        user_cards.append(deal_card())
        computer_cards.append(deal_card())

    while not is_game_over:
        user_score = calculate_score(user_cards)
        computer_score = calculate_score(computer_cards)

        print(f"Your cards : {user_cards} , current score {user_score}")
        print(f"Computer's first card:{computer_cards[0]}")

        if user_score ==0 or user_score>21 or computer_score == 0:
            print("Game over ")
            is_game_over = True
        else:
            another_card = input("Type 'y' to get another card, type 'n' to pass").lower()
            if another_card == "y":
                user_cards.append(deal_card())
            else:
                is_game_over = True



    while computer_score != 0 and computer_score < 17:
        computer_cards.append(deal_card())
        computer_score = calculate_score(computer_cards)
    print(compare(user_score,computer_score))

while input("do you want play a black jack again type'y' or 'n' ") =='y':
    play_game()
    print("\n" * 20)
    play_game()