import os
class Factorial:
	def factorial(self,n):
		factorial = 1
		if (n > 0):
			i = n
			while (i > 0):
				factorial *= i
				i -= 1
			return "Factorial: {}".format(factorial)
		elif (n == 0):
			return "Factorial: {}".format(factorial)
		else:
			return "Sorry! Numbers 0 and above are only allowed."
x = Factorial()
number = int(input("Number to check its factorial: "))
result = x.factorial(number)
print(result)
os.system("pause")