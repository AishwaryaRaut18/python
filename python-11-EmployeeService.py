import os
import sys
from Employee import SalariedEmp,ContractEmp
if os.path.exists("contractemployee.dat"):
    with open("contractemployee.dat") as contractfh:
        contractlist = contractfh.readlines()
        print(contractlist)
else:
    contractlist = []

if os.path.exists("salariedemployee.dat"):
    with open("salariedemployee.dat") as salariedfh:
        salariedlist = salariedfh.readlines()
        print(salariedlist)
else:
    salariedlist = []

# counters
salariedcount = len(salariedlist)
contractcount=len(contractlist)



# functions
def addemployee():

    cont = 'y'
    while cont == 'y':

        eid = int(input("enter id"))
        nm = input("enter employee name")
        ds = input("enter designation")
        dt = input("enter department")
        ch = input("do you want to add salaried emp or contract emp? (s/c)")
        if ch == "s":
            s = float(input("enter empsal:"))
            temp=SalariedEmp(eid, nm,  dt, ds, s)
            salariedlist.append(str(temp))
        elif ch=="c":
            w = float(input("enter emp hourly wages:"))
            h = int(input("enter the hours worked:"))
            temp=ContractEmp(eid, nm, dt, ds,h, w)
            contractlist.append(str(temp))
        else:
            print("invalid choice")
        cont = input("do u want to continue? y/n")



def deleteEmp(eno,e):
    if e=="s":
        emp = searchbyempno(eno,salariedlist)
        if emp != None:
            salariedlist.remove(emp)
        return emp
    elif e=="c":
        emp = searchbyempno(eno, contractlist)
        if emp != None:
            contractlist.remove(emp)
        return emp
    else:
        return None


def modifysalary(eno, sal):
    cout = 0
    for i in salariedlist:
        lst1 = i.split(',')
        if (int(lst1[0])) == eno:
            lst1[4] = int(input('enter new salary'))
            salariedlist[cout] = ','.join(lst1)

        cout = cout + 1
    else:
        print('Id not found')



def searchbyempno(eno,lst):
    return_val=None
    for em in lst:
        lst1 = em.split(',')
        if (int(lst1[0])) == eno:
            return_val= em
    return return_val

def calculateSalary(eid,choice):
    if choice=="s":
         for em in salariedlist:
            lst1 = em.split(',')
            if (int(lst1[0])) == eid:
                 temp=SalariedEmp(int(lst1[0]),lst1[1],lst1[2],lst1[3],float(lst1[4]))
                 print("salary is:",float(lst1[4]) )
                 sal=temp.calcSal()
                 return sal
    elif choice=="c":
            for em in contractlist:
                lst1 = em.split(',')
                if (int(lst1[0])) == eid:
                    temp=ContractEmp(int(lst1[0]),lst1[1],lst1[2],lst1[3],int(lst1[4]),float(lst1[5]))
                    print("salary is:", float(lst1[5]))
                    sal=temp.calcSal()
                    return sal
    else:
        return None

    return None


print("salaried employees list len ", len(salariedlist))
print("contract employees list len ", len(contractlist))

ch = 1
while ch < 8:

    print("1. Add new employee")
    print("2. Delete employee")
    print("3. Modify salary of employee")
    print("4. Search employee")
    print("5. Calculate salary of employee")
    print("6. Display all")
    print("7. Exit, write all objects into file ")

    ch = int(input("Enter your choice"))
    if ch == 1:
        addemployee()
        print(salariedlist)
        print(contractlist)
    elif ch == 2:
        e = input("enter either salaried or contract employee to be deleted (s/c)")
        eid = int(input("Enter the eid of the employee to be deleted:"))
        ret=deleteEmp(eid,e)
        if ret!=None:
            print(f"employee {eid} deleted")
        else:
            print(f"Employee {eid} not found")


    elif ch == 3:
        eno = input("enter the id of the employee:")
        sal = int(input("Enter the salary of the employee"))
        modifysalary(eno, sal)

    elif ch == 4:
        eno=int(input("enter id"))
        emp=None
        e = input("enter either salaried or contract employee to be deleted (s/c)")
        if e=="s":
            emp=searchbyempno(eno,salariedlist)
        elif e=="c":
            emp=searchbyempno(eno,contractlist)
        else:
            print("invalid entry")

        if emp!=None:
            print(emp)
        else:
            print("not found")
    elif ch == 5:
        eid=int(input("enter eid:"))
        e = input("enter either salaried or contract employee to be deleted (s/c)")
        sal=calculateSalary(eid,e)
        if sal!=None:
            print(f"The salary of the employee {eid} is {sal}")
        else:
            print("Employee not found")

    elif ch == 6:
        print("The total employees are:")
        print("Salaried employees:")
        print(salariedlist)
        print("contract employees:")
        print(contractlist)
    elif ch == 7:

            with open("salariedemployee.dat", "w") as fo:
                for f in salariedlist:
                    fo.write(f)

            with open("contractemployee.dat", "w") as fo:
                for f in contractlist:
                    fo.write(f)
            sys.exit(0)

    else:
        print("Invalid choice.")




