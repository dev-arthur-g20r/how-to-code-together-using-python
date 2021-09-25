import os
class SumOfEven:
	def sumOfEven(self,n):
		i = 1
		sum = n * (n + 1)
		while (i <= n * 2):
			if (i % 2 == 0):
				print(i)
			i += 1
		return sum
x = SumOfEven()
number = int(input("Number of even numbers: "))
result = x.sumOfEven(number)
print("Sum of these even numbers:",result)
os.system("pause")