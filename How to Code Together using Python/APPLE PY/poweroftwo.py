import os
def isPowerOfTwo(n):
	f = 1
	r = 2
	i = 0
	powers = []
	while (i < 95):
		powers.append(f)
		nextTerm = f * r
		f = nextTerm
		i += 1
	if (n in powers):
		print(n,"is a power of two.")
	else:
		print(n,"is not a power of two.")
number = int(input("Number to check if power of two: "))
isPowerOfTwo(number)
os.system("pause")