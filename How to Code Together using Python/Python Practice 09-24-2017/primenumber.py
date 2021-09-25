import os
def isPrime(n):
	isPrime = True
	i = 2
	while (i <= n / 2):
		result = n % i
		if (result == 0):
			isPrime = False
			break
		i += 1
	if (isPrime and n > 1):
		return "is prime."
	else:
		return "is not prime."
number = int(input("Number to check if its prime: "))
result = isPrime(number)
print(number,result)
os.system("pause")