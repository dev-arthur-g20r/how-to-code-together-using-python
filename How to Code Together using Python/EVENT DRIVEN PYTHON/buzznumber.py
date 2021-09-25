import os
def buzzNumber(n):
	if (n % 7 == 0 or n % 10 == 7):
		print(n, " is a Buzz number.")
	else:
		print(n, " is not a Buzz number.")
	return
number = int(input("Number to check if Buzz number: "))
buzzNumber(number)
os.system("pause")