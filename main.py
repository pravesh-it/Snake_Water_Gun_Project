'''
Snake Water Gun Game.

1 for snake
-1 for water
0 for gun

'''
import random

computer = random.choice([-1, 0, 1])
youstr = input("Enter your choice: ")
youDict = {"snake": 1, "water": -1, "gun": 0}
reverseDict = {1: "snake", -1: "water", 0: "gun"}

try:
    you = youDict[youstr]
    
    print(f"Your chose: {reverseDict[you]}\nComputer chose: {reverseDict[computer]}")
    
    if(computer == you):
        print("It's a Draw")
    
    else:
        if(computer == -1 and you == 1):
            print("You Win")
        
        elif(computer == -1 and you == 0):
            print("You Lose")

        elif(computer == 1 and you == -1):
            print("You Lose")

        elif(computer == 1 and you == 0):
            print("You Win")
    
        elif(computer == 0 and you == -1):
            print("You Win")
    
        elif(computer == 0 and you == 1):
            print("You Lose")
        
        else:
            print("Something went wrong")

except KeyError:
    print("Invalid choice. Please enter snake, water or gun.")