import os
def sumOfEven(n):
	sum = n * (n + 1)
	i = 1
	while (i <= n * 2):
		if (i % 2 == 0):
			print(i)
		i += 1
	print("Sum of these even numbers:",sum)
number = int(input("Number of even numbers to check its sum: "))
sumOfEven(number)
os.system("pause")
	