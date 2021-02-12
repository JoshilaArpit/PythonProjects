import random
swg = ['s', 'w', 'g']
i = 0
compwinner = 0
humanwinner = 0

while i < 9:
    comp = random.choice(swg)
    inp = input("s, w or g ?")
    #if computer chooses snake
    if comp == 's':
        print("Mine was s.")
        if inp == 's':
            pass
        elif inp == 'w':
            compwinner += 1
        elif inp == 'g':
            humanwinner += 1
        else:
            print("Invalid Input!")
            pass

    elif comp == 'w':
        print("Mine was w.")
        if inp == 's':
            humanwinner += 1
        elif inp == 'w':
            pass
        elif inp == 'g':
            compwinner += 1
        else:
            print("Invalid Input!")
            pass
    #if computer chooses gun
    else:
        print("Mine was g.")
        if inp == 's':
            compwinner += 1
        elif inp == 'w':
            humanwinner += 1
        elif inp == 'g':
            pass
        else:
            print("Invalid Input!")
            pass
    i += 1

if compwinner > humanwinner:
    print(f"You lost this by {compwinner}, {humanwinner}.")
elif compwinner < humanwinner:
    print(f"You won this by {humanwinner}, {compwinner}.")
else:
    print(f"This was a draw! You both got {humanwinner} points.")