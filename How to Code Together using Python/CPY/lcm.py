import os 
class LCM:
	def __init__(self,n1,n2):
		self.n1 = n1 
		self.n2 = n2 
	def lcm(self):
		if (self.n1 < self.n2):
			min = self.n1 
			max = self.n2 
		else:
			min = self.n2 
			max = self.n1 
		i = 1
		while (i <= max):
			result = max * i 
			if (result % min == 0):
				lcm = result
				break
			i += 1
		print("LCM:",lcm)
num1 = int(input("Num1 = "))
num2 = int(input("Num2 = "))
x = LCM(num1,num2)
x.lcm()
os.system("pause")