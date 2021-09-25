import os
def perimeterOfSquare(s):
	p = s * 4
	return p
side = float(input("Enter length of a side of square to check its perimeter: "))
perimeter = perimeterOfSquare(side)
print("Perimeter of square: ", perimeter)
os.system("pause")