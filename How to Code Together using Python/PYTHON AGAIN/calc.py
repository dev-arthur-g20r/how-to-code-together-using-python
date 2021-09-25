import os
def add(x,y):
	sum = x + y
	print("Sum:",sum)
def subtract(x,y):
	difference = x - y
	print("Difference:",difference)
def multiply(x,y):
	product = x * y
	print("Product:",product)
def divide(x,y):
	if (y == 0):
		print("Undefined")
	else:
		quotient = x / y
		print("Quotient:",quotient)
num1 = float(input("Num1 = "))
operator = input("Operator: ")
num2 = float(input("Num2 = "))
if (operator == "+"):
	add(num1,num2)
elif (operator == "-"):
	subtract(num1,num2)
elif (operator == "*"):
	multiply(num1,num2)
elif (operator == "/"):
	divide(num1,num2)
else:
	print("Sorry! + - * / are only allowed.")
os.system("pause")