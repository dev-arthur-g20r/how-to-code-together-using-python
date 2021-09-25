import os
class Factorial:
	def __init__(self,n):
		self.n = n
	def factorial(self):
		factorial = 1
		if (self.n > 0):
			i = self.n 
			while (i > 0):
				factorial *= i 
				i -= 1
			return "Factorial: {}".format(factorial)
		elif (self.n == 0):
			return "Factorial: {}".format(factorial)
		else:
			print("Sorry! Numbers 0 and above are only allowed.")
			return ""
number = int(input("Number to check its factorial: "))
x = Factorial(number)
result = x.factorial()
print(result)
os.system("pause")