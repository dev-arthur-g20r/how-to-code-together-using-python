import os
import math
def volumeOfCone(r,h):
	volume = math.pi * (r ** 2) * (h / 3)
	print("Volume of cone: ", volume)
	return
radius = float(input("Radius of cone: "))
height = float(input("Height of cone: "))
volumeOfCone(radius,height)
os.system("pause")