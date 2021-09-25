import os
class GeometricSequence:
	def geometric(self,n,f,r):
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
sequence.geometric(number,first,ratio)
os.system("pause")