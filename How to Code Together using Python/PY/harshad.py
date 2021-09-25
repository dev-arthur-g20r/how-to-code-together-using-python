import os
class HarshadNumber:
	def __init__(self,n):
		self.n = n 
	def isHarshad(self):
		copy = self.n
		sum = 0
		while (copy > 0):
			remainder = copy % 10
			sum += remainder 
			copy = copy // 10
		if (self.n % sum == 0):
			return "{} is Harshad.".format(self.n)
		else:
			return "{} is not Harshad.".format(self.n)
number = int(input("Number to check if Harshad: "))
x = HarshadNumber(number)
result = x.isHarshad()
print(result)
os.system("pause")