import sys
lst=[]
k=0
n=int(input("enter number of elements"))
print("enter elements")
for i in range(0,n):
    ele=int(input())
    lst.append(ele)
    
for j in range(0,n):
    while k < lst[j]:
        sys.stdout.write("*")
        k=k+1
    k=0
    print("")
    
