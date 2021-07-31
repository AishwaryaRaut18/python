#design a system which allows to maintain list of courses
import sys
data=[]
choice=0
while choice!=7:
    print("1. Accept data\n2. Delete data by values\n3. Delete data by position")
    print("4. Sort\n5. Reverse\n6. Print in sorted order ")
    print("7. Print in reverse order\n8. Display data")
    choice=int(input("enter choice"))
    if choice==1: #add data in the list
        print("""1. add at the end\n 2. add at the position """)
        ch=int(input("enter choice"))
        d=input("enter the data to add")
        if d in data:
            print("data exists")
        else: 
            if ch==1:
                data.append(d)
            else:
                pos=int(input("enter position"))
                data.insert(pos,d)
            print("data added",d)
                
                
    elif choice==2:
        print("1.delete from value")
        d=input("enter data to delete")
        if d in data:
              data.remove(d)
              print("course is removed",d)
        else:
              print("not found")

    elif choice==3:
        print("1.delete by position")
        pos=int(input("enter position"))
        data.pop(pos)
        print("data is removed from position",pos)
  
    elif choice==4: #sort
        print("1. Ascending order\n2. Descending order")
        c=int(input("enter choice"))
        if(c==1):
               ascendlist=data
               ascendlist.sort()
               print("sorting data in ascending order is done")     
        elif(c==2):
               descendlist=data
               descendlist.sort(reverse=True)
               print("sorting data in descending order is done")
        
     
    elif choice==5:#reverse
        reverselist=data
        reverselist.reverse()
       

    elif choice==6:
        print("ordered list= ",ascendlist or descendlist)

    elif choice==7:
         print("reverse list= ",reverselist)
    elif choice==8:
        print(data)
   
    elif choice==7:
        sys.exit(0)
    else:
        print("wrong choice")

