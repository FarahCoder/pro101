import random

answer = "y"


while answer == "y":
    n = random.randint(1,6)

    if n == 1:
        print("-----")
        print("     ")
        print("  0  ")
        print("     ")
        print("-----")

    if n == 2:
        print("-----")
        print("0    ")
        print("     ")
        print("   0 ")
        print("-----")

    if n == 3:
        print("-----")
        print("0    ")
        print("  0  ")
        print("    0")
        print("-----")

    if n == 4:
        print("-----")
        print("0   0")
        print("     ")
        print("0   0")
        print("-----")

    if n == 5:
        print("-----")
        print("0   0")
        print("  0  ")
        print("0   0")
        print("-----")

    if n == 6:
        print("-----")
        print("0   0")
        print("0   0")
        print("0   0")
        print("-----")

    answer=input("Would you like to roll a dice? {y or n} ")

    print("\n")
