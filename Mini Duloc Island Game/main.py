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
''')

print("Welcome to Duloc Island.")
print("Your mission is to find the treasure!") 

choice1 = input("You have arrived on the island! Would you like to go left or right? Type 'left' or 'right'. ")
if choice1 == "left":
    choice2 = input("You have arrived at a swamp. Would you like to swim or go around? Type 'swim' or 'go around'. ")
    if choice2 == "go around":
        choice3 = input("You have arrived at a portal with three doors. Which door would you like to go through? Type 'red', 'blue', 'yellow', or 'whatever' if you don't want any door. ")
        if choice3 == "red":
            print("You got eaten. Game Over!") 
        elif choice3 == "yellow":
                print("You've found the dragon's lair and all her treasure!")    
        elif choice3 == "blue":
                print("You fell in love with Robin Hood and ran away from the treasure! Game over!")
        else:
                print("You got stuck in a magic mirror forever! Game Over!") 
                exit()
    else:
        print("You got sat on by Shrek! Game Over!")
        exit()
else:
    print("You have fallen into a rabbit hole. The game is over.")
    exit()