import os
def checkIfKaprekar(n):
	square = n ** 2
	sq = str(square)
	if (square <= 9):
		sq = "0" + sq
	length = len(sq)
	mid = int(length / 2)
	left = str(sq[0:mid])
	right = str(sq[mid:])
	l = int(left)
	r = int(right)
	sum = l + r
	if (sum == n):
		print(n, " is a Kaprekar number.")
	else:
		print(n , " is not a Kaprekar number.")
	return
number = int(input("Enter the number to check if it's a Kaprekar number: "))
checkIfKaprekar(number)
os.system("pause")