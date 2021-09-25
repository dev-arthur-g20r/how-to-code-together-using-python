import os
def fibonacci(terms):
	counter = 0
	first = 0
	second = 1
	while counter < terms:
		if(terms > 0):
			print(first)
			nextTerm = first + second
			first = second
			second = nextTerm
			counter += 1
	return
number_of_terms = int(input("Number of terms to create a Fibonacci sequence: "))
fibonacci(number_of_terms)
os.system("pause")