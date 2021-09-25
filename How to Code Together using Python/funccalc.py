import os

def addNumbers(num1,num2):
	sum = float(num1) + float(num2)
	print ("Sum is %f" % sum)
	return
def subtractNumbers(num1,num2):
	diff = float(num1) - float(num2)
	print ("Difference is %f" % diff)
	return
def multiplyNumbers(num1,num2):
	prod = float(num1) * float(num2)
	print ("Product is %f" % prod)
	return
def divideNumbers(num1,num2):
	quot = float(num1) / float(num2)
	print ("Quotient is %f" % quot)
	return
	
x = input("x = ")
operator = input("Operator: ")
y = input("y = ")
if (operator == "+"):
	addNumbers(x,y)
elif (operator == "-"):
	subtractNumbers(x,y)
elif (operator == "*"):
	multiplyNumbers(x,y)
elif (operator == "/"):
	divideNumbers(x,y)
else:
	print("Sorry! Arithmetic operators +, -, *, and / are only allowed for the two numbers to operate.")

os.system("pause")