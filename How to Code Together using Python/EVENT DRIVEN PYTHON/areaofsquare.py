import os
def areaOfSquare(s):
	a = s ** 2
	return a
side = float(input("Enter length of a side of a square to check its area: "))
area = areaOfSquare(side)
print("Area of square: ", area)
os.system("pause")