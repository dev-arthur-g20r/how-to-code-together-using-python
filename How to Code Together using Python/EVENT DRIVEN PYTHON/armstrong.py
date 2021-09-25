import os
def checkIfArmstrong(num):
	c = int(num)
	sum = 0
	strnum = str(num)
	length = len(strnum)
	while (int(c) > 0):
		d = int(c) % 10
		sum += int(pow(int(d),int(length)))
		c = c / 10
	if (int(num) == int(sum)):
		print(num, " is an Armstrong number.")
	else:
		print(num, " is not an Armstrong number.")
	return
number = int(input("Number to check if Armstrong number: "))
checkIfArmstrong(number)
os.system("pause")