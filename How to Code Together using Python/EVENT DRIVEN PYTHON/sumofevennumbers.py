import os
def sumOfEvenNumbers(n):
	sum = 0
	sum = n ** 2 + n
	print("Sum of ", n, " consecutive even numbers is ", sum)
	return
num = int(input("Input number to check its sum of even numbers: "))
sumOfEvenNumbers(num)
os.system("pause")