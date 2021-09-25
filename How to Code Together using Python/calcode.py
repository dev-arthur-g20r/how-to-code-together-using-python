import os
num1 = float(input("Num1 = "))
ope = input("Operator: ")
num2 = float(input("Num2 = "))

if ope == "+":
	sum = num1 + num2
	print (num1, " + ", num2, " = ", sum)
elif ope == "-":
	diff = num1 - num2
	print (num1, " - ", num2, " = ", diff)
elif ope == "*":
	prod = num1 * num2
	print (num1, " * ", num2, " = ", prod)
elif ope == "/":
	quot = num1 / num2
	print (num1, " / ", num2, " = ", quot)
else:
	print ("Sorry! +, -, *, and / are the only allowed Arithmetic operators to be used.")
os.system("pause")