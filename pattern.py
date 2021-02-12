while True:
    inp = int(input("0 or 1: "))
    if (inp == 0) or (inp == 1):
        break


n = int(input("Enter number of rows: "))

def boolconverter(a):
    """This function is used to convert an integer to a boolean.
It will convert 0 to True and 1 to false."""

    if a == 0:
        return True
    elif a == 1:
        return False

boolconverted = boolconverter(inp)

if boolconverted == True:
    for r in range(1, n + 1):
        print(r * "*")
        r += 1

elif boolconverted == False:
    for r in range(n, 0, -1):
        print(r * "*")
        r += 1
