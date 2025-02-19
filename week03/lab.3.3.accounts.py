# create a Python account.
numberAccount=input("Please enter an 10 digit number: ")
if len(numberAccount) == 10 and numberAccount.isdigit():
    maskedAccount="xxxxxx"+ numberAccount[-4:]
    print(maskedAccount)
else:
    print("Error: Please enter a valid 10-digit account number.")  
