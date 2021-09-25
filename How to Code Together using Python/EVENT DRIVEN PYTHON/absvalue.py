import os
def absValue(n):
	if (n < 0):
		return n * -1
	else:
		return n
number = float(input("Number to check its absolute value: "))
result = absValue(number)
print("Absolute value: ", result)
os.system("pause")