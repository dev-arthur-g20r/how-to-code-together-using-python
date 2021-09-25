import os
class DisariumNumber:
	def isDisarium(self,n):
		copy = n
		sum = 0
		num = str(n)
		length = len(num)
		while (copy > 0):
			remainder = copy % 10
			sum += remainder ** length
			length -= 1
			copy = copy // 10
		if (sum == n):
			return "{} is Disarium.".format(n)
		else:
			return "{} is not Disarium.".format(n)
x = DisariumNumber()
number = int(input("Number to check if Disarium: "))
result = x.isDisarium(number)
print(result)
os.system("pause")