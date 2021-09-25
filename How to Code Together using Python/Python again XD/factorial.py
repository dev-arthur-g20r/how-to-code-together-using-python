import os
def factorial(n):
	factorial = 1
	i = n
	while (i > 0):
		factorial *= i
		i -= 1
	print("Factorial:",factorial)
number = int(input("Number to check its factorial: "))
factorial(number)
os.system("pause")