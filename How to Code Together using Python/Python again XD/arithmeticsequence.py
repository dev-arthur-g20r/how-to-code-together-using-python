import os
def arithmeticSequence(n,f,d):
	i = 0
	while (i < n):
		print(f)
		nextTerm = f + d
		f = nextTerm
		i += 1
terms = int(input("Number of terms in Fibonacci sequence: "))
first = int(input("First term: "))
difference = int(input("Common difference: "))
arithmeticSequence(terms,first,difference)
os.system("pause")