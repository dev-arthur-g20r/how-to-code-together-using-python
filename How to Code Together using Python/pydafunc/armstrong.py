import os
def isArmstrong(n):
	copy = n
	sum = 0
	strn = str(n)
	length = len(strn)
	while (copy > 0):
		remainder = copy % 10
		sum += remainder ** length
		copy = copy // 10
	if (sum == n):
		return "{} is Armstrong.".format(n)
	else:
		return "{} is not Armstrong.".format(n)
number = int(input("Number to check if Armstrong: "))
result = isArmstrong(number)
print(result)
os.system("pause")