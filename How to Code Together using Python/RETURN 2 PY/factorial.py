import os
class Factorial:
	def factorial(self,n):
		factorial = 1
		if (n > 0):
			i = n
			while (i > 0):
				factorial *= i 
				i -= 1
			return factorial
		elif (n == 0):
			return factorial
x = Factorial()
number = int(input("Number to check its factorial: "))
result = x.factorial(number)
if (number >= 0):
	print("Factorial:",result)
else:
	print("Sorry! Numbers 0 and above are only allowed.")
os.system("pause")