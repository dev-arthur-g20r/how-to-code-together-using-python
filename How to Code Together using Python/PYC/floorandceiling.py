import os
class FloorAndCeiling:
	def __init__(self,n):
		self.n = n
	def floorAndCeiling(self):
		if (float(self.n) == int(self.n)):
			floor = int(self.n)
			ceiling = int(self.n)
		elif (self.n < 0):
			floor = int(self.n - 1)
			ceiling = int(self.n)
		else:
			floor = int(self.n)
			ceiling = int(self.n + 1)
		return "Floor: {}\nCeiling: {}".format(floor,ceiling)
number = float(input("Number to check its floor and ceiling: "))
x = FloorAndCeiling(number)
result = x.floorAndCeiling()
print(result)
os.system("pause")