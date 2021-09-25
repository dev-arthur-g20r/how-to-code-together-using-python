import os
import math
def perimeterOfTriangle(x,y,z):
	p = x + y + z
	print("Perimeter of triangle: {0:.03f}".format(p))
def areaOfTriangle(x,y,z):
	s = (x + y + z) / 2
	ar = math.sqrt(s * (s - x) * (s - y) * (s - z))
	print("Area of triangle: {0:.03f}".format(ar))
print("Enter dimensions of triangle: ")
a = float(input("a = "))
b = float(input("b = "))
c = float(input("c = "))
perimeterOfTriangle(a,b,c)
areaOfTriangle(a,b,c)
os.system("pause")