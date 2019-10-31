# Program that will generate a random number and allow user to guess
# 10/31/19
# CTI-110 P5HW1 - Random Number
# Elizabeth Johnson

def main():
    menu()
    print()
    choice = input("What would you like to do? ")
    print()
    while choice != '2':
        if choice == '1':
            randomNumber()
            print("---------------------")
            print()
            menu()
            print()
            choice = input("What would you like to do? ")
        else:
            print('That is not an option.')
            print()
            menu()
            print()
            choice = input("What would you like to do? ")
    print()
    print('Goodbye.')






def menu():
    print("      Main Menu      ")
    print("---------------------")
    print("1. Random Number Game")
    print("2. Exit")

def randomNumber():
    import random
    number = random.randint(1, 100)
    print('I have chosen a random number from 1-100. Try and guess it!')
    guess = int(input())
    print()
    while guess != number:
        if guess > number:
            print('The number is lower than that. Try again.')
            guess = int(input("Guess again:" ))
            print()
        else:
            print('The number is higher than that. Try again.')
            guess = int(input("Guess again: "))
            print()
    print('Congrats! You have guessed the number correctly!')
    print()

main()
        
