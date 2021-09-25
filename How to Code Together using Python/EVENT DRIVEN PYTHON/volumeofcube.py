import os
def volumeOfCube(a):
	v = a ** 3
	print("Volume of cube: ", v)
	return
side = float(input("Side of a cube (length): "))
volumeOfCube(side)
os.system("pause")