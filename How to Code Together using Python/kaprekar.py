import os
def checkIfKaprekarNumber(n):
	sq = int(pow(int(n),2))
	s = str(sq)
	if(sq <= 9):
		s = "0" + sq
	length = len(s)
	mid = int(length) / 2
	left = str(s[0:int(mid)])
	right = str(s[int(mid):])
	l = int(left)
	r = int(right)
	sum = int(l) + int(r)
	if (int(sum) == int(n)):
		print ("%d is a Kaprekar number." % int(n))
	else:
		print ("%d is not a Kaprekar number." % int(n))
	return
num = input("Number: ")
checkIfKaprekarNumber(int(num))
os.system("pause")