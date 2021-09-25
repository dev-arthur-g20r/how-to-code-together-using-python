import os
def floor(n):
	if (n % 1 == 0):
		floor = int(n)
	elif (n < 0):
		floor = int(n - 1)
	else:
		floor = int(n)
	print("Floor: ", floor)
	return
def ceiling(n):
	if (n % 1 == 0):
		ceiling = int(n)
	elif(n < 0):
		ceiling = int(n)
	else:
		ceiling = int(n + 1)
	print("Ceiling: ", ceiling)
	return
num = float(input("Number to check its floor and ceiling: "))
floor(num)
ceiling(num)
os.system("pause")