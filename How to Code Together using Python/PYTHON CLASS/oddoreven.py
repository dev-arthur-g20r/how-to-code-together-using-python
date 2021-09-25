import os
class OddOrEven:
	def isOddOrEven(self,n):
		if (n % 2 == 0):
			print(n,"is EVEN.")
		else:
			print(n,"is ODD.")
x = OddOrEven()
number = int(input("Number to check if odd or even: "))
x.isOddOrEven(number)
os.system("pause")