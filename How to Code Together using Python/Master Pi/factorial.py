import os
def factorial(n):
	factorial = 1
	if (n > 0):
		i = n
		while(i > 0):
			factorial *= i
			i -= 1
		print("Factorial:",factorial)
	elif (n == 0):
		print("Factorial:",factorial)
	else:
		print("Sorry! Numbers 0 and greater are only allowed.")
number = int(input("Number to check its factorial: "))
factorial(number)
os.system("pause")