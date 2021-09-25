import os
class Calculator:
	def add(self,x,y):
		sum = x + y
		return "Sum: {}".format(sum)
	def subtract(self,x,y):
		difference = x - y
		return "Difference: {}".format(difference)
	def multiply(self,x,y):
		product = x * y
		return "Product: {}".format(product)
	def divide(self,x,y):
		quotient = x / y
		return "Quotient: {}".format(quotient)
calc = Calculator()
num1 = float(input("Num1 = "))
operator = input("Operator: ")
num2 = float(input("Num2 = "))
if (operator == "+"):
	result = calc.add(num1,num2)
elif (operator == "-"):
	result = calc.subtract(num1,num2)
elif (operator == "*"):
	result = calc.multiply(num1,num2)
elif (operator == "/"):
	result = calc.divide(num1,num2)
else:
	print("Sorry! + - * / are the only allowed operators.")
print(result)
os.system("pause")