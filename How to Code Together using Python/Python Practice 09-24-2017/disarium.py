import os
def isDisarium(n):
	copy = n
	sum = 0
	num = str(n)
	length = len(num)
	while (copy > 0):
		remainder = copy % 10
		sum += remainder ** length
		length -= 1
		copy = copy // 10
	if (n == sum):
		return "is Disarium."
	else:
		return "is not Disarium."
number = int(input("Number to check if Disarium: "))
result = isDisarium(number)
print(number,result)
os.system("pause")