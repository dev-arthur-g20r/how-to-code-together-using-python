import os
def perimeterOfRectangle(l,w):
	p = 2 * (l + w)
	print("Perimeter of rectangle: {0:.03f}".format(p))
def areaOfRectangle(l,w):
	a = l * w
	print("Area of rectangle: {0:.03f}".format(a))
print("Enter dimensions of rectangle:")
length = float(input("Length = "))
width = float(input("Width = "))
perimeterOfRectangle(length,width)
areaOfRectangle(length,width)
os.system("pause")