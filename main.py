import sys, random

assert sys.version_info >= (3,7), "This script requires at least Python 3.7"
 

range = 100

name = input("Hello there. What's your name? ")
print("A beautiful day isn't it " + name + "?")

quit = False

while not quit:
    randomNumber = random.randint(1, range)
    number = input("\nIf you would, please enter a number between 1-" + str(range) + ": ")
    range = int(range)
    print("The number you've guessed is: " + (number))
    if not number.isdigit():
        print("Please enter a real number. ")
    else:
        number = int(number)
        attempts = 1
        while (number) != randomNumber:
            print("I'm sorry, but you did not guess the number. Better luck next time!")
            if number > randomNumber:
                print("\nHint: You went too high!")
            elif number < randomNumber:
                print("\nHint: Your guess is too low!")
            number = input("\nPlease enter another number between 1-" + str(range) + ": ")
            range = int(range)
            number = int(number)
            print("You've attempted this same number " + str(attempts) + " times.")
            attempts = int(attempts)
            attempts = attempts + 1

print("Fantastic, you guessed the number!")
retry = input("\nWould you like to play again?")
retry = retry.lower()
if retry == "yes" or retry == "y":
    quit = False
else:
    quit = True
    print("Goodbye!")


print("\n\nThanks for playing. Have a good day " + name + "!")


               
