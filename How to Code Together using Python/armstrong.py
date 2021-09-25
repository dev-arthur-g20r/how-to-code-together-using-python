import os
def checkIfArmstrongNumber(n):
	sum = 0
	nstr = str(n)
	x = len(nstr)
	temp = int(nstr)
	while(int(temp) != 0):
		r = int(temp) % 10
		sum = int(sum) + int(pow(r,x))
		temp = int(temp) / 10
	if (int(n) == int(sum)): 
		print ("%d is an Armstrong number." % int(n))
	else:
		print ("%d is not an Armstrong number." % int(n))
	return
num = input("Number: ")
checkIfArmstrongNumber(int(num))
os.system("pause")