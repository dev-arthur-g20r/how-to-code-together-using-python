import os
def add(x,y):
	sum = x + y
	return sum
def subtract(x,y):
	difference = x - y
	return difference
def multiply(x,y):
	product = x * y
	return product
def divide(x,y):
	quotient = x / y
	return quotient
num1 = float(input("First number: "))
ope = input("Operator: ")
num2 = float(input("Last number: "))
if (ope == "+"):
	result = add(num1,num2)
	print("Sum of ", num1, " and ", num2, " is ", result)
elif (ope == "-"):
	result = subtract(num1,num2)
	print("Difference of ", num1, " and ", num2, " is ", result)
elif (ope == "*"):
	result = multiply(num1,num2)
	print("Product of ", num1, " and ", num2, " is ", result)
elif (ope == "/"):
	if (num2 == 0):
		print("Undefined")
	else:
		result = divide(num1,num2)
		print("Quotient of ", num1, " and ", num2, " is ", result)
else:
	print("Sorry! These arithmetic operators (+ - * /) are only allowed.")
os.system("pause")