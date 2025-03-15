# This program read in 
# a students percentage
# and prints out the
# corresponding grade

while True:
    percentage=round(float(input("Enter the percentage: ")))
# print (precentage)
# be careful with and ors
    if percentage==-1:
        print("Finish students")
        break
    elif percentage<0 or percentage>100:
        print("Please enter a number beetwen 0 and 100")
    elif percentage <40:
        print("Fail")
    elif percentage <50:
        print("Pass")
    elif percentage<60:
        print("Meritl")
    elif percentage<70:
        print("Merit2")
    else:
        print("Distinction")