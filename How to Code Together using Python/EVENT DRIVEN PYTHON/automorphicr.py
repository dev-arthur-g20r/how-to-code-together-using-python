import os
def checkIfAutomorphic(n):
	square = int(n ** 2)
	strsquare = str(square)
	nstr = str(n)
	if (strsquare.endswith(nstr) == True):
		print(n, " is automorphic.")
	else:
		print(n, " is not automorphic.")
	return
num = int(input("Enter number to check if automorphic: "))
checkIfAutomorphic(num)
os.system("pause")