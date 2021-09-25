import os
def checkIfNiven(num):
	c = int(num)
	sum = 0
	while (c > 0):
		d = int(c) % 10
		sum = int(sum) + (d)
		c = int(c) / 10
	if (int(num) % int(sum) == 0):
		print ("%d is a Niven number." % int(num))
	else:
		print ("%d is not a Niven number." % int(num))
	return
n = input("Number: ")
checkIfNiven(int(n))
os.system("pause")