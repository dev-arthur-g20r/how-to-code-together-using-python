import os
class PrimeNumber:
	def __init__(self,n):
		self.n = n 
	def isPrime(self):
		isPrime = True
		i = 2
		while (i <= self.n / 2):
			result = self.n % i 
			if (result == 0):
				isPrime = False
				break
			i += 1
		if (isPrime and self.n > 1):
			print(self.n,"is prime.")
		else:
			print(self.n,"is not prime.")
number = int(input("Number to check if prime: "))
x = PrimeNumber(number)
x.isPrime()
os.system("pause")