import os
class Calculator:
	def __init__(self,x,y):
		self.x = x
		self.y = y
	def add(self):
		sum = self.x + self.y
		return "Sum: {}".format(sum)
	def subtract(self):
		difference = self.x - self.y
		return "Difference: {}".format(difference)
	def multiply(self):
		product = self.x * self.y
		return "Product: {}".format(product)
	def divide(self):
		quotient = self.x / self.y
		return "Quotient: {}".format(quotient)
num1 = float(input("Num1 = "))
operator = input("Operator: ")
num2 = float(input("Num2 = "))
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
	print("Sorry! + - * / are only allowed.")
print(result)
os.system("pause")