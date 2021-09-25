import os
def fibonacci(n):
	first = 1
	second = 1
	while (first <= n):
		print(first)
		nextTerm = first + second
		first = second
		second = nextTerm
terms = int(input("Possible last term in fibonacci sequence: "))
fibonacci(terms)
os.system("pause")