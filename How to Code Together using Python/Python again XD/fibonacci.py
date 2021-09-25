import os
def fibonacci(n):
	first = 0
	second = 1
	i = 0
	while (i < n):
		print(first)
		nextTerm = first + second
		first = second
		second = nextTerm
		i += 1
terms = int(input("Number of terms in Fibonacci sequence: "))
fibonacci(terms)
os.system("pause")