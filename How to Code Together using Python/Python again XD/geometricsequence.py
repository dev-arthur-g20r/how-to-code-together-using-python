import os
def geometricSequence(n,f,r):
	i = 0
	while (i < n):
		print(f)
		nextTerm = f * r
		f = nextTerm
		i += 1
terms = int(input("Number of terms in Geometric sequence: "))
first = int(input("First term: "))
ratio = int(input("Common ratio: "))
geometricSequence(terms,first,ratio)
os.system("pause")