import os
class PrimeNumber:
	def isPrime(self,n):
		isPrime = True
		i = 2
		while (i <= n / 2):
			result = n % i
			if (result == 0):
				isPrime = False
				break
			i += 1
		if (isPrime and n > 1):
			return "{} is prime.".format(n)
		else:
			return "{} is not prime.".format(n)
x = PrimeNumber()
number = int(input("Number to check if prime: "))
result = x.isPrime(number)
print(result)
os.system("pause")