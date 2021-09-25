import os
class GCF:
	def gcf(self,n1,n2):
		while (n2 > 0):
			remainder = n1 % n2
			n1 = n2
			n2 = remainder
		print("GCF:",n1)
n = GCF()
num1 = int(input("Num1: "))
num2 = int(input("Num2: "))
n.gcf(num1,num2)
os.system("pause")