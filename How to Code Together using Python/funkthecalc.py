import os

def addNumbers(num1,num2):
	sum = float(num1) + float(num2)
	print "Sum is %f" % float(sum)
	return
def subtractNumbers(num1,num2):
	diff = float(num1) - float(num2)
	print "Difference is %f" % float(diff)
	return
def multiplyNumbers(num1,num2):
	prod = float(num1) * float(num2)
	print "Product is %f" % float(prod)
	return
def divideNumbers(num1,num2):
	quot = float(num1) / float(num2)
	print "Quotient is %f" % float(quot)
	return
	
x = raw_input("x = ")
operator = raw_input("Operator: ")
y = raw_input("y = ")

if (operator == "+"):
	addNumbers(float(x),float(y))
elif (operator == "-"):
	subtractNumbers(float(x),float(y))
elif (operator == "*"):
	multiplyNumbers(float(x),float(y))
elif (operator == "/"):
	divideNumbers(float(x),float(y))
else:
	print "Sorry! +, -, * and / are the only allowed Arithmetic operators."
os.system("pause")