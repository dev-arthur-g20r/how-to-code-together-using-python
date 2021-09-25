import os
def multiplicationTable(n):
	i = 1
	while (i <= 10):
		print("{} X {} = {}".format(n,i,(n * i)))
		i += 1
number = int(input("Number to check its 10 multiples: "))
multiplicationTable(number)
os.system("pause")