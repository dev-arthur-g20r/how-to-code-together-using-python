import os
import math
def checkIfSunnyNumber(x):
	n = int(x) + 1
	root = math.sqrt(int(n))
	if (int(root) == float(root)):
		print ("%d is a Sunny number." % int(x))
	else:
		print ("%d is not a Sunny number." % int(x))
	return

num = input("Number to check if sunny number: ")
checkIfSunnyNumber(int(num))
os.system("pause")