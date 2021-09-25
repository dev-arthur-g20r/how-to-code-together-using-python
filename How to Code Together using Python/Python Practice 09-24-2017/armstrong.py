import os
def isArmstrong(n):
	copy = n
	num = str(n)
	sum = 0
	length = len(num)
	while (copy > 0):
		remainder = copy % 10
		sum += remainder ** length
		copy = copy // 10
	if (n == sum):
		return "is Armstrong."
	else:
		return "is not Armstrong."
number = int(input("Number to check if Armstrong: "))
result = isArmstrong(number)
print(number,result)
os.system("pause")