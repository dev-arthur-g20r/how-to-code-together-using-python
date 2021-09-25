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
			return "{} is Krishnamurthy.".format(self.n)
		else:
			return "{} is not Krishnamurthy.".format(self.n)
number = int(input("Number to check if Krishnamurthy: "))
x = KrishnamurthyNumber(number)
result = x.isKrishnamurthy()
print(result)
os.system("pause")