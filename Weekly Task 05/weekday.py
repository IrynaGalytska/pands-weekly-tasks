import datetime

x = int(datetime.datetime.now().strftime("%w"))
if x==0 or x==6:
    print("It is the weekend, yay!")
else:
    print("Yes, unfortunately today is a weekday.")



