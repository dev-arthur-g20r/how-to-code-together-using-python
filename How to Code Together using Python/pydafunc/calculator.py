import os
def add(x,y):
	sum = x + y
	return "{} + {} = {}".format(x,y,sum)
def subtract(x,y):
	difference = x - y
	return "{} - {} = {}".format(x,y,difference)
def multiply(x,y):
	product = x * y
	return "{} * {} = {}".format(x,y,product)
def divide(x,y):
	quotient = x / y
	return "{} / {} = {}".format(x,y,quotient)
num1 = float(input("Num1 = "))
operator = input("Operator: ")
num2 = float(input("Num2 = "))
result = ""
if (operator == "+"):
	result = add(num1,num2)
elif (operator == "-"):
	result = subtract(num1,num2)
elif (operator == "*"):
	result = multiply(num1,num2)
elif (operator == "/"):
	result = divide(num1,num2)
else:
	result = "Sorry! + - * / are the only allowed operators."
print(result)
os.system("pause")