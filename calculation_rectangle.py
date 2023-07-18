while True:
    x = float(input("Enter long side: "))
    y = float(input("Enter short side: "))
    if x<y:
        print("Please enter the properly.")
        continue
    elif x == y:
        print("Sides cannot be equal")
        continue
    else:
        break

area = (x*y)
perimeter = (x+y)
print(f"area:{area}\n perimeter:{perimeter}")
