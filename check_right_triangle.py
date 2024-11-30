"""
AUTHOR : Joe martin Rince
DATE:30-11-2024
"""
def is_check_right_triangle():
    sides=[side1,side2,side3]
    sides.sort()
    if sides[2]**2==sides[0]**2+sides[1]**2:
        return True
    return False

side1=int(input("ENTER SIDE1:"))
side2=int(input("ENTER SIDE2:"))
side3=int(input("ENTER SIDE3:"))

if is_check_right_triangle():
        print("THE GIVEN SIDES ARE PART OF A RIGHT TRIANGLE")
else:
        print("THE GIVEN SIDES ARE  NOT PART OF A RIGHT TRIANGLE")
is_check_right_triangle()