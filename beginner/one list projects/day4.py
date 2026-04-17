#rock scissors paper game
import random

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
game_images = [rock, paper, scissors]

players_choice = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n"))
print(game_images[players_choice])

computers_choice = random.randint(0, 2)
print("Computer chose:")
print(game_images[computers_choice])

if players_choice >= 3 or players_choice <0:
    print("You typed an invalid number. You lose")
elif players_choice == computers_choice:
    print("It's a draw")
elif computers_choice > players_choice:
  print("You lose")
elif players_choice > computers_choice:
  print("You win!")