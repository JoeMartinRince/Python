limit=int(input("Enter your limit :"))
num=int(input("Enter your number : "))
smallest=num
largest=num
for i  in range (1,limit):
    num=int(input("Enter a number : "))
    if num<smallest:
        smallest=num
    elif num > largest:
        largest = num
print(f"The largest number is {largest}")
print(f"The smallest number is {smallest}")




