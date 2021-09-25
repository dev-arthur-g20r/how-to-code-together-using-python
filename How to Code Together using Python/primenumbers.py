import os

def checkIfPrime(x):
	isPrime = True
	i = 2
	while(i <= int(x)/2):
		temp = int(x) % int (i)
		if (temp == 0):
			isPrime = False
			break
		i = int(i) + 1
	if (isPrime == True and int(x) > 0 and int(x) != 1 and int(x) != 0):
		print ("%d is prime." % int(x))
	else:
		print ("%d is not prime." % int(x))
	return
	
num = input("Number to check if prime: ")
checkIfPrime(int(num))

os.system("pause")