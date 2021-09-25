import os
class KrishnamurthyNumber:
	def isKrishnamurthy(self,n):
		copy = n
		sum = 0
		while (copy > 0):
			remainder = copy % 10
			factorial = 1
			while (remainder > 0):
				factorial *= remainder
				remainder -= 1
			sum += factorial
			copy = copy // 10
		if (sum == n):
			print(n,"is Krishnamurthy.")
		else:
			print(n,"is not Krishnamurthy.")
x = KrishnamurthyNumber()
number = int(input("Number to check if Krishnamurthy: "))
x.isKrishnamurthy(number)
os.system("pause")