import os
import math
def areaOfSquare(x):
	area = math.pow(float(x), 2)
	print ("Area of the square is %f." % float(area))
	return
side = input("Measure of all sides in the square to check its area: ")
areaOfSquare(float(side))
os.system("pause")