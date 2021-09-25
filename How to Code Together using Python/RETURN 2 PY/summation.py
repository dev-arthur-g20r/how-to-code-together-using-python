import os
class Summation:
	def summation(self,n,f,t):
		sum = 0
		i = f
		while (i <= t):
			sum += n ** i
			i += 1
		return sum 
x = Summation()
number = int(input("Number: "))
from_p = int(input("From power: "))
to = int(input("To power: "))
result = x.summation(number,from_p,to)
print("Summation:",result)
os.system("pause")