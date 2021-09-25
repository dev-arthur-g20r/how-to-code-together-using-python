import os

class Calculator:
	def __init__(self,first,second):
		self.sum = float(first) + float(second)
		self.difference = float(first) - float(second)
		self.product = float(first) * float(second)
		self.quotient = float(first) / float(second)

first_number = float(input("First Number: "))
operator = input("Operator: ")
second_number = float(input("Second Number: "))
my_calculator = Calculator(first_number,second_number)

if (operator == "+"):
	print("\n{0} + {1} = {2}".format(first_number,second_number,my_calculator.sum))
elif (operator == "-"):
	print("\n{0} - {1} = {2}".format(first_number,second_number,my_calculator.difference))
elif (operator == "*"):
	print("\n{0} * {1} = {2}".format(first_number,second_number,my_calculator.product))
elif (operator == "/"):
	print("\n{0} / {1} = {2}".format(first_number,second_number,my_calculator.quotient))
else:
	print("\nSorry! + - * / are only allowed.")

os.system("pause")