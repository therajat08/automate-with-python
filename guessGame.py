# program to guess the number correctly

import random

secretNumber = random.randint(1,20)

print("In this game you get 6 chances")

for guessTaken in range(1,7):
    print("Enter a number between 1 and 20")
    num = int(input())
    if num < secretNumber:
        print("Your guess was too low")
    elif num > secretNumber:
        print("Your guess was too high")
    else:
        print("Well done you got the right answer in " + str(guessTaken) +" guesses")
        break

if num != secretNumber:
    print("Sorry you have used all of your chances")
    print("the number i was thinking was "+ str(secretNumber))


