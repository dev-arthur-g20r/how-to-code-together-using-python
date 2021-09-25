import os
def arithmeticSequence(n,f,d):
	i = 0
	while (i < n):
		print(f)
		nextTerm = f + d
		f = nextTerm
		i += 1
number = int(input("Number of terms in Arithmetic sequence: "))
first = int(input("First term: "))
difference = int(input("Common difference: "))
arithmeticSequence(number,first,difference)
os.system("pause")