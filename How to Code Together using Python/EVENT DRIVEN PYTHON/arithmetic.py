import os
def arithmeticSequence(first_term,difference,terms):
	i = 0
	while i < terms:
		print(first_term)
		nextTerm = first_term + difference
		first_term = nextTerm
		i += 1
	return
number_of_terms = int(input("Number of terms in Arithmetic sequence: "))
first = int(input("First number in Arithmetic sequence: "))
common_difference = int(input("Common difference: "))
arithmeticSequence(first,common_difference,number_of_terms)
os.system("pause")