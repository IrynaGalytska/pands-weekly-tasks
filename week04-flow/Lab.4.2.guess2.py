# The program tells the user 
# if there guess is too high or too low

numberToGuess=30
guess=int(input("Please guess the number: "))
while guess!=numberToGuess:
    if numberToGuess>guess:
        print("Too low")
    else: # I know it cant be equal or too low,
        # so it must be too high
        print("Too high")
    guess=int(input("Please guess again:"))
print("Well done!Yes the number was",numberToGuess)