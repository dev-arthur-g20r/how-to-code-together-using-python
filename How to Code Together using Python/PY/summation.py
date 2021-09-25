import os
class Summation:
	def __init__(self,n,f,t):
		self.f = f
		self.n = n 
		self.t = t 
	def summation(self):
		sum = 0 
		i = self.f 
		while (i <= self.t):
			sum += self.n ** i
			i += 1
		return "Summation: {}".format(sum)
number = int(input("Number: "))
from_p = int(input("From power: "))
to = int(input("To power: "))
x = Summation(number,from_p,to)
result = x.summation()
print(result)
os.system("pause")