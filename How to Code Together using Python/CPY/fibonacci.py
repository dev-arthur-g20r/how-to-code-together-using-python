import os
class FibonacciSequence:
	def __init__(self,n):
		self.n = n 
	def fibonacci(self):
		first = 0
		second = 1
		i = 0
		while (i < self.n):
			print(first)
			nextTerm = first + second 
			first = second
			second = nextTerm
			i += 1
number = int(input("Number of terms in Fibonacci sequence: "))
sequence = FibonacciSequence(number)
sequence.fibonacci()
os.system("pause")