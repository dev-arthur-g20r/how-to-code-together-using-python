import os
def highestOf3(a,b,c):
	if (a > b and a > c):
		print("a = ", a, " is the highest.")
	elif (b > a and b > c):
		print("b = ", b, " is the highest.")
	elif (c > a and c > b):
		print("c = ", c, " is the highest.")
	elif (a == b and b > c):
		print("a = ", a, " and b = ", b, " are the highest.")
	elif (a == c and c > b):
		print("a = ", a, " and c = ", c, " are the highest.")
	elif (b == c and c > a):
		print("b = ", b, " and c = ", b, " are the highest.")
	else:
		print("All values are equal.")
	return
num1 = float(input("First number: "))
num2 = float(input("Second number: "))
num3 = float(input("Third number: "))
highestOf3(num1,num2,num3)
os.system("pause")