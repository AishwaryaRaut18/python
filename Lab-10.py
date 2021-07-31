#function
def overlapping(lst1,lst2):
 for x in range(0,n):
    for y in range(0,n1):
     if (lst1[x]==lst2[y]):
        return 'True'

# creating an empty list
lst1 = []
lst2 = [] 
# number of elemetns as input
n = int(input("Enter number of elements for 1st list : "))
  
# iterating till the range
for i in range(0, n):
    ele = int(input())
  
    lst1.append(ele) # adding the element
      
print(lst1)

n1 = int(input("Enter number of elements for 2nd list : "))
  
# iterating till the range
for j in range(0, n1):
    ele = int(input())
  
    lst2.append(ele) # adding the element
      
print(lst2)

if(overlapping(lst1,lst2)=='True'):
    print("common element found")
else:
    print("all elements are unique")


