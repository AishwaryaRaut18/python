import sys
a = set()
b = set()
n=int(input("enter set size"))
for i in range(0,n):
    ele=input()
    a.add(ele)
choice=0
while choice!=7:
 print("1.delete elemnet if exits otherwise do not show any error")
 print("2.add a element")
 print("3.create one more set")
 print("4.union of 2 sets")
 print("5.difference of 2 sets")
 print("6.convert set into frozenset")
 print("7.exit")
 choice=int(input("enter choice"))
 if choice==1:
    delete=input("enter element you want to delete")
    a.discard(delete) # will delete if found and ignore if not found
    print(a)

 elif choice==2:
    ele=input("enter element you want to add")
    a.add(ele) 
    print(a)

 elif choice==3:
    n1=int(input("enter set size"))
    for i in range(0,n1):
       b.add(input())
    
 elif choice==4:
     #union
     #print(a.union(b))
     print(a|b)

 elif choice==5:
    #print(a.difference_update(b))
    print(a-b,b-a)
    #a=a-b
    #print(a)

 elif choice==6:
    c=frozenset(a)
    d=frozenset(b)
    print("first set to frozenset: ",c)
    print("second set to frozenset: ",d)

 elif choice==7:
    sys.exit()

 else:
    print("wrong choice")


