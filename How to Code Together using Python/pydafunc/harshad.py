import os
def isHarshad(n):
	copy = n
	sum = 0
	while (copy > 0):
		remainder = copy % 10
		sum += remainder
		copy = copy // 10
	if (n % sum == 0):
		return "{} is Harshad.".format(n)
	else:
		return "{} is not Harshad.".format(n)
number = int(input("Number to check if Harshad: "))
result = isHarshad(number)
print(result)
os.system("pause")