import os
def isHarshad(n):
	copy = n
	sum = 0
	while (copy > 0):
		remainder = copy % 10
		sum += remainder
		copy = copy // 10
	if (n % sum == 0):
		return "is Harshad."
	else:
		return "is not Harshad."
number = int(input("Number to check if Harshad: "))
result = isHarshad(number)
print(number,result)
os.system("pause")