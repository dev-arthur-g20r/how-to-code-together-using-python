import os
class OddOrEven:
	def oddOrEven(self,n):
		if (n % 2 == 0):
			return "{} is EVEN.".format(n)
		else:
			return "{} is ODD.".format(n)
x = OddOrEven()
number = int(input("Number to check if odd or even: "))
result = x.oddOrEven(number)
print(result)
os.system("pause")