from collections import OrderedDict
people={'Arham':'Blue','Vinod':'Purple','Lisa':'Yellow','Jenny':'Pink'}
n=len(people.keys())
print("number of people: ",n)
people['Lisa']='Green'
people.popitem()  #removes last inserted item
sort=OrderedDict(sorted(people.items()))
print(sort)
