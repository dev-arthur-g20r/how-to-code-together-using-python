import os
def isPalindromic(n):
	copy = n
	sum = 0
	while (copy > 0):
		remainder = copy % 10
		sum = (sum * 10) + remainder
		copy = copy // 10
	if (sum == n):
		return "is Palindromic."
	else:
		return "is not Palindromic."
number = int(input("Number to check if palindromic: "))
result = isPalindromic(number)
print(number,result)
os.system("pause")