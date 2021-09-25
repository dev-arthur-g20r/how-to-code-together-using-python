import os
import math
class Circle:
	def __init__(self,r):
		self.r = r 
	def area(self):
		a = math.pi * (self.r ** 2)
		return "Area: {0:.03f}".format(a)
	def circumference(self):
		c = 2 * math.pi * self.r
		return "Circumference: {0:.03f}".format(c)
print("Please enter dimension of circle.")
radius = float(input("Radius: "))
cir = Circle(radius)
area = cir.area()
circumference = cir.circumference()
print(area)
print(circumference)
os.system("pause")