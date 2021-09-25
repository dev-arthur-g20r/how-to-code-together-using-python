#!/usr/bin/python
import os

def addNumbers(x,y):
	sum = float(x) + float(y)
	print "Sum is %f" % float(sum)
	return
def subtractNumbers(x,y):
	diff = float(x) - float(y)
	print "Difference is %f" % float(diff)
	return
def multiplyNumbers(x,y):
	prod = float(x) * float(y)
	print "Product is %f" % float(prod)
	return
def divideNumbers(x,y):
	quot = float(x) / float(y)
	print "Quotient is %f" % float(quot)
	return
	
num1 = raw_input("Num1: ")
opera = raw_input("Operator: ")
num2 = raw_input("Num2: ")
if (opera == '+'):
	addNumbers(float(num1),float(num2))
elif (opera == '-'):
	subtractNumbers(float(num1),float(num2))
elif (opera == '*'):
	multiplyNumbers(float(num1),float(num2))
elif (opera == '/'):
	divideNumbers(float(num1),float(num2))
else:
	print "+, -, *, and / are the only Arithmetic operators."
os.system("pause")