import os;
print "Hello World!";
print "Arithmetic Calcualator with 2 added operators (% - Modulus for ints only and ** - Exponent)";
x = raw_input("Enter x: ");
operator = raw_input("Enter operator: ");
y = raw_input("Enter y (Exponent for **): ");
if (operator == "+"):
	print "Sum is ", float(x) + float(y);
elif (operator == "-"):
	print "Difference is ", float(x) - float(y);
elif (operator == "*"):
	print "Product is ", float(x) * float(y);
elif (operator == "/"):
	print "Quotient is ", float(x) / float(y);
elif (operator == "%"):
	print "Remainder is %d" % (int(x) % int(y));
elif (operator == "**"):
	print "%f raised to power of %f is %f" % (float(x), float(y), float(x) ** float(y));
else:
	print "Sorry! +, -, *, /, % and ** are the only allowed arithmetic operators.";
os.system("pause");