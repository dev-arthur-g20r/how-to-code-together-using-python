import os
class FibonacciSequence:
	def fibonacci(self,n):
		first = 0
		second = 1
		i = 0
		while (i < n):
			print(first)
			nextTerm = first + second
			first = second
			second = nextTerm
			i += 1
sequence = FibonacciSequence()
number = int(input("Number of terms in Fibonacci sequence: "))
sequence.fibonacci(number)
os.system("pause")