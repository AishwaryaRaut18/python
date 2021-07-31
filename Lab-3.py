
string=""
s=str(input("enter string: "))
s=s.lower()
s=s.replace(" ","")
for character in s:
    if character.isalpha():
        string += character
s=string[::-1]
if s == string:
    print("its palindrome")
else:
    print("its not a palidrome")
