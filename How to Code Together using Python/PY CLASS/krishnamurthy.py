import os
class KrishnamurthyNumber:
	def __init__(self,n):
		self.n = n 
	def isKrishnamurthy(self):
		copy = self.n
		sum = 0
		while (copy > 0):
			remainder = copy % 10
			factorial = 1
			while (remainder > 0):
				factorial *= remainder
				remainder -= 1
			sum += factorial
			copy = copy // 10
		if (sum == self.n):
			print(self.n,"is Krishnamurthy.")
		else:
			print(self.n,"is not Krishnamurthy.")
number = int(input("Number to check if Krishnamurthy: "))
x = KrishnamurthyNumber(number)
x.isKrishnamurthy()
os.system("pause")