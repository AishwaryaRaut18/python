list_of_list=[[] for i in range (0,10)]
ch='t'
while ch=='t':
 i=int(input("enter number"))
 n=i%10
 list_of_list[n].append(i)
 print(list_of_list)
 print("do you want to continue (t/f)")
 ch=input()
