lst=['dxz','axz','bat','rat','cat','pat','bbc','bbm','cbm','acx','scx','dde','ddd','der','fer','ffe','fff','fgt','hgt','ghy','jhy','jiu','jik','jjk','kjh','jki','lki','olk','ilo','nmk','jmn','bnh','jnb','iol','poi','opl','ipo','aqw','wqa','erf','fre','ase','dsw','rtg','ftr','yuh','juy','gvb','nvg','qwe','dwq','tyh','uyt','azx','sza']
result=[]
ch='t'
while ch=='t':
 i=str(input("enter a word"))
 letter=i[1]
 for x in lst:
     if x[1]==letter:
      result.append(x)
 print(result)
 result.clear()
 print("do you want to continue (t/f)")
 ch=input()
