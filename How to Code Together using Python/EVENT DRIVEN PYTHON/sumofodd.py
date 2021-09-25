import os
def sumOfOdd(n):
	for i in range(1, n * 2):
		if (i % 2 == 1):
			print(i)
	sum = n ** 2
	print("Sum of these even numbers: ", sum)
	return
number = int(input("Number of even numbers: "))
sumOfOdd(number)
os.system("pause")