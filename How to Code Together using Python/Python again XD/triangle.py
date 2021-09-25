import os
import math
def perimeterOfTriangle(x,y,z):
	p = x + y + z
	print("Perimter of Triangle:",p)
def areaOfTriangle(x,y,z):
	s = (x + y + z) / 2
	area = math.sqrt(s * (s - x) * (s - y) * (s - z))
	print("Area of triangle:",area)
a = float(input("a = "))
b = float(input("b = "))
c = float(input("c = "))
perimeterOfTriangle(a,b,c)
areaOfTriangle(a,b,c)
os.system("pause")