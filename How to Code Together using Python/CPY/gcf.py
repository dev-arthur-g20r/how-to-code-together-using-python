import os
class GCF:
	def __init__(self,n1,n2):
		self.n1 = n1 
		self.n2 = n2 
	def gcf(self):
		while (self.n2 > 0):
			remainder = self.n1 % self.n2 
			self.n1 = self.n2 
			self.n2 = remainder
		print("GCF:",self.n1)
num1 = int(input("Num1 = "))
num2 = int(input("Num2 = "))
x = GCF(num1,num2)
x.gcf()
os.system("pause")