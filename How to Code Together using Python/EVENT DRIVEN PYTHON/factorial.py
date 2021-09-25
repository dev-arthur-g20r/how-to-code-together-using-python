import os
def factorial(number):
	factorial = 1
	if (number == 0):
		print("Factorial is 1.")
	elif(number < 0):
		print("Sorry! Positive integers are only allowed for the factorial operation.")
	else:
		while number >= 1:
			factorial *= number
			number -= 1
		print("Factorial is ", factorial)
	return
	
num = int(input("Number to determine its factorial: "))
factorial(num)
		
os.system("pause")