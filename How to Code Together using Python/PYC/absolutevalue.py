import os
class AbsoluteValue:
	def __init__(self,n):
		self.n = n
	def absValue(self):
		if (self.n < 0):
			abs = self.n * -1
		else:
			abs = self.n 
		return "Absolute value: {}".format(abs)
number = float(input("Number to check its absolute value: "))
x = AbsoluteValue(number)
result = x.absValue()
print(result)
os.system("pause")