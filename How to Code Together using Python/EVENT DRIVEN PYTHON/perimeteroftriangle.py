import os
def perimeterOfTriangle(a,b,c):
	p = a + b + c
	return p
print("Enter length of two sides and base to check perimeter of the triangle.")
base = float(input("Base: "))
side1 = float(input("Side 1: "))
side2 = float(input("Side 2: "))
perimeter = perimeterOfTriangle(side1,base,side2)
print("Perimeter of triangle: ", perimeter)
os.system("pause")