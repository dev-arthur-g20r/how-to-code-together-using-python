import os
def woo(n):
	i = n
	j = n - (n - 1)
	sum = 0
	while (i > 0 and j <= i):
		res = int(str(i)+"000"+str(j))
		print(res)
		sum += res
		i -= 1
		j += 1
	print(sum)
number = int(input("Number: "))
woo(number)
os.system("pause")