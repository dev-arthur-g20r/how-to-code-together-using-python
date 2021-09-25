import os
import math
def quadratic(x,y,z):
	discRoot = math.sqrt((y ** 2) - (4 * x * z))
	root1 = (-y + discRoot) / (2 * x)
	root2 = (-y - discRoot) / (2 * x)
	print("Root 1:",root1)
	print("Root 2:",root2)
a = eval(input("a = "))
b = eval(input("b = "))
c = eval(input("c = "))
quadratic(a,b,c)
os.system("pause")