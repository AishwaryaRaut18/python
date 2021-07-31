
import numpy as np

lst1=[]
lst2=[]

count=int(input("enter the number of elements :"))
print("For 1st array")
for i in range(1,count+1):
  ele=int(input(f"Enter the element {i}  of first array:"))
  lst1.append(ele)
print(lst1)
print("For 2nd array")
for i in range(1,count+1):
  ele=int(input(f"Enter the element {i}  of first array:"))
  lst2.append(ele)
print(lst2)

arr1=np.asarray((lst1+lst2))
arr1

lst3=[]
lst4=[]

count=int(input("enter the number of elements :"))
print("For 3rd array")
for i in range(1,count+1):
  ele=int(input(f"Enter the element {i}  of first array:"))
  lst3.append(ele)
print(lst3)
print("For 4th array")
for i in range(1,count+1):
  ele=int(input(f"Enter the element {i}  of first array:"))
  lst4.append(ele)
print(lst4)

arr2=np.asarray((lst3+lst4))
arr2

arraynew=np.stack((arr1,arr2))
print("new array= ",arraynew)

add=arr1+arr2
print("addition= ",add)

mul=arr1*arr2
print("multiplication= ",mul)

ex_1=np.exp(arr1)
print("exponential1= ",ex_1)

ex_2=np.exp(arr2)
print("exponential1= ",ex_2)