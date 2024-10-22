"""AUTHOR : JOE MARTIN RINCE
DATE:22/10/2024
VERSION: 1.0"""
num1=int(input("Enter your first number : "))
num2=int(input("Enter your second number : "))
num3=int(input("Enter your third number: "))
if num1>num2 and num1>num3 :
    print("Number 1 is the largest")
elif num2>num3 and num2>num1 :
    print("Number 2 is the largest ")
else:
    print("Number 3 is the largest")