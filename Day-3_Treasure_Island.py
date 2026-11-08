print("Welcome to Treasure Island.\nYour mission is to find the treasure.")

print("You're at a cross road. Where do you want to go?")
choice1 = input("\tType 'left' or 'right'\n")
if choice1 == "left":
    print("You've come to a lake. There is an island in the middle of the lake.")
    choice2 = input("\tType 'wait' to wait for a boat. Type 'swim' to swim across.\n")
    if choice2 == "wait":
        choice3 = input("Which door would you choose?  Red | Yellow | Blue\n")
        if choice3 == "yellow":
            print("You Won!")
        elif choice3 == "red" or choice3 == "blue":
            print("Game Over!")
    else:
        print("You fell into the river.\nGame Over")
else:
    print("Fall into a hole.\nGame Over!")                
            