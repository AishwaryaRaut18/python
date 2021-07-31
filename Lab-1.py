import sys
n = int(input("How many days are in a particular month: "))
d = int(input("What day of week the month begins: "))
for j in range(d):
	sys.stdout.write("   ") 
i = 1
while i <= n:
	if i < 10:
		sys.stdout.write(f"  {i}"),
	else:
		sys.stdout.write(f" {i}"),
	if (i+d) % 7 == 0:
		print ("")
	i = i + 1
