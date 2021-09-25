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
			return "{} is Disarium.".format(self.n)
		else:
			return "{} is not Disarium.".format(self.n)
number = int(input("Number to check if Disarium: "))
x = DisariumNumber(number)
result = x.isDisarium()
print(result)
os.system("pause")