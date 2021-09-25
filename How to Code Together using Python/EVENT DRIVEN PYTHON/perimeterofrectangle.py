import os
def perimeterOfRectangle(l,w):
	p = 2 * (l + w)
	return p
print("Enter length and width of rectangle to check its perimeter: ")
length = float(input("Length: "))
width = float(input("Width: "))
perimeter = perimeterOfRectangle(length,width)
print("Perimeter of rectangle: ", perimeter)
os.system("pause")