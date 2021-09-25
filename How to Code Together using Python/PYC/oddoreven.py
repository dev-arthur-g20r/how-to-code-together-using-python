import os
class OddOrEven:
	def __init__(self,n):
		self.n = n
	def isOddOrEven(self):
		if (self.n % 2 == 0):
			return "{} is EVEN.".format(self.n)
		else:
			return "{} is ODD.".format(self.n)
number = int(input("Number to check if odd or even: "))
x = OddOrEven(number)
result = x.isOddOrEven()
print(result)
os.system("pause")