import os
def summation(n,f,t):
	i = f
	sum = 0
	while (i <= t):
		sum += n ** i
		i += 1
	print("Summation:",sum)
number = int(input("Number: "))
from_p = int(input("From power: "))
to = int(input("To power: "))
summation(number,from_p,to)
os.system("pause")