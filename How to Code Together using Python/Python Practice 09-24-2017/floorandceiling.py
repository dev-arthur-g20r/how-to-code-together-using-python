import os
def floor(n):
	if (float(n) == int(n)):
		floor = int(n)
	elif (n < 1):
		floor = int(n - 1)
	else:
		floor = int(n)
	return floor
def ceiling(n):
	if (float(n) == int(n)):
		ceiling = int(n)
	elif(n < 1):
		ceiling = int(n)
	else:
		ceiling = int(n + 1)
	return ceiling
number = float(input("Number to check its floor and ceiling: "))
f = floor(number)
c = ceiling(number)
print("Floor:",f,"\nCeiling:",c)
os.system("pause")