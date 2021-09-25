import os
class GCF:
	def gcf(self,number1,number2):
		while (number2 > 0):
			remainder = number1 % number2
			number1 = number2
			number2 = remainder
		print("GCF:",number1)
x = GCF()
num1 = int(input("Num1 = "))
num2 = int(input("Num2 = "))
x.gcf(num1,num2)
os.system("pause")