import os
class PalindromicNumber:
	def __init__(self,n):
		self.n = n 
	def isPalindromic(self):
		copy = self.n
		sum = 0
		while (copy > 0):
			remainder = copy % 10
			sum = (sum * 10) + remainder
			copy = copy // 10
		if (sum == self.n):
			return "{} is palindromic.".format(self.n)
		else:
			return "{} is not palindromic.".format(self.n)
number = int(input("Number to check if palindromic: "))
x = PalindromicNumber(number)
result = x.isPalindromic()
print(result)
os.system("pause")