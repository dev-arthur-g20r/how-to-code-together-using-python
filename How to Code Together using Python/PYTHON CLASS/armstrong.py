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
			print(n,"is Armstrong.")
		else:
			print(n,"is not Armstrong.")
x = ArmstrongNumber()
number = int(input("Number to check if Armstrong: "))
x.isArmstrong(number)
os.system("pause")