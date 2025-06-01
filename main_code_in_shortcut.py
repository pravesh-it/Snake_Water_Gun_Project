import random

computer = random.choice([-1, 0, 1])
youstr = input("Enter your choice: ")
youDict = {"snake": 1, "water": -1, "gun": 0}
reverseDict = {1: "snake", -1: "water", 0: "gun"}

you = youDict[youstr]
print(f"Your chose: {reverseDict[you]}\nComputer chose: {reverseDict[computer]}")
    
if(computer == you):
        print("It's a Draw")

if((computer - you) == -1 or (computer - you) == 2 ):
    print("You Lose!")

else:
    print("You Win!")

'''
The below logic is written on the basis of the value of the computer - you.

if(computer == -1 and you == 1): = -2
            print("You Win")
        
        elif(computer == -1 and you == 0): = -1
            print("You Lose")

        elif(computer == 1 and you == -1): = 2
            print("You Lose")

        elif(computer == 1 and you == 0): = 1
            print("You Win")
    
        elif(computer == 0 and you == -1): = 1
            print("You Win")
    
        elif(computer == 0 and you == 1): -1
            print("You Lose")
'''