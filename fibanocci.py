N=int(input("Enter a range :"))
first_number=0
second_number=1
third_number=0
while(third_number <N):
    print(third_number , end=" ")
    third_number=first_number+second_number
    first_number = second_number
    second_number= third_number