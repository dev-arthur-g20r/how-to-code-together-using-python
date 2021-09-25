import os
import math
def areaOfCircle(r):
	area = math.pi * math.pow(float(r),2)
	print ("Area of circle is %f" % float(area))
	return
radius = input("Radius of circle: ")
areaOfCircle(float(radius))
os.system("pause")