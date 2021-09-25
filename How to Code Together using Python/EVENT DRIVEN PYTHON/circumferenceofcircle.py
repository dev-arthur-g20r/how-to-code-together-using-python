import os
import math
def circumferenceOfCircle(r):
	c = 2 * math.pi * r
	return c
radius = float(input("Radius of circle to check circle's circumference: "))
circumference = circumferenceOfCircle(radius)
print("Circumference of circle: ", circumference)
os.system("pause")