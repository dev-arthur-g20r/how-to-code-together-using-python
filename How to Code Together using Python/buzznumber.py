import os
def checkIfBuzzNumber(x):
	if (int(x) % 7 == 0 or int(x) % 10 == 7):
		print ("%d is a Buzz number." % int(x))
	else:
		print ("%d is not a Buzz number." % int(x))
	return
	
num = input("Number to check if Buzz number or not: ")
checkIfBuzzNumber(int(num))
os.system("pause")