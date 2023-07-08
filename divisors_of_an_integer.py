"""
If you need to calculate divisors of an integer numbers you can use my code.
"""

A = int(input("Input an integer number==> "))
list=[]
for i in range(1,A+1):
    if A%i==0:
        list.append(i)
print(A," list of divisors of A:", list)
