import os
class AdamNumber:
	def isAdam(self,n):
		copy1 = n
		square1 = n ** 2
		sum1 = 0
		while (copy1 > 0):
			remainder1 = copy1 % 10
			sum1 = (sum1 * 10) + remainder1
			copy1 = copy1 // 10
		square2 = sum1 ** 2
		copy2 = square2
		sum2 = 0
		while (copy2 > 0):
			remainder2 = copy2 % 10
			sum2 = (sum2 * 10) + remainder2
			copy2 = copy2 // 10
		if (sum2 == square1):
			return "{} is Adam.".format(n)
		else:
			return "{} is not Adam.".format(n)
x = AdamNumber()
number = int(input("Number to check if Adam: "))
result = x.isAdam(number)
print(result)
os.system("pause")