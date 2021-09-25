import os
def checkIfArmstrong(n):
	copy = n
	nstr = str(n)
	length = len(nstr)
	sum = 0
	while(copy > 0):
		remainder = copy % 10
		sum += remainder ** length
		length -= 1
		copy = copy // 10
	if (n == sum):
		print(n, " is a Disarium number.")
	else:
		print(n, " is not a Disarium number.")
	return
number = int(input("Number to check if Disarium: "))
checkIfArmstrong(number)
os.system("pause")

	