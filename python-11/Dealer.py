# 2.	Create a class Dealer,
# store id, name, mobile and full address create 5 objects
# Find dealers which matches following condition
# a)	Find dealer who lives in Pune.
# b)	Find dealer having mobile as palindrome.


class Dealer():
    def __init__(self, id=0, nm='',city='',mob=1111111111):
        self.__id = id
        self.__name = nm
        self.__address = city
        self.__mobile=mob


    def getId(self):
        return self.__id

    def getMobile(self):
        return self.__mobile

    def getAddress(self):
        return self.__address

    def __str__(self):
        return  str(self.__id)+"," +str(self.__name)+","+str(self.__address)+"," +str(self.__mobile)


d1=Dealer(101,"Hari","Pune",9999999999)
d2=Dealer(102,"Shravya","Hyderabad",9440815249)
d3=Dealer(103,"Kavya","Kolkata",9985557190)
d4=Dealer(104,"Raam","Mumbai",9444444449)
d5=Dealer(105,"Kishore","Pune",9898984444)
dealerslist=[d1,d2,d3,d4,d5]

print("The dealers with palindrome mobile number are:")
for d in dealerslist:
    if str(d.getMobile())==str(d.getMobile())[::-1]:
        print(d)

print("The dealers who reside in Pune are:")
for d in dealerslist:
    if d.getAddress()=="Pune":
        print(d)


