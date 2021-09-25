import os
def sumUp(n):
	if (n >= 1 and n <= 1000):
		sum = 0
		i = 0
		while (i <= n):
			sum += i
			i += 1
		print("Sum from 1 to ", n, " is ", sum)
	else:
		print("Sorry! Numbers from 1 to 1000 are only allowed.")
	return
number = int(input("Number from 1 to (max: 1000): "))
sumUp(number)
os.system("pause")