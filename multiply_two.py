"""
AUTHOR:JOE MARTIN RINCE
SATE:3-12-2024

"""
def multiply_two_numbers(n1,n2):
    if n2==1:
        return n1
    else:
        return n1+multiply_two_numbers(n1,n2-1)

t=multiply_two_numbers(5,4)
print(t)