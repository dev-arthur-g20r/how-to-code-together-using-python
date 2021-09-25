import os
import math
def areaOfCircle(r):
	area = math.pi * (r ** 2)
	return area
radius = float(input("Radius of circle to check its area: "))
area = areaOfCircle(radius)
print("Area of circle: ", area)
os.system("pause")