import os
class GeometricSequence:
	def geometricSequence(self,n,f,r):
		i = 0
		while (i < n):
			print(f)
			nextTerm = f * r
			f = nextTerm
			i += 1
sequence = GeometricSequence()
number = int(input("Number of terms in Geometric sequence: "))
first = int(input("First term: "))
ratio = int(input("Common ratio: "))
sequence.geometricSequence(number,first,ratio)
os.system("pause")