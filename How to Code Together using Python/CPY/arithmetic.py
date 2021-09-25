import os
class ArithmeticSequence:
	def __init__(self,n,f,d):
		self.n = n 
		self.f = f 
		self.d = d 
	def arithmetic(self):
		i = 0
		while (i < self.n):
			print(self.f)
			nextTerm = self.f + self.d 
			self.f = nextTerm
			i += 1
number = int(input("Number of terms in Arithmetic sequence: "))
first = int(input("First term: "))
difference = int(input("Common difference: "))
sequence = ArithmeticSequence(number,first,difference)
sequence.arithmetic()
os.system("pause")