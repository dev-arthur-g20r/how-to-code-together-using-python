import os
class ArithmeticSequence:
	def arithmetic(self,n,f,d):
		i = 0
		while (i < n):
			print(f)
			nextTerm = f + d
			f = nextTerm
			i += 1
sequence = ArithmeticSequence()
number = int(input("Number of terms in Arithmetic sequence: "))
first = int(input("First term: "))
difference = int(input("Common difference: "))
sequence.arithmetic(number,first,difference)
os.system("pause")