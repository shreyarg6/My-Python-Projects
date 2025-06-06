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

import random

game_images = [rock, paper, scissors]

user_choice = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors. "))
if user_choice >= 0 and user_choice <= 2:
    print("You chose: " + game_images[user_choice])
comp_choice = random.randint(0, 2)
print("Computer chose: " + game_images[comp_choice])

if user_choice == 0 and comp_choice == 0:
    print("You tied!")
elif user_choice == 0 and comp_choice == 1:
    print("The computer won! Maybe next time!")
elif user_choice == 0 and comp_choice == 2:
    print("You won!")
elif user_choice == 1 and comp_choice == 0:
    print("You won!")
elif user_choice == 1 and comp_choice == 1:
    print("You tied!")
elif user_choice == 1 and comp_choice == 2:
    print("The computer won! Maybe next time!")
elif user_choice == 2 and comp_choice == 0:
    print("The computer won! Maybe next time!")
elif user_choice == 2 and comp_choice == 1:
    print("You won!")
elif user_choice == 2 and comp_choice == 2:
    print("You tied!")