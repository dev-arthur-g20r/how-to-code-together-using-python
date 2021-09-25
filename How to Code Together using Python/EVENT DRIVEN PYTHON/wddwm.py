import os
def multiplicationTable(n):
	if (n > 0):
		product = 1
		for i in range(1, 11):
			product = n * i
			print(n, " X ", i, " = ", product)
	else:
		print("Sorry! Numbers greater than 0 are only allowed.")
	return
number = int(input("Any number greater than 0: "))
multiplicationTable(number)
os.system("pause")