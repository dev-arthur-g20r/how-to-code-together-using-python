import os
def floorAndCeiling(n):
	if (float(n) == int(n)):
		floor = int(n)
		ceiling = int(n)
	elif (n < 1):
		floor = int(n - 1)
		ceiling = int(n)
	else:
		floor = int(n)
		ceiling = int(n + 1)
	print("Floor:",floor,"\nCeiling:",ceiling)
number = float(input("Number to check its floor and ceiling: "))
floorAndCeiling(number)
os.system("pause")