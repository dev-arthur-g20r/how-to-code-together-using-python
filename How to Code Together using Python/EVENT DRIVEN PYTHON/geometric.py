import os
def geometricSequence(first_term,ratio,terms):
	i = 0
	while i < terms:
		print(first_term)
		nextTerm = first_term * ratio
		first_term = nextTerm
		i += 1
	return
number_of_terms = int(input("Number of terms in Geometric sequence: "))
first = int(input("First term: "))
common_ratio = int(input("Common ratio: "))
geometricSequence(first,common_ratio,number_of_terms)
os.system("pause")