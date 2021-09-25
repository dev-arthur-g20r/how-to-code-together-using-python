import os
def add(x,y):
	sum = x + y
	return sum
def subtract(x,y):
	diff = x - y
	return diff
def multiply(x,y):
	prod = x * y
	return prod
def divide(x,y):
	quot = x / y 
	return quot
num1 = float(input("Num1: "))
operator = input("Operator: ")
num2 = float(input("Num2: "))
if (operator == "+"):
	result = add(num1,num2)
	print(num1," + ",num2," = ",result)
elif (operator == "-"):
	result = subtract(num1,num2)
	print(num1," - ",num2," = ",result)
elif (operator == "*"):
	result = multiply(num1,num2)
	print(num1," * ",num2," = ",result)
elif (operator == "/"):
	if (num2 == 0):
		print("Undefined")
	else:
		result = divide(num1,num2)
		print(num1," / ",num2, " = ",result)
else:
	print("Sorry! + - * / are the only allowed Arithmetic operators.")
os.system("pause")