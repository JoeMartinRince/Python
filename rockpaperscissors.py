"""
AUTHOR: JOE MARTIN RINCE
DATE :18-11-2024
"""
import random

text="You Lose !"
choices=["rock","paper","scissors"]
while True:
    num=int(input("Enter 0 for rock, 1 for paper, and 2 for scissors:  "))
    no=random.randint(0,2)
    print(f"Computer choice : {choices[no]}")
    if num>2 or num<0:
    print ("Invalid response ")

    elif choices[num]==0 and choices[no]==1:
        print(text)
    elif choices[num]==1 and choices[no]==2:
        print(text)
    elif choices[num]==2 and choices[no]==0:
        print(text)
    elif choices[num]==choices[no]:
        print("Tie")
    else:
        print("You Win!")