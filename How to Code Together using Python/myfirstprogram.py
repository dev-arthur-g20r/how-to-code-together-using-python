import os
print ("Hello World!")
x = input("Enter x: ")
operator = input("Enter operator: ")
y = input("Enter y: ")
if (operator == '+'):
	print ("Sum is ", float(x) + float(y))
elif (operator == '-'):
	print ("Difference is ", float(x) - float(y))
elif (operator == '*'):
	print ("Product is ", float(x) * float(y))
elif (operator == '/'):
	print ("Quotient is ", float(x) / float(y))
else:
	print ("Sorry! +, -, * and / are the only allowed arithmetic operators.")
os.system("pause")