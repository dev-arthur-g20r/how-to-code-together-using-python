import os
import math
def volumeOfSphere(r):
	v = (4/3) * (math.pi) * (r ** 3)
	return v 
radius = float(input("Radius of sphere to determine its volume: "))
volume = volumeOfSphere(radius)
print("Volume of sphere: ", volume)
os.system("pause")