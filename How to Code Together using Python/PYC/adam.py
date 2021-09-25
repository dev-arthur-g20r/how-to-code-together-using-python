import os
class AdamNumber:
	def __init__(self,n):
		self.n = n
	def isAdam(self):
		copy1 = self.n 
		sum1 = 0
		square1 = self.n ** 2
		while (copy1 > 0):
			remainder1 = copy1 % 10
			sum1 = (sum1 * 10) + remainder1 
			copy1 = copy1 // 10
		square2 = sum1 ** 2
		copy2 = square2
		sum2 = 0
		while (copy2 > 0):
			remainder2 = copy2 % 10
			sum2 = (sum2 * 10) + remainder2
			copy2 = copy2 // 10
		if (sum2 == square1):
			return "{} is Adam.".format(self.n)
		else:
			return "{} is not Adam.".format(self.n)
number = int(input("Number to check if Adam: "))
x = AdamNumber(number)
result = x.isAdam()
print(result)
os.system("pause")