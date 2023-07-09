"""
If you have three number and you need to know whice is bigger than the others, you can use my code.
"""

while(True):
    a = int(input("Input the first number:"))
    b = int(input("Input the second number:"))
    c= int(input("Input the third:"))
    if a > b and a > c :
        print("The biggest number is:",a)
        cevap = input("Do you want to continue ? ==> (y/N)")
        if cevap == "y":
            continue
        elif cevap == "N":
            break
    elif b > a and b > c:
        print("The biggest number is",b)
        cevap = input("Do you want to continue ? ==> (y/N)")
        if cevap == "y":
            continue
        elif cevap == "N":
            break
    else:
        print("The biggest number is",c)
        cevap = input("Do you want to continue ? ==> (y/N)")
        if cevap == "y":
            continue
        elif cevap == "N":
            break
