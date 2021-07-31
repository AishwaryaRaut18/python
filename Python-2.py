string1=str(input("enter first string"))
string2=str(input("enter sub string you want to search"))
pos = string1.find(string2)
while pos != -1:
   print("position: ",pos)
   pos=string1.find((string2),pos+1)
print(string1.count(string2))
