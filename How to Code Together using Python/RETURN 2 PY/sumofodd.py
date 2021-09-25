import os
class SumOfOdd:
	def sumOfOdd(self,n):
		sum = n ** 2
		i = 1
		while (i <= n * 2):
			if (i % 2 == 1):
				print(i)
			i += 1
		return sum
x = SumOfOdd()
number = int(input("Number of odd numbers: "))
result = x.sumOfOdd(number)
print("Sum of these odd numbers:",result)
os.system("pause")