import os
class OddOrEven:
	def ifOddOrEven(self,x):
		if (x % 2 == 0):
			print(x,"is EVEN.")
		else:
			print(x,"is ODD.")
n = OddOrEven()
number = int(input("Number to check if odd or even: "))
n.ifOddOrEven(number)
os.system("pause")