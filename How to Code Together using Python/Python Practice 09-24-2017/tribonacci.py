import os
def tribonacci(n):
	first = 0
	second = 1
	third = 1
	i = 0
	while (i < n):
		print(first)
		nextTerm = first + second + third
		first = second
		second = third
		third = nextTerm
		i += 1
number = int(input("Number of terms in Tribonacci sequence: "))
tribonacci(number)
os.system("pause")