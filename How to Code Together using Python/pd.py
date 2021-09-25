import os
def squareRoot(n):
	#A square root of a number is that number raised to 1/2 (number ^ 1/2) 
	#since it is the reversed version of n squared (number ^ 2)
	square_root = n ** 0.5
	return "Square root: {0:.11f}".format(square_root)
def main():
	number = float(input("Number to check square root: "))
	result = squareRoot(number)
	print(result)
	main()
main()
os.system("pause")