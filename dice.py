# a = random.random() * 100  # *100 for getting random number in 0 to 100
# #random numbers (rational/irrational etc) between 0 and 1
# print(a)
import random
dice = []
for i in range(1, 7):
    dice.append(i)

while True:
    num = random.choice(dice)
    print(num)
    choice = input("Again ? (y/n) ")
    if choice == "y" or choice == "Y":
        pass
    elif choice == "n" or choice == "N":
        print("Thank You!")
        break
    else:
        print("Invalid input!\n")
        break
