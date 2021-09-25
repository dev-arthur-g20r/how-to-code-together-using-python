import os
def isPrime(n):
	isPrime = True
	i = 2
	while (i <= n / 2):
		checker = n % i
		if (checker == 0):
			isPrime = False
			break
		i += 1
	if (isPrime and n > 1):
		print(n,"is prime.")
	else:
		print(n,"is not prime.")
number = int(input("Number to check if prime: "))
isPrime(number)
os.system("pause")