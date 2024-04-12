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

game_images=[rock, paper, scissors]
print("Welcome to the Rock Paper Scissors Contest sponsored by the THE ROCK PAPER SCISSORS ASSOCIATION")
player_choice=int(input("What do you choose? Type 0 for Rock ,1 for Paper or 2 for Scissors\n"))
if  player_choice>=3 or player_choice<0 :
    print("You have entered an invalid number")
else:
    print(f"You Chose: {game_images[player_choice]}")
    computer_choice = random.randint(0, 2)
    print(f"Computer Chose: {game_images[computer_choice]}")


    if player_choice == 0 and computer_choice == 2:
        print("You Win!!!")
    elif player_choice == 2 and computer_choice == 0:
        print("You Lose")
    elif computer_choice > player_choice:
        print("You Lose")
    elif computer_choice < player_choice:
        print("You Lose")
    elif computer_choice == player_choice:
        print("The match is tied")


















