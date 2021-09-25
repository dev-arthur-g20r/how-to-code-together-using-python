import os
import math
def sunnyNumber(n):
	x = n + 1
	root = math.sqrt(x)
	if (int(root) == float(root)):
		print(n, " is a Sunny number.")
	else:
		print(n, " is not a Sunny number.")
	return
number = int(input("Number to check if Sunny: "))
sunnyNumber(number)
os.system("pause")