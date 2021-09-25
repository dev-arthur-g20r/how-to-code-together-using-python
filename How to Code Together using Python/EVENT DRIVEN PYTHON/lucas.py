import os
def lucasSeries(terms):
	first = 2
	second = 1
	i = 0
	while i < terms:
		print(first)
		nextTerm = first + second
		first = second
		second = nextTerm
		i += 1
	return
number_of_terms = int(input("Number of terms in Lucas series: "))
lucasSeries(number_of_terms)
os.system("pause")