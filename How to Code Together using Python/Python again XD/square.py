import os
def perimeterOfSquare(x):
	p = 4 * x
	print("Perimeter of square:",p)
def areaOfSquare(x):
	a = x ** 2
	print("Area of square:",a)
a = float(input("Side of square: "))
perimeterOfSquare(a)
areaOfSquare(a)
os.system("pause")