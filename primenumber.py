"""
AUTHOR : Joe Martin Rince
DATE :29-10-2024
"""
n=int(input("Enter your number : "))
for i in range(2,(n//2)+1):
    if n %i==0:
        break
if i==(n//2):
    print(f"The given number {n} is prime")
else:
    print(f"The given number {n} is composite")