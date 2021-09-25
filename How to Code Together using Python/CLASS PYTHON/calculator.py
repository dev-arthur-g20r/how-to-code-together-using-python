import os
class Calculator:
	def add(self,x,y):
		sum = x + y
		print("Sum:",sum)
	def subtract(self,x,y):
		difference = x - y
		print("Difference:",difference)
	def multiply(self,x,y):
		product = x * y
		print("Product:",product)
	def divide(self,x,y):
		quotient = x / y
		print("Quotient:",quotient)
calc = Calculator()
num1 = float(input("Num1 = "))
operator = input("Operator: ")
num2 = float(input("Num2 = "))
if (operator == "+"):
	calc.add(num1,num2)
elif (operator == "-"):
	calc.subtract(num1,num2)
elif (operator == "*"):
	calc.multiply(num1,num2)
elif (operator == "/"):
	calc.divide(num1,num2)
else:
	print("Sorry! + - * / are only allowed.")
os.system("pause")
