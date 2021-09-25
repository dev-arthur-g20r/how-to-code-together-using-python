import os

def checkIfPrime(x):
	isPrime = True
	i = 2
	while (int(i) <= int(x) / 2):
		temp = int(num) % int(i)
		if (int(temp) == 0):
			isPrime = False
			break
		i = int(i) + 1
	if (isPrime == True and int(num) != 0 and int(num) != 1 and int(num) > 0):
		print ("%d is prime." % int(x))
	else:
		print ("%d is not prime." % int(x))
	return
	
num = input("Please enter number to check if prime or not: ")
checkIfPrime(int(num))

os.system("pause")