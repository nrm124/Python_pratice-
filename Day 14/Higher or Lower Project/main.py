import random
import game_data
players = (game_data.data)

score = 0

def compare(n1,n2,s_score):
    if n1 > n2:
        s_score +=1
    else:
        print(f"Sorry, that's wrong. Final score: {s_score}")

def generate_two_player(player_data):
    first_player = random.choice(player_data)
    second_player =random.choice(player_data)
    if first_player == second_player:
        second_player =random.choice(player_data)
    return first_player,second_player

def generate_player(player_data):
    third_player = random.choice(player_data)
    return third_player

a_player , b_player = generate_two_player(players)

c_player = generate_player(players)
for player in a_player['name']and b_player['name']:
    if player['name'] == a_player['name']:
        c_player =random.choice(players)
    elif player['name'] == b_player['name']:
        c_player = random.choice(players)
    else:
        c_player = c_player
a_player_followers = a_player['follower_count']
b_player_followers = b_player['follower_count']
print(c_player)

# print(a_player_followers,b_player_followers)
#
# print(compare(a_player_followers,b_player_followers,score))
print(f"Compare A: {a_player['name']}, {a_player['description']}, from {a_player['country']} ")
print(f"Against B: {b_player['name']}, {b_player['description']}, from {b_player['country']} ")
selected = input("Who has more followers? Type 'A' or 'B':").lower()
#
should_contuie = True
while should_contuie :

    if selected == 'a':
            (compare(a_player_followers,b_player_followers,score))
            (compare(b_player_followers,))
    elif selected == 'b':
            (compare(b_player_followers,a_player_followers,score))


























# def compare(list,s_score):
#     for player in list:
#     if list[0] > s_player:
#         s_score +=1
#         return s_score
#     else:
#         print(f"Sorry, that's wrong. Final score: {s_score}")





