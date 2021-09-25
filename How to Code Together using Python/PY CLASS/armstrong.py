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
			print(self.n,"is Armstrong.")
		else:
			print(self.n,"is not Armstrong.")
number = int(input("Number to check if Armstrong: "))
x = ArmstrongNumber(number)
x.isArmstrong()
os.system("pause")