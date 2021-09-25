import os
class calculator():
	def add(self,x,y):
		sum = x + y
		return sum
	def subtract(self,x,y):
		difference = x - y
		return difference
	def multiply(self,x,y):
		product = x * y
		return product
	def quotient(self,x,y):
		quotient = x / y
		return quotient
	def operatorError(self):
		print("Sorry! The only allowed operators are + - * and /.")

computer = calculator()
num1 = float(input("Num1 = "))
operator = input("Operator: ")
num2 = float(input("Num2 = "))

if (operator == "+"):
	result = computer.add(num1,num2)
	print("Sum is ", result)
elif (operator == "-"):
	result = computer.difference(num1, num2)
	print("Difference is ", result)
elif (operator == "*"):
	result = computer.product(num1, num2)
	print("Product is ", result)
elif (operator == "/"):
	if (num2 == 0):
		print("Undefined")
	else:
		result = computer.quotient(num1,num2)
		print("Quotient is ", result)
else:
	computer.operatorError()
os.system("pause")