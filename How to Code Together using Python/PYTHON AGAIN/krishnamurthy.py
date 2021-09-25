import os
def isKrishnamurthy(n):
	copy = n
	sum = 0
	while (copy > 0):
		remainder = copy % 10
		factorial = 1
		while (remainder > 0):
			factorial *= remainder
			remainder -= 1
		sum += factorial
		copy = copy // 10
	if (sum == n):
		print(n,"is Krishnamurthy.")
	else:
		print(n,"is not Krishnamurthy.")
number = int(input("Number to check if Krishnamurthy: "))
isKrishnamurthy(number)
os.system("pause")