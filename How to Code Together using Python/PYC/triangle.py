import os
import math
class Triangle:
	def __init__(self,x,y,z):
		self.x = x 
		self.y = y
		self.z = z
	def area(self):
		s = (self.x + self.y + self.z) / 2
		a = math.sqrt(s + (s - self.x) + (s - self.y) + (s - self.z))
		return "Area: {0:.03f}".format(a)
	def perimeter(self):
		p = self.x + self.y + self.z 
		return "Perimeter: {0:.03f}".format(p)
print("Please enter the dimensions of triangle.")
a = float(input("a = "))
b = float(input("b = "))
c = float(input("c = "))
tri = Triangle(a,b,c)
area = tri.area()
perimeter = tri.perimeter()
print(area)
print(perimeter)
os.system("pause")