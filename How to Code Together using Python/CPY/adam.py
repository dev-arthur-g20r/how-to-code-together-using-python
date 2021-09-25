import os
class AdamNumber:
	def __init__(self,n):
		self.n = n
	def isAdam(self):
		copy1 = self.n 
		square1 = self.n ** 2
		sum1 = 0
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
			print(self.n,"is Adam.")
		else:
			print(self.n,"is not Adam.")
number = int(input("Number to check if Adam: "))
x = AdamNumber(number)
x.isAdam()
os.system("pause")