# program asks user's name
# cash
# Y/N
# program checks if the user has more than or equal to $30

name = input("Enter your name:")
money = input("Enter your cash amount:")
hungry = input("Are you hungry? (Y/N)")

if hungry == "Y":
    if int(money) >= 30:
        print(f"{name} should go eat breakfast")
    else:
        print("Your money is not enough")
elif hungry == "N":
    print("You are not hungry")
else:
    print("Please make sure that you enter either Y or N")
