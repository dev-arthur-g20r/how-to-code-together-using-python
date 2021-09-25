import os
def checkOddOrEven(f,l):
	for i in range(f,l + 1):
		if (i % 2 == 0):
			print(i, " - EVEN")
		else:
			print(i, " - ODD")
	return
fr = int(input("Number from: "))
to = int(input("Number to: "))
checkOddOrEven(fr,to)
os.system("pause")