"""
If you need to know a number able to divide another number you can use this code to figure it out.
"""

A = int(input("Input a number==> "))
B = int(input("Input a number==> "))

if A%B==0:
    print("B can divide A to integer number.")
else:
    print("B cannot divide A to integer number.")
