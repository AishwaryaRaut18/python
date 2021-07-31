alphabet = "abcdefghijklmnopqrstuvwxyz"
string=str(input("enter string"))
s=string
string=string.replace(" ","")
string=string.lower()
for char in alphabet:
       if char not in string:
           Flag=False
           break
       else:
           Flag=True
if(Flag==False):
    print(f"{s}: is not pangram")
else:
    print(f"{s}: is pangram")
