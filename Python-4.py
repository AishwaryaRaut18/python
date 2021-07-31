cities=[]
location=[]
n=int(input("enter list size"))
for x in range(0, n):
      c=str(input("enter city name"))
      cities.append(c)
      l=str(input("enter location"))
      location.append(l)
      
zipped=zip(cities,location)
print(list(zipped))
