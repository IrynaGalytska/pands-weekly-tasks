# The programme calculates a sequence of collats
# Avthor: Iryna Galytska
number=int(input("Please enter a positive integer: "))
if number>0:
    while number!=1:
        print(number,end=" ") 
        if number %2==0:
            number=number//2
        else:
            number=number*3+1
    print(number) # current value is one
else:
    print("Error: The number must be positive!")
   
