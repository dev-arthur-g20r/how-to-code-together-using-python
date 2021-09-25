import os
def areaOfRectangle(l,w):
	a = l * w
	return a 
print("Enter length and width to determine area of rectangle: ")
length = float(input("Length: "))
width = float(input("Width: "))
area = areaOfRectangle(length,width)
print("Area of rectangle: ", area)
os.system("pause")