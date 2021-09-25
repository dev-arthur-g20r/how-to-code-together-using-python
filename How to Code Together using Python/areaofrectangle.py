import os
import math
def areaOfRectangle(b,h):
	area = float(b) * float(h)
	print ("Area of the rectangle is %f" % float(area))
	return

base = input("Base of rectangle: ")
height = input("Height of rectangle: ")
areaOfRectangle(float(base),float(height))
os.system("pause")