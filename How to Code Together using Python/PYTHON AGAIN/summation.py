import os
def summation(n,f,t):
	sum = 0
	i = f
	while i <= t:
		sum += n ** i
		i += 1
	print("Summation:",sum)
number = int(input("Number: "))
from_p = int(input("From power: "))
to = int(input("To power: "))
summation(number,from_p,to)
os.system("pause")