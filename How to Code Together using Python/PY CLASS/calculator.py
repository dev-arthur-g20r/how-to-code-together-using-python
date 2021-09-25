import os
class Calculator:
	def __init__(self,x,y):
		self.x = x 
		self.y = y
	def add(self):
		sum = self.x + self.y
		print("Sum:",sum)
	def subtract(self):
		difference = self.x - self.y
		print("Difference:",difference)
	def multiply(self):
		product = self.x * self.y
		print("Product:",product)
	def divide(self):
		quotient = self.x / self.y
		print("Quotient:",quotient)
num1 = float(input("Num1 = "))
operator = input("Operator: ")
num2 = float(input("Num2 = "))
calc = Calculator(num1,num2)
if (operator == "+"):
	calc.add()
elif (operator == "-"):
	calc.subtract()
elif (operator == "*"):
	calc.multiply()
elif (operator == "/"):
	calc.divide()
else:
	print("Sorry! + - * / are the only allowed Arithmetic operators.")
os.system("pause")