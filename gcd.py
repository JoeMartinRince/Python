"""
AUTHOR: JOE MARTIN RINCE
DATE:3-12-2024
"""
def gcd(n1,n2):
    if n1%n2==0:
        return n2
    else:
        return gcd(n2,n1%n2)

g=gcd(1029,255)
print(g)