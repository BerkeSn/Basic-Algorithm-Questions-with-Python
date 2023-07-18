a = int(input("Enter a number: "))
liste = []

for i in range(1,a+1):
    if a%i==0:
        liste.append(i)
        i+=1
    
if len(liste)>2:
    print(f"The entered number is not prime number.\t These are dividers: {liste}")
else:
    print(f"The entered number is a prime number .\t {liste}")
  
