import os
def fibonacciArray(terms):
	array = []
	i = 0
	first = 0
	second = 1
	while i < terms:
		array.append(first)
		nextTerm = first + second
		first = second
		second = nextTerm
		i += 1
	print(array)
	return
number_of_terms = int(input("Number of terms in Fibonacci sequence: "))
fibonacciArray(number_of_terms)
os.system("pause")