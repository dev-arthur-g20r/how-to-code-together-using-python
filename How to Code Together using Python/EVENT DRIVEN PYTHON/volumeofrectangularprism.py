import os
def volumeOfRectangularPrism(l,w,h):
	volume = l * w * h
	print("Volume of rectangular prism: ", volume)
	return
print("Enter length, width and height of rectangular prism to check its volume: ")
length = float(input("Length: "))
width = float(input("Width: "))
height = float(input("Height: "))
volumeOfRectangularPrism(length,width,height)
os.system("pause")