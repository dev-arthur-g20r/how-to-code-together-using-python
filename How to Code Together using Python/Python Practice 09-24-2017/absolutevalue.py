import os
def absoluteValue(n):
	if (n < 0):
		abs = n * -1
	else:
		abs = n
	return abs
number = float(input("Number to check its absolute value: "))
result = absoluteValue(number)
print("Absolute value:",result)
os.system("pause")