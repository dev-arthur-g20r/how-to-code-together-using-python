import os
def floorAndCeiling(n):
	if (float(n) < 0):
		floor = int(n - 1)
		ceiling = int(n)
	elif (float(n) == int(n)):
		floor = int(n)
		ceiling = int(n)
	else:
		floor = int(n)
		ceiling = int(n + 1)
	return "Floor: {}\nCeiling: {}".format(floor,ceiling)
number = float(input("Number to check floor and ceiling: "))
result = floorAndCeiling(number)
print(result)
os.system("pause")