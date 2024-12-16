"""
AUTHOR : JOE MARTIN RINCE
DATEC:14-11-2024
Simple desktop calculator using Python. Only the five basic arithmetic operators.
"""
from itertools import product

num1=int(input("Enter your number 1 : "))
num2=int(input("Enter your number 2 :"))
operation=input("Enter your operation , '+' , '_' , '*' or '/': ")
if operation == '+':
    sum1=(num1+num2)
    print(sum1)
elif operation=='_':
    difference=(num1-num2)
    print(difference)
elif operation=='*':
    product1=(num1*num2)
    print(product1)
elif operation=='/':
    quotient=(num1/num2)
    print(quotient)
else :
    print("wrong operation")
