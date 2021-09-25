import os
def factorial(n):
	i = n
	factorial = 1
	if (n > 0):
		while (i > 0):
			factorial *= i
			i -= 1
		return factorial
	elif (n == 0):
		return factorial
number = int(input("Number to check its factorial: "))
result = factorial(number)
if (number >= 0):
	print("Factorial:",result)
else:
	print("Numbers greater than or equal to 0 are only allowed. Sorry.")
os.system("pause")