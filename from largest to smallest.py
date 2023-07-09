"""
If you need to sort from largest to smallest there is two way. First way is long way, I found it when I start coding. It is very long and repeat itself. Due to that I do not recommend it.
But the second way is very short and do not repeat itself, it is very useful.
"""
# First way
a = float(input("Input the first number:"))
b = float(input("Input the second number:"))
c= float(input("Input the third number:"))

if a > b and a > c :
    if b > c:
        print(a,">",b,">",c)
    elif c>b:
        print(a,">",c,">",b)
    else:
        print(a,">",b,"=",c)
elif b > a and b > c:
    if a>c:
        print(b,">",a,">",c)
    elif c>a:
        print(b,">",c,">",a)
    else:
        print(b,">",c,"=",a)
elif c>a and c>b:
    if a > b:
        print(c,">",a,">",b)
    elif b > a:
        print(c,">",b,">",a)
    else:
        print(c,">",b,"=",a)
elif a==b:
    if a>c:
        print(a,"=",b,">",c)
    elif a<c:
        print(c,">",b,"=",a)
    else:
        print(a,"=",b,"=",c)
elif a==c:
    if a>b:
        print(a,"=",c,">",b)
    elif a<b:
        print(b,">",a,"=",c)
    else:
        print(a,"=",b,"=",c)
elif b==c:
    if b>a:
        print(b,"=",c,">",a)
    elif b<a:
        print(a,">",b,"=",c)
    else:
        print(a,"=",b,"=",c)
# The second way
a = float(input("Input the first number: "))
b = float(input("Input the second number: "))
c = float(input("Input the third number: "))

largest = max(a, b, c)
smallest = min(a, b, c)
middle = (a + b + c) - (largest + smallest)

print("Sorting from largest to smallest: ", end="")
if a == b == c:
    print(a, "=", b, "=", c)
elif a == b or a == c or b == c:
    if a == b:
        print(largest, "=", middle, ">", smallest)
    elif a == c:
        print(largest, ">", middle, "=", smallest)
    else:
        print(largest, ">", middle, "=", smallest)
else:
    print(largest, ">", middle, ">", smallest)
