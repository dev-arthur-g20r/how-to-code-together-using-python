import os
def perimeterOfSquare(a):
	p = 4 * a
	print("Perimeter of square: {0:.03f}".format(p))
def areaOfSquare(a):
	ar = a ** 2
	print("Area of square: {0:.03f}".format(ar))
print("Enter dimension of square: ")
side = float(input("Side = "))
perimeterOfSquare(side)
areaOfSquare(side)
os.system("pause")