import os
def sumOfOdd(n):
	i = 1
	sum = n ** 2
	while (i <= n * 2):
		if (i % 2 == 1):
			print(i)
		i += 1
	print("Sum of these odd numbers:",sum)
number = int(input("Number of odd numbers to check its sum: "))
sumOfOdd(number)
os.system("pause")