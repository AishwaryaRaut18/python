def addcity():
    name=str(input("enter name of city"))
    v=city.get(name,-1)
    if v==-1:
        n=int(input("enter tree list size"))
        print("enter trees")
        for i in range(0,n):
            tree=str(input())
            city.setdefault(name,[]).append(tree)
        return 1
    else:
            return 2
      
        
def deletecity(name):
    v=city.get(name,-1)
    if v!=-1:
        print(name,v)
        ch=input("are you sure ?(y/n)")
        if ch=="y":
            v=city.pop(name,-1)
            return 0
        else:
            return 1
    else:
        return 2


def modifycity(name):
    val_list=list(city.values())
    v=city.get(name,-1)
    if v!=-1:
        print(name,v)
        city.setdefault(name,[]).clear()
        ch=input("are you sure ?(y/n)")
        if ch=="y":
            n=int(input("enter tree list size"))
            for i in range(0,n):
                tree=input()
                city.setdefault(name,[]).append(tree)
            return 0
        else:
            return 1
    else:
        return 2

def display_all():
    print(city)
        
def displaytreeBycity(name):   
   print(city.get(name))

def displaycityBytree(tree):   
    key_list=list(city.keys())
    val_list=list(city.values())
    for i in val_list:
        for j in i:
           position=val_list.index(i)
    print(key_list[position])
        

import sys    
city={}
modify=[]
choice=0
while choice!=7:
    print("1. add new city and tree\n2. display all cities and the list of trees for all cities\n3. display list of trees of a particular city")
    print("4. display cities which have given tree\n5. delete city")
    print("6. modify tree list\n7. exit")
    choice=int(input("enter choice"))
    if choice==1:
        ans=addcity()
        if ans==1:
            print("city added")
        elif ans==2:
            print("city exists")

    elif choice==2:
        display_all()

    elif choice==3:
        name=(input("enter name"))
        displaytreeBycity(name)

    elif choice==4:
        tree=(input("enter tree"))
        displaycityBytree(tree)

    elif choice==5:
        name=input("enter city name")
        ans=deletecity(name)
        if ans==0:
            print("city deleted")
        elif ans==1:
            print("city exists, not deleted")
        else:
            print("not found")

    elif choice==6:
        name=input("enter name")
        ans=modifycity(name)
        if ans==0:
            print("city modify")
        elif ans==1:
            print("trees exists, not modified")
        else:
            print("not found")

    elif choice==7:
        sys.exit(0)

    else:
        print("wrong choice")
