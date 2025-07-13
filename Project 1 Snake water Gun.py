import random

'''
1 for snake
-1 for water
0 for gun
'''
Computer = random.choice([-1, 0, 1])
youstr = input("Enter your choice: ")
youdict = {"s": 1, "w": -1, "g": 0}
reverseDict = {1: "Snake", -1: "Water", 0: "Gun"}


you = youdict[youstr]

#By now we have 2 numbers, you and computer

print(f"You Chose {reverseDict[you]}\nComputer chose {reverseDict[Computer]}")

if(Computer == you):
    print("Its a Draw!")

else:
    
    if(Computer == -1 and you == 1):
        print("You win!")

    elif(Computer == -1 and you == 0):
         print("You Lose!")

    elif(Computer == 1 and you == -1):
         print("You Lose!")

    elif(Computer == 1 and you == 0):
         print("You Win!")

    elif(Computer == 0 and you == -1):
        print("You Win!")

    elif(Computer == 0 and you == 1):
        print("You Lose!")

    else:
         print("Something Went Wrong")

