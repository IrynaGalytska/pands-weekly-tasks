# This program reads in a string and strips
# any leading or trailing spaces.
# It also converts all the letters to lowercase.
# Then, It outputs the lengths of the original string
# and the normalised one

# Author: Iryna Galytska
rawString=input("Please enter a string: ")
normalisedString=rawString.strip().lower()
lenghtOfRawString=len(rawString)
lenghtOfNormalised=len(normalisedString)
print(f"That String normalised is :{normalisedString}")
print(f"we reduced the input string from {lenghtOfRawString} to {lenghtOfNormalised} characters")

