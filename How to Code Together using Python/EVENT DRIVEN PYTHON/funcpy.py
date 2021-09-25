import os
def add(num1,num2):
	sum = float(num1) + float(num2)
	print(num1, " + ", num2, " = ", sum)
	return
def subtract(num1,num2):
	diff = float(num1) - float(num2)
	print(num1, " - ", num2, " = ", diff)
	return
def multiply(num1,num2):
	prod = float(num1) * float(num2)
	print(num1, " * ", num2, " = ", prod)
	return
def divide(num1,num2):
	quot = float(num1) / float(num2)
	print(num1, " / ", num2, " = ", quot)
	return
	
x = float(input("x = "))
ope = input("Operator: ")
y = float(input("y = "))

if (ope == "+"):
	add(x,y)
elif (ope == "-"):
	subtract(x,y)
elif (ope == "*"):
	multiply(x,y)
elif (ope == "/"):
	if (y == 0):
		print("Undefined")
	else:
		divide(x,y)
else:
	print("Arithmetic operators only allowed.")
os.system("pause")