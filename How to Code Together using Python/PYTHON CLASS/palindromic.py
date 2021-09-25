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
			print(n,"is palindromic.")
		else:
			print(n,"is not palindromic.")
x = PalindromicNumber()
number = int(input("Number to check if palindromic: "))
x.isPalindromic(number)
os.system("pause")