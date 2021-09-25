import os
def ifHarshad(n):
	copy = n
	sum = 0
	while (copy > 0):
		remainder = copy % 10
		sum += remainder
		copy = copy // 10
	if (n % sum == 0):
		print(n,"is Harshad.")
	else:
		print(n,"is not Harshad.")
number = int(input("Number to check if Harshad: "))
ifHarshad(number)
os.system("pause")