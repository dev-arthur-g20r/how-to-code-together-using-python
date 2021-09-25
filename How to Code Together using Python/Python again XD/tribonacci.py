import os
def tribonacci(n):
	i = 0
	first = 0
	second = 1
	third = 1
	while (i < n):
		print(first)
		nextTerm = first + second + third
		first = second
		second = third
		third = nextTerm
		i += 1
terms = int(input("Number of terms in Tribonacci sequence: "))
tribonacci(terms)
os.system("pause")