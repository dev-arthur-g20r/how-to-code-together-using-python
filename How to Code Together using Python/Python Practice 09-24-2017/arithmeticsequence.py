import os
def arithmeticSequence(t,f,d):
	i = 0
	while (i < t):
		print(f)
		nextTerm = f + d
		f = nextTerm
		i += 1
terms = int(input("Number of terms in Arithmetic sequence: "))
first = int(input("First term: "))
difference = int(input("Common difference: "))
arithmeticSequence(terms,first,difference)
os.system("pause")