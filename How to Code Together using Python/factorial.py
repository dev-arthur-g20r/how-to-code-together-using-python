import os

def checkFactorial(number):
	result = 1
	if (number > 0):
		while (int(number) >= 1):
			result *= int(number)
			number -= 1
		print ("Factorial: %d" % int(result))
	elif (number == 0):
		print ("Factorial: %d" % int(result))
	else:
		print ("Sorry! Positive integers are only allowed to check its factorials.")
	return

num = input("Number = ")
checkFactorial(int(num))

os.system("pause")