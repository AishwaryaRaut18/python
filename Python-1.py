import sys
def even(string):
    print("character at even position: ",string[1::2])
def odd(string):
    print("character at odd position: ",string[0::2])
def length(string):
    global n
    n=len(string)
    print("length of string",n)
def a(string):   
    string=string+("a"*n)  
    print(string)
string=str(input("enter string"))
i=a
while i !='e':
    print("a.display characters from even position \nb.display characters from odd position \nc.display length of a string \nd.add a at the end of string length times\ne.exit")
    i=str(input("enter option"))
    if i=='a':
        even(string)
    elif i=='b':
        odd(string)
    elif i=='c':
        length(string)
    elif i=='d':
        a(string)
    elif i=='e':
        print("exit")
        sys.exit()
