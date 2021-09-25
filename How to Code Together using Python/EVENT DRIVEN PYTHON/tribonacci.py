import os
def tribonacci(terms):
	counter = 0
	first = 0
	second = 1
	third = 1
	while counter < terms:
		print(first)
		nextTerm = first + second + third
		first = second
		second = third
		third = nextTerm
		counter = counter + 1
	return
number = int(input("Enter number of terms for Tribonacci sequence: "))
tribonacci(number)
os.system("pause")