import os
def isDisarium(n):
	copy = n
	number = str(n)
	length = len(number)
	sum = 0
	while (copy > 0):
		remainder = copy % 10
		sum += remainder ** length
		length -= 1
		copy = copy // 10
	if (sum == n):
		return "{} is Disarium.".format(n)
	else:
		return "{} is not Disarium.".format(n)
number = int(input("Number to check if Disarium: "))
result = isDisarium(number)
print(result)
os.system("pause")