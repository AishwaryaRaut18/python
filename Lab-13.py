import re
 
def correct(inputString):
 
    #Removing extra spaces
    correctedString = re.sub('\ +',' ',inputString)
 
    #Putting extra space after period
    correctedString = re.sub('\.','. ',correctedString)
 
    print(correctedString)
 
 
inputString = str(input("enter string"))
 
correct(inputString)
 
