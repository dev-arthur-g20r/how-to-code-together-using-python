import os
def isPalindromic(n):
	sum = 0
	copy = n
	while (copy > 0):
		remainder = copy % 10
		sum = remainder + (sum * 10)
		copy = copy // 10
	if (sum == n):
		return "{} is palindromic.".format(n)
	else:
		return "{} is not palindromic.".format(n)
number = int(input("Number to check if palindromic: "))
result = isPalindromic(number)
print(result)
os.system("pause")