def addperson():
    name=str(input("enter name of person"))
    vehicle=str(input("enter vehicle"))
    v=person.get(name,-1)
    if v==-1:
        person[name]=vehicle
        return 1
    else:
        ch=input("overwrite???")
        if ch=="y":
            person[name]=vehicle
            return 2
        else:
            return 3
        
def deleteperson(name):
    v=person.get(name,-1)
    if v!=-1:
        print(name,v)
        ch=input("are you sure ?(y/n)")
        if ch=="y":
            v=person.pop(name,-1)
            return 0
        else:
            return 1
    else:
        return 2


def modifyperson(name):
    v=person.get(name,-1)
    if v!=-1:
        print(name,v)
        ch=input("are you sure ?(y/n)")
        if ch=="y":
            vehicle=input("enter vehicle name")
            person[name]=vehicle
            return 0
        else:
            return 1
    else:
        return 2    
        
def displayvehicleByname(name):   
   print(person.get(name))

def displaynameByvehicle(vehicle):   
    key_list=list(person.keys())
    val_list=list(person.values())
    position=val_list.index(vehicle)
    print(key_list[position])

def personname():
   print("people names: ")
   print(person.keys())
            
def vehiclename():
   print("vehicles names: ")
   print(person.values())
        

import sys    
person={}
choice=0
while choice!=8:
    print("1. add new person and their vehicle\n2. delete the person and vehicle\n3. modify vehicle name for person")
    print("4. search vehicle for the given person's name\n5. search list of people for given a vehicle")
    print("6. display all person names\n7. display all vehicle names\n8. exit")
    choice=int(input("enter choice"))
    if choice==1:
        ans=addperson()
        if ans==1:
            print("person added")
        elif ans==2:
            print("vehicle is overWritten")
        else:
            print("name exists")
    elif choice==2:
        name=input("enter name")
        ans=deleteperson(name)
        if ans==0:
            print("name deleted")
        elif ans==1:
            print("name exists, not deleted")
        else:
            print("not found")
    elif choice==3:
        name=input("enter name")
        ans=modifyperson(name)
        if ans==0:
            print("name modify")
        elif ans==1:
            print("name exists, not modified")
        else:
            print("not found")
    elif choice==4:
        name=(input("enter name"))
        displayvehicleByname(name)

    elif choice==5:
        vehicle=(input("enter vehicle"))
        displaynameByvehicle(vehicle)

    elif choice==6:
      personname()

    elif choice==7:
      vehiclename()

    elif choice==8:
        sys.exit(0)

    else:
        print("wrong choice")
