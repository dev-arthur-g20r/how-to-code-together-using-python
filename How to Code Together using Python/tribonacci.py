import os
def tribonacciSeq(terms):
	print ("Tribonacci Sequence: ")
	first = 0
	second = 1
	third = 1
	print ("%d" % int(first))
	print ("%d" % int(second))
	print ("%d" % int(third))
	d = 0
	i = 4
	while(int(i) < int(terms)):
		sum = int(first) + int(second) + int(third)
		print ("%d" % int(sum))
		first = int(second)
		second = int(third)
		third = int(sum)
		i = int(i) + 1
	return
num = input("Number of terms: ")
tribonacciSeq(int(num))
os.system("pause")