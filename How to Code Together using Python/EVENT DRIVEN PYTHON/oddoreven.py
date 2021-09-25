import os
def oddOrEven(number):
	result = int(number) % 2
	if (result == 0):
		print(number, " is EVEN.")
	else:
		print(number, " is ODD.")
	return

num = int(input("Number: "))
oddOrEven(num)
os.system("pause")