import os
def naturalSum(n):
	sum = 0
	sum = n * (n + 1) / 2
	print("Sum of ", n, " natural numbers is ", sum)
	return
number = int(input("Enter a number to check its with its natural numbers behind it: "))
naturalSum(number)
os.system("pause")