#program that reads in two numbers and
#outputs the ihteger answer and remainder
x=int(input("Enter first number: "))
y=int(input("Enter second number: "))
answer=int(x//y) # gives the int division
remainder=x%y # % gives the remainder
print("{} divider by {} is {} with remainder {} ".format(x, y, answer, remainder))

