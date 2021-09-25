import os
class Calculator():
	"""docstring for Calculator"""
	def __init__(self, x,y):
		self.x = x
		self.y = y
	def add(self):
		sum_r = self.x + self.y
		return "Sum: {}".format(sum_r)
	def subtract(self):
		diff = self.x - self.y
		return "Difference: {}".format(diff)
	def multiply(self):
		prod = self.x * self.y
		return "Product: {}".format(prod)
	def divide(self):
		quot = self.x / self.y
		return "Quotient: {}".format(quot)
		

num1 = float(input("Num1: "))
operator = input("Operator (+ - * /): ")
num2 = float(input("Num2: "))
calc = Calculator(num1,num2)
result = ""
if (operator == "+"):
	result = calc.add()
elif (operator == "-"):
	result = calc.subtract()
elif (operator == "*"):
	result = calc.multiply()
elif (operator == "/"):
	result = calc.divide()
else:
	result = "Sorry! + - * / are only allowed."
print(result)
os.system("pause")
