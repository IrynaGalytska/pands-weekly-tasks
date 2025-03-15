# that the program tells the 
# user if there guess is too high or too low

import random
numberToGuess=random.randint(0,100)
guess=int(input("Please guess the number: "))
while guess!=numberToGuess:
    if numberToGuess>guess:
        print("Too low")
    else:
        print("Too high")
    guess=int(input("Please guess again:"))
print("Well done!Yes the number was",numberToGuess)