import os
class PalindromicNumber:
	def __init__(self,n):
		self.n = n
	def isPalindromic(self):
		sum = 0
		copy = self.n
		while (copy > 0):
			remainder = copy % 10
			sum = (sum * 10) + remainder
			copy = copy // 10
		if (sum == self.n):
			print(self.n,"is palindromic.")
		else:
			print(self.n,"is not palindromic.")
number = int(input("Number to check if palindromic: "))
x = PalindromicNumber(number)
x.isPalindromic()
os.system("pause")