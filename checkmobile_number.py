"""
AUTHOR : Joe Martin Rince
Bate : 30-11-2024
"""
number1=input("Enter a number :")
def check_number():
    if len(number1)==10 and number1[0]=="9" or number1[0]=="7" or number1[0]=="8":
        print("valid number ")
    else:
        print("Invalid number")

check_number()
