import os
import math
def volumeOfCylinder(r,h):
	v = math.pi * (r ** 2) * h
	print("Volume of cylinder: ", v)
	return
radius = float(input("Radius of cylinder: "))
height = float(input("Height of cylinder: "))
volumeOfCylinder(radius,height)
os.system("pause")