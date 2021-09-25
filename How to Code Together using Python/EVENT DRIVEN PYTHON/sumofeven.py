import os
def sumOfEven(n):
	for i in range(1, (n + 1) * 2):
		if (i % 2 == 0):
			print(i)
	sum = n * (n + 1)
	print("Sum of these even numbers: ", sum)
	return
number = int(input("Number of even numbers: "))
sumOfEven(number)
os.system("pause")
	