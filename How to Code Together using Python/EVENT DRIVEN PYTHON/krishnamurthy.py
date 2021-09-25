import os
def krishnaMurthyNumber(n):
	sum = 0
	copy = n
	while (copy > 0):
		remainder = copy % 10
		factorial = 1
		while(remainder > 0):
			factorial *= remainder
			remainder -= 1
		sum += factorial
		copy = copy // 10
	if (n == sum):
		print(n, " is a Krishna Murthy number.")
	else:
		print(n, " is not a Krishna Murthy number.")
	return
number = int(input("Number to check if its a Krishna Murthy number: "))
krishnaMurthyNumber(number)
os.system("pause")