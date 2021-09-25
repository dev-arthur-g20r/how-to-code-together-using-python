import os

class Parallelogram:
	def __init__(self,length,width):
		self.length = length
		self.width = width

class Rectangle(Parallelogram):
	def getPerimeter(self):
		return 2 * (self.width + self.length)
	def getArea(self):
		return self.width * self.length

class Square(Parallelogram):

	def getPerimeter(self):
		return 4 * self.length
	def getArea(self):
		return self.width ** 2

myParallelogram = input("Rectangle or Square? (Complete word please): ")
if (myParallelogram.capitalize() == "Rectangle" or myParallelogram.capitalize() == "Square"):
	try:
		if (myParallelogram.capitalize() == "Rectangle"):
			theLength = float(input("\nLength (l) = "))
			theWidth = float(input("Width (w) = "))
			perimeterFormula = "2 (l + w)"
			areaFormula = "l * w"
			theChosen = Rectangle(theLength,theWidth)
		elif (myParallelogram.capitalize() == "Square"):
			theLength = float(input("\nLength of a side (s) = "))
			theWidth = theLength
			perimeterFormula = "4s"
			areaFormula = "s ** 2 (s by the power of 2)"
			theChosen = Square(theLength,theWidth)

		print("\nPerimeter ({0}) = {1}".format(perimeterFormula,theChosen.getPerimeter()))
		print("Area ({0}) = {1}".format(areaFormula,theChosen.getArea()))
	except:
		print("Sorry! Length and width shall only be numbers.")
else:
	print("\nSorry! Rectangle or square only.")

os.system("pause")