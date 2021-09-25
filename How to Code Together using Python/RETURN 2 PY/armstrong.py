import os
class ArmstrongNumber:
	def isArmstrong(self,n):
		copy = n
		sum = 0
		num = str(n)
		length = len(num)
		while (copy > 0):
			remainder = copy % 10
			sum += remainder ** length
			copy = copy // 10
		if (sum == n):
			return "{} is Armstrong.".format(n)
		else:
			return "{} is not Armstrong.".format(n)
x = ArmstrongNumber()
number = int(input("Number to check if Armstrong: "))
result = x.isArmstrong(number)
print(result)
os.system("pause")