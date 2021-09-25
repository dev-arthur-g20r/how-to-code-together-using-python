import os
def isKaprekar(n):
	square = n ** 2
	sq = str(square)

	if (square < 9):
		sq = "0" + sq
	length = len(sq)

	mid = length // 2

	first = int(sq[0:mid])
	last = int(sq[mid:])

	sum = first + last

	if (sum == n):
		return "{} is Kaprekar.".format(n)
	else:
		return "{} is not Kaprekar.".format(n)

number = int(input("Number to check if Kaprekar: "))
result = isKaprekar(number)
print(result)
os.system("pause")