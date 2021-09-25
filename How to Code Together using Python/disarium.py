import os
def checkIfDisariumNumber(n):
	copy = int(n)
	d = 0
	sum = 0
	s = str(n)
	length = len(s)
	while (int(copy) > 0):
		d = int(copy) % 10
		sum = int(sum) + int(pow(int(d),int(length)))
		length = int(length) - 1
		copy = int(copy) / 10
	if (int(sum) == int(n)):
		print ("%d is a Disarium number." % int(n))
	else:
		print ("%d is not a Disarium number." % int(n))
	return
num = input("Number: ")
checkIfDisariumNumber(int(num))
os.system("pause")