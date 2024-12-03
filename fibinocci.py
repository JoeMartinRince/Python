"""
AUTHOR: JOE MARTIN RINCE
DATE :3-12-2024

"""

def fibinocci(n):
    sequence=[]
    first_number=0
    second_number=1
    for _ in range(n):
        sequence.append(first_number)
        first_number,second_number=second_number,first_number+second_number
    return sequence

