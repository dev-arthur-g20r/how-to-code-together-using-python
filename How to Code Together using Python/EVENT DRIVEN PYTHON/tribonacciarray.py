import os
def tribonacciArray(terms):
	i = 0
	first = 0
	second = 1
	third = 1
	array = []
	while i < terms:
		array.append(first)
		nextTerm = first + second + third
		first = second
		second = third
		third = nextTerm
		i += 1
	print(array)
	return
number_of_terms = int(input("Number of terms in Tribonacci sequence: "))
tribonacciArray(number_of_terms)
os.system("pause")