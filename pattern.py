"""
AUTHOR : Joe Martin Rince
DATE: 19-11-2024
"""


# PATTERN 1
limit=int(input("Enter a limit : "))

for  i in range(0,limit):
    for j in range(i+1):
        print("*",end="")

    print()
print("  ")

#PATTERN 2

for  i in range(limit,0,-1):
    for j in range(i):
        print("*",end="")
    print()

#PATTERN 3

for i in range(1,limit+1):
    for j in range(limit-i):
        print(" ",end=" ")
    for k in range(2*i-1):
        print("*",end=" ")
    print()
print()

#PATTERN 4

for i in range(limit,0,-1):
    for j in range(limit-i):
        print(" ",end=" ")
    for k in range(2*i-1):
        print("*",end=" ")
    print()