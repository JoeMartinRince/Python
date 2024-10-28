"""
AUTHOR : Joe Martin Rince
DATE : 28-10-2024
PYTHON PROGRAM FOR SIMPLE TRAFFIC LIGHT SYSTEM
"""
colour=(input("Enter your colour :  "))
if colour == "Green" :
   print("Cars can go.")
elif colour == "Yellow":
   print("Cars should slow down")
elif colour == "Red" :
   print("Cars should stop ")
else:
   print("Invalid colour")
