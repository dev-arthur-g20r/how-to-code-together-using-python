import os
def checkIfHarshadNumber(x):
	sum = 0
	c = int(x)
	while (int(c) > 0):
		d = int(c) % 10
		sum = int(sum) + d
		c = int(c) / 10
	if (int(x) % int(sum) == 0):
		print ("%d is a Harshad number." % int(x))
	else:
		print ("%d is not a Harshad number." % int(x))
	return

num = int(input("Number to check if Harshad number: "))
checkIfHarshadNumber(int(num))
os.system("pause")