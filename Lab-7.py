def translate(String):
    new=""
    for i in range (0, len(string)):
        if string[i] == 'a' or string[i]== 'e' or string[i] == 'i' or string[i] == 'o' or string[i] == 'u':
            b = string[i]
            new += b
              
        elif string[i]!=" " or  string[i] == "," or  string[i] == "!" or  string[i] == ".":
            b = string[i] +'o' + string[i]
            new += b
              
        elif string[i] == " " or  string[i] == "," or  string[i] == "!" or  string[i] == ".":
            new +=string[i]
      
    print(new)
      
string = input("enter string")
translate(string)
