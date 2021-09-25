import os
class Square:
	def __init__(self,s):
		self.s = s
	def area(self):
		a = self.s ** 2
		return "Area: {0:.03f}".format(a)
	def perimeter(self):
		p = 4 * self.s 
		return "Perimeter: {0:.03f}".format(p)
print("Enter dimension of square.")
side = float(input("Side: "))
sq = Square(side)
area = sq.area()
perimeter = sq.perimeter()
print(area)
print(perimeter)
os.system("pause")