"""
AUTHOR : Joe Martin Rince
DATE: 28-10-2024
PYTHON PROGRAM FOR CALCULATING DISCOUNTS
"""
amount=float(input("Enter your amount:  "))
if amount>500 :
    amount=amount-amount*0.2
    print (amount)
elif amount >= 200 and amount< 500 :
    amount=amount-amount*0.1
    print (amount)
else:
    print (amount)
