import os
import math
def circumferenceOfCircle(r):
	c = 2 * math.pi * r
	print("Circumference of circle: {0:.03f}".format(c))
def areaOfCircle(r):
	a = math.pi * (r ** 2)
	print("Area of circle: {0:.03f}".format(a))
print("Enter dimension of circle:")
radius = float(input("Radius of circle: "))
circumferenceOfCircle(radius)
areaOfCircle(radius)
os.system("pause")