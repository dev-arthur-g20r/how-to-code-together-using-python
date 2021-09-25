import os
import sys
def powerOfTwo(n):
	first = 1
	ratio = 2
	i = 0
	powers = []
	while (i < 95):
		powers.append(first)
		nextTerm = first * ratio
		first = nextTerm
		i += 1
	if (n in powers):
		print (n, " is a power of two.")
	else:
		print(n, " is not a power of two.")
	return
number = int(input("Number to check if power of two: "))
powerOfTwo(number)
os.system("pause")