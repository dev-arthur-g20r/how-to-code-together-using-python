import os
def checkIfHarshad(num):
	c = int(num)
	sum = 0
	while int(c) > 0:
		d = int(c) % 10
		sum = int(sum) + int(d)
		c = int(c) / 10
	if (int(num) % int(sum) == 0):
		print(num, " is a Harshad number.")
	else:
		print(num, " is not a Harshad number.")
	return
number = int(input("Number to check if Harshad number: "))
checkIfHarshad(int(number))
os.system("pause")