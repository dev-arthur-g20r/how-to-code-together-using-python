import os
class DisariumNumber:
	def __init__(self,n):
		self.n = n 
	def isDisarium(self):
		copy = self.n 
		sum = 0 
		num = str(self.n) 
		length = len(num)
		while (copy > 0):
			remainder = copy % 10
			sum += remainder ** length
			length -= 1
			copy = copy // 10
		if (sum == self.n):
			print(self.n,"is Disarium")
		else:
			print(self.n,"is not Disarium.")
number = int(input("Number to check if Disarium: "))
x = DisariumNumber(number)
x.isDisarium()
os.system("pause")