def sqrt(x):
    r = x / 2.0
    while abs(r * r - x) > 0.00001:
        r = (r + x / r) / 2.0
    return r



number =input("Please enter a positive number: ")
if number.lstrip("-").isdigit():
    number=float(number)
    if number <= 0:
        print("Only positive numbers are allow")
    else:
        result = sqrt(number)
        print(f"The square root of {number} is approx. {round(result, 1)}.")
else:      
    print("That was not a valid number.")

