import os
def fibonacci(n):
	i = 0
	first = 0
	second = 1
	while (i < n):
		print(first)
		nextTerm = first + second
		first = second
		second = nextTerm
		i += 1
number = int(input("Number of terms in Fibonacci sequence: "))
fibonacci(number)
os.system("pause")