import os
class ArmstrongNumber:
	def __init__(self,n):
		self.n = n 
	def isArmstrong(self):
		copy = self.n
		sum = 0
		num = str(self.n)
		length = len(num)
		while (copy > 0):
			remainder = copy % 10
			sum += remainder ** length 
			copy = copy // 10
		if (sum == self.n):
			return "{} is Armstrong.".format(self.n)
		else:
			return "{} is not Armstrong.".format(self.n)
number = int(input("Number to check if Armstrong: "))
x = ArmstrongNumber(number)
result = x.isArmstrong()
print(result)
os.system("pause")