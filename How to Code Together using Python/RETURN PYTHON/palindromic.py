import os
class PalindromicNumber:
	def isPalindromic(self,n):
		copy = n
		sum = 0
		while (copy > 0):
			remainder = copy % 10
			sum = (sum * 10) + remainder
			copy = copy // 10
		if (sum == n):
			return "{} is palindromic.".format(n)
		else:
			return "{} is not palindromic.".format(n)
x = PalindromicNumber()
number = int(input("Number to check if palindromic: "))
result = x.isPalindromic(number)
print(result)
os.system("pause")