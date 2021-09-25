import os
def summation(n,f,t):
	i = f
	summation = 0
	while (i <= t):
		summation += n ** i
		i += 1
	return summation
number = int(input("Number: "))
from_p = int(input("From power: "))
to = int(input("To power: "))
result = summation(number,from_p,to)
print("Summation:",result)
os.system("pause")