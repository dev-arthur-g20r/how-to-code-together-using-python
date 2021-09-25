import os
import math
class Rectangle:
	def __init__(self,l,w):
		self.l = l
		self.w = w
	def area(self):
		a = self.l * self.w
		return "Area: {0:.03f}".format(a)
	def perimeter(self):
		p = 2 * (self.l + self.w)
		return "Perimeter: {0:.03f}".format(p)
print("Please enter dimensions of rectangle.")
length = float(input("Length: "))
width = float(input("Width: "))
rect = Rectangle(length,width)
area = rect.area()
perimeter = rect.perimeter()
print(area)
print(perimeter)
os.system("pause")