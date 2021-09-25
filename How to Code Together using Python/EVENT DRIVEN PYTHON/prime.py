import os
def checkIfPrime(n):
	isPrime = True
	i = 2
	while i <= n / 2:
		test = n % i
		if (test == 0):
			isPrime = False
			break
		i += 1
	if (isPrime == True and n > 1):
		print(n, " is prime.")
	else:
		print(n, " is not prime.")
	return
number = int(input("Number to check if prime: "))
checkIfPrime(number)
os.system("pause")