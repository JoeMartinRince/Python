'''
Python program to find the fare of people visiting the zoo
AUTHOR : Joe Martin Rince
DATE : 15-10-2024
VERSION : 1.0
'''
age=float(input("Enter your age: "))
if age<10:
    print("Your ticket fare is 2$")
elif age >=10 and age<60:
    print("Your ticket fare is 5$")
else:
    print("Your ticket fare is 1$")