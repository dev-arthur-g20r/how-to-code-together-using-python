import os
def absoluteValue(n):
	if (n < 0):
		abs = n * -1
	else:
		abs = n
	print("Absolute value:",abs)
number = float(input("Number to check its absolute value: "))
absoluteValue(number)
os.system("pause")