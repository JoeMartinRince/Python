"""
AUTHOR : Joe Matin Rince
DATE: 14-11-2024
"""
import random
l=int(input("Enter your largest number : "))
s=int(input("Enter your smallest number : "))
guess=random.randint(s,l)
no_of_tries=0

while True:

    user_input = int(input("Enter your guess : "))
    if guess > user_input:
        print("Too small , enter a larger number")

    elif guess < user_input:
        print("Too large ,enter a smaller number")

    else:
        print("Yay, You got it")
        break
    no_of_tries+=1
print(no_of_tries)