import os
def add(n1,n2):
	sum = n1 + n2
	print("Sum:",sum)
def subtract(n1,n2):
	difference = n1 - n2
	print("Difference:",difference)
def multiply(n1,n2):
	product = n1 * n2
	print("Product:",product)
def divide(n1,n2):
	quotient = n1 / n2
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