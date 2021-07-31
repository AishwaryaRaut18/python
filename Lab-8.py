def factorial(n):
    fact=1
    for i in range(1,n+1):
        fact=fact*i
    return fact

import sys
n=int(input("Enter number"))
if(n>0):
    for i in range(1,n+1):
        factor=factorial(i)
        print(i,factor)

else:
    print("Entered number is invalid")
