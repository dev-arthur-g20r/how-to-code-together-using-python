import os
def lucas(n):
	first = 2
	second = 1
	i = 0
	while i < n:
		print(first)
		nextTerm = first + second
		first = second
		second = nextTerm
		i += 1
number = int(input("Number of terms in Lucas series: "))
lucas(number)
os.system("pause")