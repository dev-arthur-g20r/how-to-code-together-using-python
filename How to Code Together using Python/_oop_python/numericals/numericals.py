class Numbers:
	def __init__(self,number):
		self.number = number

	def isOddOrEven(self):
		if (self.number % 2 == 0):
			return "{0} is EVEN.".format(self.number)
		else:
			return "{0} is ODD.".format(self.number)

	def isHarshad(self):
		copy = self.number
		sum = 0
		while (copy > 0):
			remainder = copy % 10
			sum += remainder
			copy //= 10
		if (self.number % sum == 0):
			return "{0} is Harshad.".format(self.number)
		else:
			return "{0} is not Harshad.".format(self.number)

	def isDisarium(self):
		copy = self.number
		str_num = str(copy)
		length = len(str_num)
		sum = 0
		while (copy > 0):
			remainder = copy % 10
			sum += remainder ** length
			length -= 1
			copy //= 10
		if (sum == self.number):
			return "{0} is Disarium.".format(self.number)
		else:
			return "{0} is not Disarium.".format(self.number)
			
	def isArmstrong(self):
		copy = self.number
		str_num = str(copy)
		length = len(str_num)
		sum = 0
		while (copy > 0):
			remainder = copy % 10
			sum += remainder ** length
			copy //= 10
		if (sum == self.number):
			return "{0} is Armstrong.".format(self.number)
		else:
			return "{0} is not Armstrong.".format(self.number)