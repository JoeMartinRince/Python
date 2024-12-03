"""

AUTHOR : JOE MARTIN RINCE
DATE :3-12-2024
"""
def add_numbers(n1,n2):
    if n2==0:
        return n1
    else:
        return add_numbers(n1+1,n2-1)


add_numbers(5,4)

print(add_numbers(5,4))