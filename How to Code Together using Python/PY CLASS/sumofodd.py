import os
class SumOfOdd:
	def __init__(self,n):
		self.n = n
	def sumOfOdd(self):
		sum = self.n ** 2
		i = 1
		while (i <= self.n * 2):
			if (i % 2 == 1):
				print(i)
			i += 1
		print("Sum:",sum)
number = int(input("Number of even numbers: "))
x = SumOfOdd(number)
x.sumOfOdd()
os.system("pause")