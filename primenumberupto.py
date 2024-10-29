"""
AUTHOR : Joe Martin Rince
DATE :29-10-2024
"""
limit =int(input("Enter your limit: "))
for number in range(2,limit+1):
    isprime=True
    for i in range(2,(number//2)+1):
        if number%i==0:
            isprime=False
            break
    if isprime:
        print(number,end=" ")