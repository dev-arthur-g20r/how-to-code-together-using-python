import os
class OddOrEven:
	def __init__(self,n):
		self.n = n
	def isOddOrEven(self):
		if (self.n % 2 == 0):
			print(self.n,"is EVEN.")
		else:
			print(self.n,"is ODD.")
number = int(input("Number to check if odd or even: "))
x = OddOrEven(number)
x.isOddOrEven()
os.system("pause")