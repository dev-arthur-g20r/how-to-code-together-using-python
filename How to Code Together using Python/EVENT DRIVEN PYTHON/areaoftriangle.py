import os
def areaOfTriangle(b,h):
	a = b * h / 2
	return a
print("Enter base and height to check area of triangle.")
base = float(input("Base: "))
height = float(input("Height: "))
area = areaOfTriangle(base,height)
print("Area of triangle: ", area)
os.system("pause")