import os
def checkIfRightTriangle(x,y,z):
	xsquare = x ** 2
	ysquare = y ** 2
	zsquare = z ** 2
	if (zsquare == xsquare + ysquare):
		print("Right triangle")
	else:
		print("Not a right triangle")
	return
a = float(input("a = "))
b = float(input("b = "))
c = float(input("c = "))
checkIfRightTriangle(a,b,c)
os.system("pause")