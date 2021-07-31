import sys
def main():
      n=int(input("Enter number"))
      sys.stdout.write("1")
      for i in range(2,n+1):
          print("+",i,end=" ")
      print("=",end=" ")
      print(sum(n))
def sum(x):
        if x <= 1:
          return x
        else:
          return x + sum(x-1)

main()
