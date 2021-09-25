import os
class GeometricSequence:
	def __init__(self,n,f,r):
		self.n = n 
		self.f = f 
		self.r = r
	def geometric(self):
		i = 0
		while (i < self.n):
			print(self.f)
			nextTerm = self.f * self.r 
			self.f = nextTerm
			i += 1
number = int(input("Number of terms in Geometric sequence: "))
first = int(input("First term: "))
ratio = int(input("Common ratio: "))
sequence = GeometricSequence(number,first,ratio)
sequence.geometric()
os.system("pause")