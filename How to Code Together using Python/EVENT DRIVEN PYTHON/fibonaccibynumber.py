import os
def fibonacci(n):
	x = 1
	y = 1
	while x <= n:
		print(x)
		x, y = y, x + y
	return
number = int(input("Fibonacci sequence from 1 to: "))
fibonacci(number)
os.system("pause")