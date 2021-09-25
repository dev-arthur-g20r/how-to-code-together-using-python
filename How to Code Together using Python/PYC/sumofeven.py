import os
class SumOfEven:
	def __init__(self,n):
		self.n = n 
	def sumOfEven(self):
		sum = self.n * (self.n + 1)
		i = 1
		while (i <= self.n * 2):
			if (i % 2 == 0):
				print(i)
			i += 1
		print("Sum of these even numbers:",sum)
number = int(input("Number of even numbers: "))
x = SumOfEven(number)
x.sumOfEven()
os.system("pause")
		