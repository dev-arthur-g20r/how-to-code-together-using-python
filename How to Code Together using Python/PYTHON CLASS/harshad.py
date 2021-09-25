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
			print(n,"is Harshad.")
		else:
			print(n,"is not Harshad.")
x = HarshadNumber()
number = int(input("Number to check if Harshad: "))
x.isHarshad(number)
os.system("pause")