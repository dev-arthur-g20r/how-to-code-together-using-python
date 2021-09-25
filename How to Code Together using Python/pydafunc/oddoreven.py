import os
def oddOrEven(n):
	if (n % 2 == 0):
		return "{} is EVEN.".format(n)
	else:
		return "{} is ODD.".format(n)

number = int(input("Number: "))
result = oddOrEven(number)
print(result)
os.system("pause")