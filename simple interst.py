"""
Python program to find the simple interest over a time period
Auther : Joe Martin Rince
Date : 15-10-2024
Version 1.0
"""
principle_amount=float(input("Enter the principle amount : "))
interest_rate=float(input("Enter the interest rate : "))
time_period=float(input("Enter the number of years : "))
simple_interest= principle_amount*interest_rate*time_period
print(f"The simple interest is : {simple_interest}")
