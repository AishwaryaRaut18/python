lst=[]
new=[]

n=int(input("enter size of list"))
print("enter element")
for i in range(0, n):
    ele=int(input())
    lst.append(ele)

for i in range(0,max(lst)+1):
    if i in lst:
       val=lst.index(i)
       new.insert(i,val)
    else:
       new.insert(i,-1)
print(new)