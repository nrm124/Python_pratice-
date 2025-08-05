import random
from queue import PriorityQueue

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''
game_images = [rock,paper,scissors]
you_choice = int(input('what do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.'))
if you_choice >=0 and you_choice <=2:
    print(game_images[you_choice])

computer_choose = random.randint(0,2)
print("Computer chose:")
print(game_images[computer_choose])




if you_choice >= 3 or you_choice < 0:
    print("you typed an invalid number")
elif  you_choice ==0 and computer_choose ==2:
    print("You win")
elif computer_choose > you_choice:
    print("You lose")
elif you_choice > computer_choose:
    print("you win!")
elif computer_choose == 0 and you_choice == 2:
    print("you lose")
elif you_choice == computer_choose:
    print("its Draw!")


#
# if you_choice == 0:
#     you_choice =rock
#     print(rock)
# elif you_choice == 1:
#     you_choice =paper
#     print(paper)
# elif you_choice == 2:
#     you_choice =scissors
#     print(scissors)
# else:
#     print("Alert : Invalid Selection ")
#
#
#
# random_computer_selection = [rock,paper,scissors]
# print("Computer Chose:")
# computer_chose = random.choice(random_computer_selection)
# print(computer_chose)
# if you_choice == computer_chose:
#     print("Its Draw")
# elif you_choice ==
#     print("you win")
# elif you_choice == "paper":
#     print("you win")
#
# else:
#     print("you lose")
#
