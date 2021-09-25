import os
def primeCheck(n):
	isPrime = True
	i = 2
	while (i <= n / 2):
		result = n % i
		if (result == 0):
			isPrime = False
			break
		i += 1
	if (isPrime and n > 1):
		print(n,"is prime.")
	else:
		print(n,"is not prime.")
number = int(input("Number to check if prime: "))
primeCheck(number)
os.system("pause")