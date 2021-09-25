import os
class HarshadNumber:
	def isHarshad(self,n):
		copy = n
		sum = 0
		while (copy > 0):
			remainder = copy % 10
			sum += remainder
			copy = copy // 10
		if (n % sum == 0):
			return "{} is Harshad.".format(n)
		else:
			return "{} is not Harshad.".format(n)
x = HarshadNumber()
number = int(input("Number to check if Harshad: "))
result = x.isHarshad(number)
print(result)
os.system("pause")