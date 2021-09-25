import os
def checkIfAutomorphic(x):
	sqr = pow(int(x),2)
	strsqr = str(sqr)
	xstr = str(x)
	if (strsqr.endswith(xstr) == True):
		print ("%d is automorphic." % int(x))
	else:
		print ("%d is not automorphic." % int(x))
	return
num = input("Number: ")
checkIfAutomorphic(int(num))
os.system("pause")