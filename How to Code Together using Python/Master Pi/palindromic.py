import os
def isPalindromic(n):
	copy = n
	sum = 0
	while (copy > 0):
		remainder = copy % 10
		sum = (sum * 10) + remainder
		copy = copy // 10
	if (sum == n):
		print(n,"is palindromic.")
	else:
		print(n,"is not palindromic.")
number = int(input("Number to check if palindromic: "))
isPalindromic(number)
os.system("pause")