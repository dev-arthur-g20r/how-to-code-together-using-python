import os
import math
def perimeterOfRectangle(l,w):
	p = 2 * (l + w)
	print("Perimeter of rectangular:",p)
def areaOfRectangle(l,w):
	a = l * w
	print("Area of rectangle:",a)
length = float(input("Length of rectangle: "))
width = float(input("Width of rectangle: "))
perimeterOfRectangle(length,width)
areaOfRectangle(length,width)
os.system("pause")