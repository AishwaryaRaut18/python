from abc import ABC, abstractmethod


class Person():
    def __init__(self, pid=0, nm=''):
        self.__id = pid
        self.__name = nm

    def getId(self):
        return self.__id

    def __str__(self):
        return  str(self.__id)+"," +str(self.__name)


class Employee(Person, ABC):
    def __init__(self, pid=0, nm='', dept='', desg=''):
        super().__init__(pid, nm)
        self.__dept = dept
        self.__desg = desg

    @abstractmethod
    def calcSal(self):
        pass

    def __str__(self):
        return super().__str__() + ","+str(self.__dept)+","+str(self.__desg)


class SalariedEmp(Employee):
    def __init__(self, pid=0, nm='', dept='', desg='', sal=1000.00):
        super().__init__(pid, nm, dept, desg)
        self.__sal = sal

    def getSal(self):
        return self.__sal

    def __str__(self):
        return super().__str__()+","+str(self.__sal)+"\n"

    def calcSal(self):
        pf=0.08*self.__sal
        hra=0.15*self.__sal
        da=0.1*self.__sal
        netSal=round(self.__sal-pf+hra+da,2)
        return netSal

    def setSal(self, salary):
        self.__sal = salary


class ContractEmp(Employee):
    def __init__(self, pid=0, nm='', dept='', desg='', hrs_worked=8,hourlywages=1000):
        super().__init__(pid, nm, dept, desg)
        self.__hourlyWages = hourlywages
        self.__hrsWorked = hrs_worked

    def gethourlywages(self):
        return self.__hourlyWages

    def gethoursworked(self):
        return self.__hrsWorked

    def __str__(self):
        return super().__str__() + ","+str(self.__hrsWorked )+ " ," +str(self.__hourlyWages)+"\n"

    def sethourlywages(self, wages):
        self.__hourlyWages = wages

    def sethoursWorked(self, hours):
        self.__hourlyWages = hours

    def calcSal(self):
        return round(self.__hourlyWages * self.__hrsWorked, 2)


if __name__ == '__main__':
    p = Person(12, "a")
    print(p)

    s = SalariedEmp(12, "b", "HR", "MGR", 23456)
    print(s.calcSal())

    c = ContractEmp(100, "c", "Eng", "Dev", 1500)
    print(c)
    print(c.calcSal())
    emplist=[]
    emplist.append(str(s))
    emplist.append(str(c))
    print(emplist)