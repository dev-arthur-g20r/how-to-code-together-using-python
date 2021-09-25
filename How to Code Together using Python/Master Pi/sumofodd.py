import os
def sumOfOdd(n):
	sum = n ** 2
	i = 1
	while (i <= n * 2):
		if (i % 2 == 1):
			print(i)
		i += 1
	print("Sum of these even numbers:",sum)
number = int(input("Number of odd numbers: "))
sumOfOdd(number)
os.system("pause")