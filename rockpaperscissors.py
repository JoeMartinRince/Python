"""
AUTHOR: JOE MARTIN RINCE
DATE :18-11-2024
"""


import random

text = "You Lose!"
choices = ["rock", "paper", "scissors"]

while True:
    
        num = int(input("Enter 0 for rock, 1 for paper, and 2 for scissors: "))
        
       
        if num < 0 or num > 2:
            print("Invalid response. Please enter 0, 1, or 2.")
            continue
        
        no = random.randint(0, 2)
        print(f"Computer choice: {choices[no]}")

        
        if num == no:
            print("Tie")
        elif (num == 0 and no == 2) or (num == 1 and no == 0) or (num == 2 and no == 1):
            print("You Win!")
        else:
            print(text)
  
