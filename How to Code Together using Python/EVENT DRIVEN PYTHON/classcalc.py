import os
class my_class():
	def add(self,x,y):
		sum = x + y
		print("Sum is ", sum)
		return
	def subtract(self,x,y):
		diff = x - y
		print("Difference is ", diff)
		return
	def multiply(self,x,y):
		prod = x * y
		print("Product is ", prod)
		return
	def divide(self,x,y):
		sum = x / y
		print("Sum is ", sum)
		return
calc = my_class()

a = float(input("a = "))
ope = input("Operator: ")
b = float(input("b = "))

if (ope == "+"):
	calc.add(a,b)
elif (ope == "-"):
	calc.subtract(a,b)
elif (ope == "*"):
	calc.multiply(a,b)
elif (ope == "/"):
	if (b == 0):
		print("Undefined")
	else:
		calc.divide(a,b)
else:
	print("Sorry! +, -, * and / are only allowed.")
os.system("pause")