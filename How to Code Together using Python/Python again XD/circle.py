import os
import math
def circumference(r):
	p = 2 * math.pi * r
	print("Circumference of circle:",p)
def areaOfCircle(r):
	a = math.pi * (r ** 2)
	print("Area of circle:",a)
radius = float(input("Radius of circle: "))
circumference(radius)
areaOfCircle(radius)
os.system("pause")