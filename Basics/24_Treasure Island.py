print('''    
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************
''')  #we have used three single quotes coz it allows us to do multiple lines of string
print('''Welcome to Treasure Island.''')
print("Your mission is to find the treasure.")
a=input('You\'re at a cross road. Where do you want to go? Type "Left" or "Right" ').lower()
if a =="right":
    b = input('You\'re infront of a lake.What do you want to do? Type "Swim" or "Wait" ').lower()
    if b=="wait":
        c = input(
            'You\'re infront of three doors which lead to diffrent places.Which color door do you want to open? Type "Red" or "Blue" or "Yellow" ').lower()
        if c=="yellow":
            print("HURRAY! YOU WON")
        elif c=="red":
            print("A hungry lion attacked you.GAME OVER")
        elif c=="blue":
            print("It was a gas chamber. GAME OVER")
    else:
        print("The Waters where infested with crocodiles.GAME OVER")
else:
    print("ALAS! You fell into a hole.GAME OVER")



