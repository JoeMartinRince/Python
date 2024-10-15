'''
Python program to check whether the given number
is positive or not
AUTHOR :Joe Martin Rince
DATE: 15-19-2024
VERSION:1.0
'''
number=int(input("Enter a number:"))
if number>0:
    print("The given number:",number," is positive")
elif number<0:
    print("the given number:", number, "is negative ")
else:
    print("The given number:", number, " is zero")