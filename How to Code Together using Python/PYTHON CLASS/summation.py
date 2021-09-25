import os
class Summation:
	def summation(self,n,f,t):
		sum = 0
		i = f
		while (i <= t):
			sum += n ** i
			i += 1
		print("Summation:",sum)
x = Summation()
number = int(input("Number: "))
from_p = int(input("From power: "))
to = int(input("To power: "))
x.summation(number,from_p,to)
os.system("pause")