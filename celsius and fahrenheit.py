"""AUTHOR: JOE MARTIN RINCE
DATE:22/10/2024
VERSION:1.0"""
t=int(input("Enter your temperature:  "))
unit=input("Is this 'C' or 'F': ")

if unit=='C':
    f=(9/5 *t)+32
    print("Your temperature is ",f)
else:
   c=5/9 * (t-32)
   print("Your temperature is ",c)