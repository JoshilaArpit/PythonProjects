import random
guess = 0
num = random.randint(1, 101)

while guess < 9:
    inp = int(input("Enter a number"))
    if inp == num:
        print("You win!")
        break

    elif inp < num:
        print("The correct number is larger than your input")
        guess += 1
        print("You have ", (9 - guess), " tries left")
        if guess == 9:
            print("You lost!")
            print("The correct  number is", num)
            break

    else:
        print("The correct number is smaller than your input")
        guess += 1
        print("You have ", (9 - guess), " tries left")
        if guess == 9:
            print("You lost!")
            break