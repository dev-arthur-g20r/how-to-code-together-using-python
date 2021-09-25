import os
class Calculator:
	def add(self,x,y):
		sum = x + y
		return sum
	def subtract(self,x,y):
		difference = x - y
		return difference
	def multiply(self,x,y):
		product = x * y
		return product
	def divide(self,x,y):
		quotient = x / y
		return quotient
calc = Calculator()
num1 = float(input("Num1 = "))
operator = input("Operator: ")
num2 = float(input("Num2 = "))
if (operator == "+"):
	result = calc.add(num1,num2)
	print("Sum:",result)
elif (operator == "-"):
	result = calc.subtract(num1,num2)
	print("Difference:",result)
elif (operator == "*"):
	result = calc.multiply(num1,num2)
	print("Product:",result)
elif (operator == "/"):
	result = calc.divide(num1,num2)
	print("Quotient:",result)
else:
	print("Sorry! + - * / are the only Arithmetic operators.")
os.system("pause")