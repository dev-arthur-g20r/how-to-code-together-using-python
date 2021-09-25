import os
def checkIfPalindromic(n):
	copy = n
	sum = 0
	while (copy > 0):
		remainder = copy % 10
		sum = (sum * 10) + remainder
		copy = copy // 10
	if (n == sum):
		print(n, " is Palindromic.")
	else:
		print(n, " is not Palindromic.")
	return
number = int(input("Number to check if Palindromic: "))
checkIfPalindromic(number)
os.system("pause")