import os
def checkIfArmstrong(n):
	copy = n
	nstr = str(n)
	length = len(nstr)
	sum = 0
	while(copy > 0):
		remainder = copy % 10
		sum += remainder ** length
		copy = copy // 10
	if (n == sum):
		print(n, " is an Armstrong number.")
	else:
		print(n, " is not an Armstrong number.")
	return
number = int(input("Number to check if Armstrong: "))
checkIfArmstrong(number)
os.system("pause")

	