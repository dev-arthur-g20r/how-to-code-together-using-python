import os
class LCM:
	def lcm(self,n1,n2):
		if (n1 < n2):
			min = n1
			max = n2
		else:
			min = n2
			max = n1
		i = 1
		while (i <= max):
			result = max * i
			if (result % min == 0):
				lcm = result
				break
			i += 1
		print("LCM:",lcm)
x = LCM()
num1 = int(input("Num1: "))
num2 = int(input("Num2: "))
x.lcm(num1,num2)
os.system("pause")